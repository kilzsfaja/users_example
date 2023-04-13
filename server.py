from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("create.html")

# @app.route("/")
# def index():
#     users = User.get_all()
#     print(users)
#     return render_template("read.html", all_users = users)

@app.route('/read', methods=['GET'])
def show():
    users = User.get_all()
    return render_template("read.html", all_users = users)

@app.route('/create/user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/read')

# @app.route("/users/read/form/<int:id>", methods=["GET"])
# def display_read(id):
#     data = {
#         "user_id": id
#     }
#     current_user = User.get_one(data)
#     return render_template("read.html", current_user = current_user)

if __name__ == "__main__":
    app.run(debug=True)

# **********************

#   Method: GET
#   grabbing everything in a list
#   URL: make it plural ex: "/todos"
#   Function: get_all_todos()
#             get_todos()

#   Method: GET
#   grabbing ONE of a particular list
#   URL: "/todo/<int:id>"
#        "/user/<int:id>"
#   Function: get_todo_by_id(id)
#             get_todo(id)

#   Method: GET
#   Displaying a form that will eventually refer to a list
#   URL: "/todo/form"
#   Function: display_todo_form()

#   Method: POST
#   Create a new item of a list
#   URL: "/todo/add"
#        "/todo/new"
#   Function: create_todo_list()
#             add_todo()
#             new_todo()

#   Method: POST-PUT
#   Updating an existing item of a list
#   URL: "/todo/update/<int:id>"
#        "/todo/edit/<int:id>"
#   Function: update_todo(id)
#             edit_todo(id)

#   Method: POST - DELETE
#   Deleting an existing item of a list
#   URL: "/todo/remove/<int:id>"
#        "/todo/delete/<int:id>"
#   Function: remove_todo(id)
#             delete_todo(id)

# **********************