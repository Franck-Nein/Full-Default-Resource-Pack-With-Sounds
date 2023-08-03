import os
import json
import shutil
import argparse

def copy_file_with_directories(src_path, dest_path):
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    shutil.copy2(src_path, dest_path)

def copy_files_from_json(json_file, base_src_dir, base_dest_dir):
    with open(json_file) as f:
        json_data = json.load(f)

    for rel_path, obj_data in json_data["objects"].items():
        src_hash = obj_data["hash"]
        src_file = os.path.join(base_src_dir, src_hash[:2], src_hash)
        dest_file = os.path.join(base_dest_dir, rel_path)
        copy_file_with_directories(src_file, dest_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy files from JSON data to the destination directory.")
    parser.add_argument("json_file", help="Path to the JSON data file")
    parser.add_argument("src_dir", help="Base source directory(objects)")
    parser.add_argument("dest_dir", help="Base destination directory")
    args = parser.parse_args()

    # Call the function to copy the files
    copy_files_from_json(args.json_file, args.src_dir, args.dest_dir)

