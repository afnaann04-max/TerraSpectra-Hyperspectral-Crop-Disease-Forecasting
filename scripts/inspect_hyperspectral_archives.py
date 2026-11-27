
"""
TerraSpectra - Hyperspectral Archive Inspector

Purpose:
Inspect ZIP archive contents without extracting large files.
Identify file formats, archive sizes and folder structures.
"""

import argparse
import zipfile
from pathlib import Path
from collections import Counter


def format_size(size):
    """Convert bytes into a readable size."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"


def inspect_archive(archive_path):
    """Inspect a ZIP archive without extracting its contents."""

    archive_path = Path(archive_path)

    print("\n" + "=" * 65)
    print(f"ARCHIVE: {archive_path.name}")
    print("=" * 65)

    if not archive_path.exists():
        print("ERROR: Archive file not found.")
        return

    if not zipfile.is_zipfile(archive_path):
        print("ERROR: Invalid or unsupported ZIP archive.")
        return

    try:
        with zipfile.ZipFile(archive_path, "r") as archive:

            files = [
                item for item in archive.infolist()
                if not item.is_dir()
            ]

            extensions = Counter(
                Path(item.filename).suffix.lower() or "[no extension]"
                for item in files
            )

            total_size = sum(item.file_size for item in files)
            compressed_size = sum(
                item.compress_size for item in files
            )

            print(f"Total files       : {len(files)}")
            print(f"Compressed size   : {format_size(compressed_size)}")
            print(f"Uncompressed size : {format_size(total_size)}")

            print("\nFILE FORMATS")
            print("-" * 40)

            for extension, count in extensions.most_common():
                print(f"{extension:<20} {count}")

            print("\nFIRST 20 FILES")
            print("-" * 65)

            for item in files[:20]:
                print(
                    f"{item.filename}\n"
                    f"    Size: {format_size(item.file_size)}"
                )

            print("\nArchive inspection completed.")

    except (OSError, zipfile.BadZipFile, RuntimeError) as error:
        print(f"ERROR while inspecting archive: {error}")


def main():
    parser = argparse.ArgumentParser(
        description="Inspect TerraSpectra hyperspectral ZIP archives."
    )

    parser.add_argument(
        "archives",
        nargs="+",
        help="Paths to VNIR or SWIR ZIP archives."
    )

    args = parser.parse_args()

    for archive in args.archives:
        inspect_archive(archive)


if __name__ == "__main__":
    main()
