import json
import threading

SESSION_MAP_FILE = "backend/session_collect_id_map.json"
SESSION_MAP_LOCK = threading.Lock()

def load_session_map():
    try:
        with open(SESSION_MAP_FILE, "r") as f:
            session_map = json.load(f)
            print(f"Loaded session map: {session_map}")
            return session_map
    except Exception as e:
        print(f"Failed to load session map: {e}")
        return {}

def save_session_map(session_map):
    try:
        with open(SESSION_MAP_FILE, "w") as f:
            json.dump(session_map, f)
        print(f"Saved session map: {session_map}")
    except Exception as e:
        print(f"Failed to save session map: {e}")