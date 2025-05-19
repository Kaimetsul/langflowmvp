import json
from pathlib import Path

def load_custom_flow(flow_file_path: str) -> dict:
    """Load a custom Langflow flow from a JSON file."""
    try:
        with open(flow_file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading custom flow: {e}")
        return {} 