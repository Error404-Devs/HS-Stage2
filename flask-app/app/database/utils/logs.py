import os
from app.database.utils.file_handler import read_json, write_json, append_json
from app.database.models.users import User
from app.database.models.tags import Tag
from app.database.models.logs import Log
from datetime import datetime

def get_all_logs():
    file_path = os.path.join("app", "database", "storage", "logs.json")
    return read_json(file_path)

def insert_log(log_id: str, message: str, data: str):
    file_path = os.path.join("app", "database", "storage", "logs.json")
    try:
        log_data = {
            "id": log_id,
            "message": message,
            "component_data": data,
            "date_logged": datetime.now().isoformat()
        }
        append_json(file_path, log_data)

        return log_data, None
    except Exception as e:
        return None, {"error": f"Error inserting log: {str(e)}"}


# def update_tag(tag_id: str, updated_fields: dict):
#     file_path = os.path.join("app", "database", "storage", "tags.json")
    
#     tags = read_json(file_path)

#     tag = next((tag for tag in tags if tag['id'] == tag_id), None)

#     if tag is None:
#         return None, {"error": f"Tag with ID {tag_id} not found."}

#     try:
#         new_user_id = updated_fields.get("data", {}).get("id")

#         if new_user_id:
#             for existing_tag in tags:
#                 if existing_tag["id"] != tag_id and existing_tag.get("data", {}).get("id") == new_user_id:
#                     existing_tag["data"] = {}

#         for field, value in updated_fields.items():
#             tag[field] = value

#         write_json(file_path, tags)

#         return {"message": f"Tag with ID {tag_id} updated successfully."}, None
#     except Exception as e:
#         return None, {"error": f"Validation failed: {str(e)}"} 



# def delete_tag(tag_id: str):
#     file_path = os.path.join("app", "database", "storage", "tags.json")

#     tags = read_json(file_path)

#     if not isinstance(tags, list):
#         return False, "Invalid data format"

#     updated_data = [tag for tag in tags if tag.get("id") != tag_id]

#     if len(updated_data) == len(tags):
#         return False, "Tag not found"

#     write_json(file_path, updated_data)

#     return True, "Tag deleted successfully"