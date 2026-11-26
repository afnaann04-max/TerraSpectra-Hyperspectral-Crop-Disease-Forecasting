import argparse
import csv
import hashlib
import json
import zipfile
from collections import defaultdict
from pathlib import Path

CLASSES = {
    "healthy",
    "leaf blight",
    "leaf curl",
    "septoria leaf spot",
    "verticulium wilt",
}

EXTENSIONS = {".jpg", ".jpeg", ".png"}

RAW_PREFIX = (
    "Dataset for Crop Pest and Disease Detection/"
    "Raw Data/CCMT Dataset/Tomato/"
)

AUG_PREFIX = (
    "Dataset for Crop Pest and Disease Detection/"
    "CCMT Dataset-Augmented/Tomato/"
)


def get_file_info(name):
    parts = name.split("/")

    if len(parts) != 6:
        return None

    if Path(parts[-1]).suffix.lower() not in EXTENSIONS:
        return None

    if parts[0] != "Dataset for Crop Pest and Disease Detection":
        return None

    return parts


def hash_entry(archive, info):
    digest = hashlib.sha256()

    with archive.open(info, "r") as stream:
        while True:
            chunk = stream.read(1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)

    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(
        description="Verify exact CCMT Raw-to-Augmented SHA-256 matches."
    )

    parser.add_argument(
        "--archive",
        default=str(
            Path.home()
            / "Downloads"
            / "Dataset for Crop Pest and Disease Detection.zip"
        ),
    )

    parser.add_argument(
        "--output",
        default="reports/ccmt_raw_to_augmented",
    )

    args = parser.parse_args()

    archive_path = Path(args.archive)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    if not archive_path.is_file():
        raise FileNotFoundError(archive_path)

    raw_map = defaultdict(list)
    augmented_map = {
        "train": defaultdict(list),
        "test": defaultdict(list),
    }

    raw_inventory = defaultdict(int)
    augmented_inventory = defaultdict(int)

    print("Archive:", archive_path)
    print("Calculating SHA-256 hashes from ZIP streams.")
    print("No image extraction or modification.")

    with zipfile.ZipFile(archive_path, "r") as archive:
        for info in archive.infolist():
            if info.is_dir():
                continue

            name = info.filename

            if name.startswith(RAW_PREFIX):
                parts = get_file_info(name)

                if parts is None or parts[1] != "Raw Data":
                    continue

                class_name = parts[4].lower()
                digest = hash_entry(archive, info)

                raw_map[digest].append({
                    "class": class_name,
                    "filename": name,
                })

                raw_inventory[class_name] += 1

            elif name.startswith(AUG_PREFIX):
                parts = get_file_info(name)

                if parts is None or parts[1] != "CCMT Dataset-Augmented":
                    continue

                split_folder = parts[3].lower()

                if split_folder not in {"train_set", "test_set"}:
                    continue

                split = (
                    "train" if split_folder == "train_set" else "test"
                )

                class_name = parts[4].lower()
                digest = hash_entry(archive, info)

                augmented_map[split][digest].append({
                    "class": class_name,
                    "filename": name,
                })

                augmented_inventory[(split, class_name)] += 1

    rows = []
    matched_raw_hashes = set()
    matched_raw_entries = set()

    for split in ("train", "test"):
        for digest, augmented_files in augmented_map[split].items():
            if digest not in raw_map:
                continue

            matched_raw_hashes.add(digest)

            for raw_file in raw_map[digest]:
                matched_raw_entries.add(raw_file["filename"])

                for augmented_file in augmented_files:
                    rows.append({
                        "sha256": digest,
                        "raw_class": raw_file["class"],
                        "raw_filename": raw_file["filename"],
                        "augmented_split": split,
                        "augmented_class": augmented_file["class"],
                        "augmented_filename": augmented_file["filename"],
                        "class_labels_agree": (
                            raw_file["class"] == augmented_file["class"]
                        ),
                    })

    raw_total = sum(raw_inventory.values())
    train_total = sum(
        augmented_inventory[("train", c)] for c in CLASSES
    )
    test_total = sum(
        augmented_inventory[("test", c)] for c in CLASSES
    )

    summary = {
        "archive": str(archive_path),
        "method": "SHA-256 over ZIP entry content streams",
        "images_extracted": False,
        "raw_images_modified": False,
        "inventory": {
            "raw_total": raw_total,
            "train_total": train_total,
            "test_total": test_total,
            "raw_by_class": dict(raw_inventory),
            "augmented_by_split_and_class": {
                f"{split}/{c}": augmented_inventory[(split, c)]
                for split in ("train", "test")
                for c in sorted(CLASSES)
            },
        },
        "raw_to_augmented": {
            "unique_raw_sha256_values": len(raw_map),
            "unique_matched_raw_sha256_values": len(matched_raw_hashes),
            "raw_file_entries_with_exact_match": len(matched_raw_entries),
            "raw_file_entries_without_exact_match": (
                raw_total - len(matched_raw_entries)
            ),
            "raw_to_augmented_exact_file_pairs": len(rows),
            "train_exact_match_pairs": sum(
                1 for row in rows if row["augmented_split"] == "train"
            ),
            "test_exact_match_pairs": sum(
                1 for row in rows if row["augmented_split"] == "test"
            ),
            "class_label_agreement_pairs": sum(
                1 for row in rows if row["class_labels_agree"]
            ),
            "class_label_disagreement_pairs": sum(
                1 for row in rows if not row["class_labels_agree"]
            ),
        },
        "limitations": [
            "Exact SHA-256 matches establish identical file content only.",
            "A matching file does not establish biological sample identity.",
            "Non-matching files may still be transformed versions of raw images.",
            "This comparison does not establish complete original-to-augmented lineage.",
            "Matching class folder names do not independently verify disease labels.",
        ],
    }

    csv_path = output_dir / "ccmt_raw_to_augmented_exact_matches.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "sha256",
            "raw_class",
            "raw_filename",
            "augmented_split",
            "augmented_class",
            "augmented_filename",
            "class_labels_agree",
        ])
        writer.writeheader()
        writer.writerows(rows)

    json_path = output_dir / "ccmt_raw_to_augmented_summary.json"
    with json_path.open("w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2)

    print("\nInventory:")
    print("Raw:", raw_total)
    print("Train:", train_total)
    print("Test:", test_total)

    print("\nRaw-to-Augmented SHA-256 results:")
    print(json.dumps(summary["raw_to_augmented"], indent=2))

    print("\nReports saved:")
    print(csv_path)
    print(json_path)


if __name__ == "__main__":
    main()
