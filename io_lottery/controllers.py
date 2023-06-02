from dataclasses import dataclass

from io_lottery.repositories import UserRepository
import uuid


class add_user_controller:
    def add(self, user_data):
        class AddUserController:
            def add(self, user_data):
                if not self._validate_user_data(user_data):
                    raise ValueError("Invalid user data")
                
            def generate_unique_id():       
                unique_id = uuid.uuid4()
                return int(unique_id) 

            new_user = {
                "id": generate_unique_id(), 
                "name": user_data["name"],
                "email": user_data["email"],
            }

            db.add_user(new_user)
        return new_user

    def _validate_user_data(self, user_data):
        if "name" not in user_data or "email" not in user_data:
            return False
        return True

class get_user_controller:
    def get(self, user_id):
        class GetUserController:
            def get(self, user_id):
        
                if not self._validate_user_id(user_id):
                    raise ValueError("Invalid user ID")

        user = db.get_user_by_id(user_id)  

        if user is None:
            return None  

        
        return user

    def _validate_user_id(self, user_id):
        return isinstance(user_id, int)


class update_user_controller:
    def update(self, user_id, updated_data):
        class UpdateUserController:
            def update(self, user_id, updated_data):        
                if not self._validate_user_id(user_id):
                    raise ValueError("Invalid user ID")

        if not self._validate_user_data(updated_data):
            raise ValueError("Invalid user data")
        user = db.get_user_by_id(user_id)  
        if user is None:
            return None 

        user["name"] = updated_data["name"]
        user["email"] = updated_data["email"]
        db.update_user(user) 
        return user

    def _validate_user_id(self, user_id):
        return isinstance(user_id, int)

    def _validate_user_data(self, user_data):
        if "name" not in user_data or "email" not in user_data:
            return False
        return True

class delete_user_ontroller:
    def delete(self, user_id):
        class DeleteUserController:
            def delete(self, user_id):
                if not self._validate_user_id(user_id):
                    raise ValueError("Invalid user ID")

        if not self._user_exists(user_id):
            return None  

        db.delete_user(user_id)

        return {"message": "User deleted successfully"}

    def _validate_user_id(self, user_id):
        return isinstance(user_id, int)

    def _user_exists(self, user_id):
        user = db.get_user_by_id(user_id)
        return user is not None

