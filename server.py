from flask import Flask, render_template, request, redirect, url_for
from users_model import User

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/users_all")

# ------------- DISPLAY ALL USERS -------------
@app.route('/users_all', methods=['GET'])
def users():
    users = User.get_all()
    return render_template("users_all.html", all_users = users)

# -------------- CREATE USER (render) --------------
@app.route('/users/new')
def new_user():
    return render_template("create_user.html")

# --------------- CREATE USER (action) -----------------
@app.route('/users/create', methods=["POST"])
def create_user():
    data = {
        **request.form
    }
    user_id = User.save(data)
    return redirect(url_for('show_user', id = user_id))
# why did URL FOR work for this but not for UPDATE route? Other ways??

# ----------------- DISPLAY ONE USER ------------------
@app.route('/users/show/<int:id>')
def show_user(id):
    user = User.get_one(id)
    return render_template("show_user.html", user = user)

# ------------------- EDIT USER (render) --------------------
@app.route('/users/edit/<int:id>')
def edit_user(id):
    user = User.get_one(id)
    return render_template("edit_user.html", user = user)

# ----------------- EDIT USER (action) -----------------
@app.route('/users/update/<int:id>', methods=["POST"])
def update_user(id):
    data = {
        **request.form,
        "id" : id
    }
    User.edit_user(data)
    return redirect('/')
    # return redirect(url_for('show_user', id = id))

# ------------------- DELETE USER ------------------------
@app.route('/users/delete/<int:id>')
def delete(id):
    User.delete(id)
    return redirect('/')

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