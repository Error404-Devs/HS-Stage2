import os
from app.database.utils.file_handler import read_json, write_json, append_json
from app.database.models.users import User
from app.database.models.tags import Tag


def get_all_tags():
    file_path = os.path.join("app", "database", "storage", "tags.json")
    return read_json(file_path)

def insert_tag(tag_id: str, name: str, user: User):
    file_path = os.path.join("app", "database", "storage", "tags.json")

    existing_tags = read_json(file_path)

    if any(tag["id"] == tag_id for tag in existing_tags):
        return None, {"error": f"Tag with ID {tag_id} already exists."}

    try:
        new_tag = Tag(
            id=tag_id,
            name=name,
            data=user,
        )

        append_json(file_path, new_tag.__dict__)

        return {"message": f"Tag with name {name} inserted successfully."}, None
    except Exception as e:
        return None, {"error": f"Error inserting tag: {str(e)}"}

<<<<<<< HEAD

def update_tag(tag_id: str, updated_fields: dict):
    file_path = os.path.join("app", "database", "storage", "tags.json")
    
=======
def update_tag(tag_id: str, updated_fields: dict):
    file_path = os.path.join("app", "database", "storage", "tags.json")

>>>>>>> upstream/main
    tags = read_json(file_path)

    tag = next((tag for tag in tags if tag['id'] == tag_id), None)

    if tag is None:
        return None, {"error": f"Tag with ID {tag_id} not found."}

    try:
<<<<<<< HEAD
        new_user_id = updated_fields.get("data", {}).get("id")

        if new_user_id:
            for existing_tag in tags:
                if existing_tag["id"] != tag_id and existing_tag.get("data", {}).get("id") == new_user_id:
                    existing_tag["data"] = {}
=======
        updated_tag_data = {**tag, **updated_fields}
        # valid_tag = Tag.model_validate(updated_tag_data)
>>>>>>> upstream/main

        for field, value in updated_fields.items():
            tag[field] = value

        write_json(file_path, tags)

        return {"message": f"Tag with ID {tag_id} updated successfully."}, None
    except Exception as e:
<<<<<<< HEAD
        return None, {"error": f"Validation failed: {str(e)}"} 

=======
        return None, {"error": f"Validation failed: {str(e)}"}
>>>>>>> upstream/main


def delete_tag(tag_id: str):
    file_path = os.path.join("app", "database", "storage", "tags.json")

    tags = read_json(file_path)

    if not isinstance(tags, list):
        return False, "Invalid data format"

    updated_data = [tag for tag in tags if tag.get("id") != tag_id]

    if len(updated_data) == len(tags):
        return False, "Tag not found"

    write_json(file_path, updated_data)

    return True, "Tag deleted successfully"