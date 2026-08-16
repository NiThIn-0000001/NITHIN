import json
import os

def parse_pipeline_log(file_contents: str) -> dict:
    try:
        data = json.loads(file_contents)
    except json.JSONDecodeError:
        print("[ERROR] Invalid JSON format.")
        return None

    if not isinstance(data, dict):
        print("[ERROR] Expected JSON object, got different structure.")
        return None

    for field in ["job_id", "status"]:
        if field not in data:
            print(f"[ERROR] Missing required field: {field}")
            return None

    summary = {
        "job_id": data["job_id"],
        "status": data["status"].upper(),
        "error_count": len(data.get("errors", []))
    }

    return summary


# --- GET DIRECTORY OF ABC.PY AUTOMATICALLY ---
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "sample.json")

with open(json_path, "r") as file:
    content = file.read()

result = parse_pipeline_log(content)
print("Result:", result)