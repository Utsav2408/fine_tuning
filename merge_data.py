import os
import json

def merge_json_folder(json_path, output_path="merged.json"):
    """
    Merges all JSON files in a folder into a single JSON file.

    Args:
        json_path (str): Path to the folder containing JSON files.
        output_path (str): Path to output the merged JSON file.

    Returns:
        int: Number of JSON objects merged.
    """
    merged_data = []

    # List all files ending with .json (ignore hidden and the output file itself)
    for filename in os.listdir(json_path):
        if filename.endswith('.json') and filename != output_path and not filename.startswith('.'):
            file_path = os.path.join(json_path, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    # If each file is a dict, append; if it's a list, extend
                    if isinstance(data, list):
                        merged_data.extend(data)
                    else:
                        merged_data.append(data)
                except Exception as e:
                    print(f"Could not read {filename}: {e}")

    # Write merged result
    out_file = os.path.join("data/pre_final", output_path)
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, indent=2, ensure_ascii=False)

    print(f"Merged {len(merged_data)} objects into {out_file}")
    return len(merged_data)


if __name__ == "__main__":
    merge_json_folder("data/jsons")