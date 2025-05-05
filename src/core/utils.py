import json
from datetime import datetime
from typing import Any, Dict

def format_timestamp() -> str:
    """Return ISO-formatted current time."""
    return datetime.now().isoformat()

def safe_json_parse(data: str) -> Dict[str, Any]:
    """Safely parse JSON with error handling."""
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return {}
    