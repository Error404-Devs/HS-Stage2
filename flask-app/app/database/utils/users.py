import os
from app.database.utils.file_handler import read_json, write_json, append_json
from app.database.models.users import User


def get_all_users():
    file_path = os.path.join("app", "database", "storage", "users.json")
    return read_json(file_path)


def insert_user(user_id: str, username: str, password: str, role: str):
    file_path = os.path.join("app", "database", "storage", "users.json")

    existing_users = read_json(file_path)

    if any(user["id"] == user_id for user in existing_users):
        return None, {"error": f"Admin with ID {user_id} already exists."}

    try:
        new_user = User(
            id=user_id,
            username=username,
            password=password,
            role=role,
        )

        append_json(file_path, new_user.__dict__)

        return {"message": f"User with name {username} inserted successfully."}, None
    except Exception as e:
        return None, {"error": f"Error inserting user: {str(e)}"}


def update_user(user_id: int, updated_fields: dict):
    file_path = os.path.join("app", "database", "storage", "users.json")

    users = read_json(file_path)

    user = next((user for user in users if user['id'] == user_id), None)

    if user is None:
        return None, {"error": f"User with ID {user_id} not found."}

    try:
        updated_user_data = {**user, **updated_fields}
        valid_user = User.model_validate(updated_user_data)

        for field, value in updated_fields.items():
            user[field] = value

        write_json(file_path, users)

        return {"message": f"User with name {user_id} updated successfully."}, None
    except Exception as e:
        return None, {"error": f"Validation failed: {str(e)}"}


def delete_user(user_id):
    file_path = os.path.join("app", "database", "storage", "users.json")

    users = read_json(file_path)

    if not isinstance(users, list):
        return False, "Invalid data format"

    updated_data = [user for user in users if user.get("id") != user_id]

    if len(updated_data) == len(users):
        return False, "User not found"

    write_json(file_path, updated_data)

    return True, "User deleted successfully"