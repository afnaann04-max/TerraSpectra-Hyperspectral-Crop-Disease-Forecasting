
import argparse
import csv
import hashlib
import json
import re
import zipfile
import zlib
from collections import defaultdict
from pathlib import Path

CLASSES = {
    "healthy",
    "leaf blight",
    "leaf curl",
    "septoria leaf spot",
    "verticulium wilt",
}

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}

PREFIX = (
    "Dataset for Crop Pest and Disease Detection/"
    "CCMT Dataset-Augmented/Tomato/"
)


def is_target_image(info, split):
    parts = info.filename.split("/")

    return (
        len(parts) == 6
        and parts[0] == "Dataset for Crop Pest and Disease Detection"
        and parts[1] == "CCMT Dataset-Augmented"
        and parts[2] == "Tomato"
        and parts[3] == split
        and parts[4].lower() in CLASSES
        and Path(parts[5]).suffix.lower() in IMAGE_EXTENSIONS
        and not info.is_dir()
    )

def hash_entry(archive, info):
    sha256 = hashlib.sha256()
    crc32 = 0
    size = 0

    with archive.open(info, "r") as stream:
        while True:
            chunk = stream.read(1024 * 1024)
            if not chunk:
                break
            sha256.update(chunk)
            crc32 = zlib.crc32(chunk, crc32)
            size += len(chunk)

    return sha256.hexdigest(), f"{crc32 & 0xffffffff:08x}", size


def summarize(train_map, test_map):
    shared = set(train_map) & set(test_map)

    matched_test_entries = sum(len(test_map[key]) for key in shared)
    matched_train_entries = sum(len(train_map[key]) for key in shared)
    matching_pairs = sum(
        len(train_map[key]) * len(test_map[key]) for key in shared
    )

    return {
        "unique_shared_hash_values": len(shared),
        "test_entries_with_train_match": matched_test_entries,
        "train_entries_with_test_match": matched_train_entries,
        "train_test_matching_file_pairs": matching_pairs,
        "unmatched_test_entries": sum(
            len(v) for k, v in test_map.items() if k not in shared
        ),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Verify CCMT Tomato Train-Test hash overlap."
    )
    parser.add_argument(
        "--archive",
        default=str(
            Path.home()
            / "Downloads"
            / "Dataset for Crop Pest and Disease Detection (1).zip"
        ),
        help="Path to the CCMT ZIP archive",
    )
    parser.add_argument(
        "--output",
        default="reports/ccmt_hash_overlap",
        help="Directory for verification reports",
    )
    args = parser.parse_args()

    archive_path = Path(args.archive)
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    if not archive_path.is_file():
        raise FileNotFoundError(f"Archive not found: {archive_path}")

    maps = {
        "sha256": {"train": defaultdict(list), "test": defaultdict(list)},
        "crc32": {"train": defaultdict(list), "test": defaultdict(list)},
    }
    inventory = defaultdict(int)
    file_records = []

    print(f"Archive: {archive_path}")
    print("Reading archive entries and calculating hashes...")

    with zipfile.ZipFile(archive_path, "r") as archive:
        for info in archive.infolist():
            split = None

            for candidate in ("train_set", "test_set"):
                if is_target_image(info, candidate):
                    split = candidate
                    break

            if split is None:
                continue

            split_label = "train" if split == "train_set" else "test"
            class_name = info.filename.split("/")[4].lower()

            sha, crc, size = hash_entry(archive, info)

            maps["sha256"][split_label][sha].append(info.filename)
            maps["crc32"][split_label][crc].append(info.filename)

            inventory[(split_label, class_name)] += 1

            file_records.append({
                "split": split_label,
                "class": class_name,
                "filename": info.filename,
                "size_bytes": size,
                "sha256": sha,
                "crc32": crc,
            })

    print("\nInventory:")
    for split in ("train", "test"):
        total = 0
        for class_name in sorted(CLASSES):
            count = inventory[(split, class_name)]
            total += count
            print(f"  {split:5} | {class_name:20} | {count}")
        print(f"  {split:5} | TOTAL                | {total}")

    sha_summary = summarize(
        maps["sha256"]["train"], maps["sha256"]["test"]
    )
    crc_summary = summarize(
        maps["crc32"]["train"], maps["crc32"]["test"]
    )

    sha_shared = set(maps["sha256"]["train"]) & set(maps["sha256"]["test"])
    crc_shared = set(maps["crc32"]["train"]) & set(maps["crc32"]["test"])

    summary = {
        "archive": str(archive_path),
        "method": {
            "sha256": "Calculated from ZIP entry content streams",
            "crc32": "Independently calculated using zlib.crc32",
            "images_extracted": False,
            "raw_images_modified": False,
        },
        "inventory": {
            "train": sum(
                inventory[("train", c)] for c in CLASSES
            ),
            "test": sum(
                inventory[("test", c)] for c in CLASSES
            ),
            "by_split_and_class": {
                f"{split}/{c}": inventory[(split, c)]
                for split in ("train", "test")
                for c in sorted(CLASSES)
            },
        },
        "sha256": sha_summary,
        "crc32": crc_summary,
        "comparison": {
            "same_shared_hash_value_count": len(sha_shared) == len(crc_shared),
            "same_matched_test_entry_count": (
                sha_summary["test_entries_with_train_match"]
                == crc_summary["test_entries_with_train_match"]
            ),
            "same_matching_file_pair_count": (
                sha_summary["train_test_matching_file_pairs"]
                == crc_summary["train_test_matching_file_pairs"]
            ),
            "sha256_shared_values": len(sha_shared),
            "crc32_shared_values": len(crc_shared),
        },
        "limitations": [
            "CRC32 is not collision-resistant and is not proof of identity.",
            "Matching hashes indicate identical file content, not biological sample identity.",
            "Hash comparison does not establish original-to-augmented lineage.",
            "Hash comparison does not establish complete biological sample independence.",
            "Near-duplicate image comparison was not performed.",
        ],
    }

    summary_path = output_dir / "ccmt_hash_overlap_summary.json"
    with summary_path.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    inventory_path = output_dir / "ccmt_hash_file_inventory.csv"
    with inventory_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=file_records[0].keys())
        writer.writeheader()
        writer.writerows(file_records)

    match_path = output_dir / "ccmt_train_test_hash_matches.csv"
    with match_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "sha256",
            "crc32",
            "train_filename",
            "test_filename",
        ])

        sha_to_crc = {}
        for record in file_records:
            sha_to_crc[record["sha256"]] = record["crc32"]

        for digest in sorted(sha_shared):
            for train_file in maps["sha256"]["train"][digest]:
                for test_file in maps["sha256"]["test"][digest]:
                    writer.writerow([
                        digest,
                        sha_to_crc[digest],
                        train_file,
                        test_file,
                    ])

    print("\nSHA-256 results:")
    print(json.dumps(sha_summary, indent=2))
    print("\nCRC32 results:")
    print(json.dumps(crc_summary, indent=2))
    print("\nHash method comparison:")
    print(json.dumps(summary["comparison"], indent=2))

    print("\nReports saved:")
    print(summary_path)
    print(inventory_path)
    print(match_path)


if __name__ == "__main__":
    main()
