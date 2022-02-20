import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
# Check at the end of the project if this next line can be deleted.
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def get_tasks():
    return render_template("home.html")


@app.route("/tools")
def tools():
    test = list(mongo.db.Test.find())
    tooldb = list(mongo.db.Tools.find())
    return render_template("tools.html", test=test, tooldb=tooldb)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    tasks = list(mongo.db.RecipeInfo.find({"$text": {"$search": query}}))
    return render_template("community.html", tasks=tasks)


@app.route("/search_recipes", methods=["GET", "POST"])
def search_recipes():
    query = request.form.get("query")
    tasks = list(mongo.db.RecipeInfo.find({"$text": {"$search": query}}))
    return render_template("profile.html", tasks=tasks)


@app.route("/community")
def community():
    info = list(mongo.db.RecipeInfo.find())
    test = list(mongo.db.Test.find())
    return render_template("community.html", info=info,  test=test)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        registration = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower()
        }
        mongo.db.users.insert_one(registration)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                        request.form.get("username")))
                return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        user = list(mongo.db.users.find())
        info = list(mongo.db.RecipeInfo.find())

    if request.method == "POST":
        veg = "N" if request.form.get("veg") else "Y"
        vegan = "N" if request.form.get("vegan") else "Y"
        community_friendly = "N" if request.form.get("comm_friendly") else "Y"

        form = request.form.to_dict()
        print(form)
        # search for a recipe with the recipe name 
        search = mongo.db.RecipeInfo.find_one(
            {"recipe_name": form["recipe_name"]})
       
        # if their is no recipe with that recipe_name on the form, then None
        # will be returned. So...
        if not search:
            # insert the recipe
            recipe_add = {
                        "recipe_name": request.form.get("recipe_name"),
                        "feeds": request.form.get("feeds"),
                        "veg": veg,
                        "vegan": vegan,
                        "created_by": session["user"],
                        "cooking": request.form.get("cooking"),  
                        "comm_friendly": community_friendly,       
                }
            mongo.db.RecipeInfo.insert_one(recipe_add)
            flash("Task successfully added")
            return render_template(
                "profile.html", username=username, user=user, info=info)

        else:     
            flash("Duplicate recipe. Please change name and try again.")

    return render_template(
        "profile.html", username=username, user=user, info=info)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# App route can be linked to an A by using URL_for in html. 
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # Mongo db link - mongo.db.RecipeInfo.remove()
    # need to define this. What is objectID aimed at{"recipe_name": ObjectId("recipe_name")} 
    mongo.db.RecipeInfo.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for(
        "profile", username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
