from zipfile import ZipFile
from pathlib import Path
from collections import defaultdict
from PIL import Image
import pandas as pd
import json

ARCHIVE = Path(r"C:\Users\Afnan\Downloads\Dataset for Crop Pest and Disease Detection.zip")
INVENTORY = Path("reports/ccmt_hash_overlap/ccmt_hash_file_inventory.csv")
OUTPUT = Path("reports/ccmt_hash_overlap")

OUTPUT.mkdir(parents=True, exist_ok=True)

def calculate_dhash(image_bytes):
    import io

    with Image.open(io.BytesIO(image_bytes)) as image:
        image = image.convert("L").resize(
            (9, 8), Image.Resampling.LANCZOS
        )
        pixels = list(image.getdata())

    value = 0
    for y in range(8):
        for x in range(8):
            left = pixels[y * 9 + x]
            right = pixels[y * 9 + x + 1]
            value = (value << 1) | int(left > right)

    return value

def hamming_distance(hash1, hash2):
    return (hash1 ^ hash2).bit_count()

print("Reading inventory...")
df = pd.read_csv(INVENTORY)

train = df[df["split"] == "train"].copy()
test = df[df["split"] == "test"].copy()

train_sha = set(train["sha256"])
test_nonexact = test[~test["sha256"].isin(train_sha)].copy()

print("Train images:", len(train))
print("Total Test images:", len(test))
print("Non-exact Test images:", len(test_nonexact))

train_records = train.to_dict("records")
test_records = test_nonexact.to_dict("records")

print("\nOpening ZIP and calculating Train dHash values...")
train_hashes = []

with ZipFile(ARCHIVE) as z:
    for i, record in enumerate(train_records, 1):
        try:
            image_bytes = z.read(record["filename"])
            dhash = calculate_dhash(image_bytes)
            train_hashes.append((record, dhash))
        except Exception as error:
            print("Train image error:", record["filename"], error)

        if i % 2000 == 0:
            print(f"Train processed: {i}/{len(train_records)}")

    print("\nCalculating Test dHash values and comparing...")
    candidate_rows = []
    nearest_rows = []

    for i, test_record in enumerate(test_records, 1):
        try:
            image_bytes = z.read(test_record["filename"])
            test_hash = calculate_dhash(image_bytes)
        except Exception as error:
            print("Test image error:", test_record["filename"], error)
            continue

        nearest_distance = 65
        nearest_record = None

        for train_record, train_hash in train_hashes:
            distance = hamming_distance(test_hash, train_hash)

            if distance < nearest_distance:
                nearest_distance = distance
                nearest_record = train_record

            if distance <= 8:
                candidate_rows.append({
                    "test_filename": test_record["filename"],
                    "test_class": test_record["class"],
                    "train_filename": train_record["filename"],
                    "train_class": train_record["class"],
                    "dhash_distance": distance
                })

        if nearest_record is not None:
            nearest_rows.append({
                "test_filename": test_record["filename"],
                "test_class": test_record["class"],
                "nearest_train_filename": nearest_record["filename"],
                "nearest_train_class": nearest_record["class"],
                "nearest_dhash_distance": nearest_distance
            })

        if i % 100 == 0:
            print(f"Test processed: {i}/{len(test_records)}")

candidate_df = pd.DataFrame(candidate_rows)
nearest_df = pd.DataFrame(nearest_rows)

candidate_path = OUTPUT / "ccmt_dhash_candidate_pairs_le8.csv"
nearest_path = OUTPUT / "ccmt_dhash_nearest_train_matches.csv"
summary_path = OUTPUT / "ccmt_dhash_candidate_summary.json"

candidate_df.to_csv(candidate_path, index=False)
nearest_df.to_csv(nearest_path, index=False)

summary = {
    "method": "64-bit Difference Hash (dHash)",
    "image_conversion": "Grayscale",
    "resize": "9x8 using Pillow LANCZOS",
    "comparison": "Horizontal adjacent-pixel differences",
    "distance_metric": "Hamming distance",
    "candidate_threshold": 8,
    "train_images_in_inventory": len(train),
    "test_images_in_inventory": len(test),
    "exact_sha256_test_matches_excluded": len(test) - len(test_nonexact),
    "non_exact_test_images": len(test_nonexact),
    "train_images_successfully_hashed": len(train_hashes),
    "test_images_with_nearest_match": len(nearest_df),
    "candidate_pairs_at_distance_8_or_less": len(candidate_df),
    "test_images_with_nearest_distance_le_2": int((nearest_df["nearest_dhash_distance"] <= 2).sum()),
    "test_images_with_nearest_distance_le_4": int((nearest_df["nearest_dhash_distance"] <= 4).sum()),
    "test_images_with_nearest_distance_le_6": int((nearest_df["nearest_dhash_distance"] <= 6).sum()),
    "test_images_with_nearest_distance_le_8": int((nearest_df["nearest_dhash_distance"] <= 8).sum()),
    "test_images_with_nearest_distance_zero": int((nearest_df["nearest_dhash_distance"] == 0).sum())
}

summary_path.write_text(json.dumps(summary, indent=4), encoding="utf-8")

print("\nCompleted.")
print(json.dumps(summary, indent=4))
print("\nSaved files:")
print(candidate_path)
print(nearest_path)
print(summary_path)
