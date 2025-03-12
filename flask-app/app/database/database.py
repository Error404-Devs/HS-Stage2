from app.database.utils.users import *
from app.database.utils.tags import *


class Database:
    # User-related methods
    @staticmethod
    def get_all_users():
        return get_all_users()

    @staticmethod
    def insert_user(user_id, username, password, role):
        return insert_user(user_id=user_id, username=username, password=password, role=role)

    @staticmethod
    def update_user(user_id: int, updated_fields: dict):
        return update_user(user_id=user_id, updated_fields=updated_fields)

    @staticmethod
    def delete_user(user_id: int):
        return delete_user(user_id=user_id)
    
    # Tag-related methods
    @staticmethod
    def get_all_tags():
        return get_all_tags()

    @staticmethod
    def insert_tag(tag_id, name, user):
        return insert_tag(tag_id=tag_id, name=name, user=user)

    @staticmethod
    def update_tag(tag_id: str, updated_fields: dict):
        return update_tag(tag_id=tag_id, updated_fields=updated_fields)

    @staticmethod
    def delete_tag(tag_id: str):
        return delete_tag(tag_id=tag_id)


db = Database()
