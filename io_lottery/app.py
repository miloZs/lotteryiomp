from flask import Flask, Response, request, jsonify

from io_lottery.controllers import add_user_controller,get_user_controller,update_user_controller,delete_user_controller
from io_lottery.repositories import UserRepository
from io_lottery.views import UserView

app = Flask(__name__)


@app.post("/users")
def add_user(user_data):
    add_user_controller.add(user_data)
    return Response(content=user_data, status_code=201)

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = get_user_controller.get(user_id)
    if user is None:
        return Response(status_code=404)
    return Response(content=user, status_code=200)

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_data):
    update_user_controller.update(user_id, updated_data)
    return Response(content=updated_data, status_code=200)

@app.patch("/users/{user_id}")
def partially_update_user(user_id: int, updated_data):
    update_user_controller.update(user_id, updated_data)
    return Response(content=updated_data, status_code=200)

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    delete_user_controller.delete(user_id)
    return Response(status_code=204)


app.add_url_rule("/users_new", view_func=UserView.as_view("users_new"))
