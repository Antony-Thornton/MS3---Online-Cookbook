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
    tooldb = list(mongo.db.Tools.find())
    ratingdb = list(mongo.db.ratings.find())
    return render_template(
        "tools.html", tooldb=tooldb, ratingdb=ratingdb)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    info = list(mongo.db.RecipeInfo.find({"$text": {"$search": query}}))
    return render_template("community.html", info=info)


@app.route("/search_recipes", methods=["GET", "POST"])
def search_recipes():
    query = request.form.get("query")
    info = list(mongo.db.RecipeInfo.find({"$text": {"$search": query}}))
    # print(info)
    # print("issue")
    return render_template("recipes.html", info=info)


@app.route("/recipes", methods=["GET", "POST"])
def recipes():
    info = list(mongo.db.RecipeInfo.find(
        {"created_by": session["user"].lower()}).sort('category'))
    # info = [x for x in info if x['created_by'].lower() == session['user'].
    # lower()]
    print(info)

    categories = {}
    distinct_categories = list(mongo.db.RecipeInfo.distinct("category"))

    for category in distinct_categories:
        recipes = list(mongo.db.RecipeInfo.find({"category": category}))
        categories[category] = recipes

    return render_template(
        "recipes.html", info=info, categories=categories, recipes=recipes)


@app.route("/community")
def community():
    info = list(mongo.db.RecipeInfo.find())
    return render_template("community.html", info=info)


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

    return render_template(
        "profile.html", username=username, user=user, info=info)
    return redirect(url_for("login"))


@app.route("/recipe_page/<username>", methods=["GET", "POST"])
def recipe_page(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    categories = []

    if session["user"]:
        user = list(mongo.db.users.find())
        info = list(mongo.db.RecipeInfo.find())
        categories = list(mongo.db.RecipeInfo.distinct("category"))
        print(categories)

    return render_template(
        "recipes.html", username=username, user=user,
        info=info, categories=categories)
    # return redirect(url_for("login"))


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
    # need to define this. What is objectID aimed at{
    # "recipe_name": ObjectId("recipe_name")}
    mongo.db.RecipeInfo.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for(
        "profile", username=session["user"]))


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        print('post')
        veg = "Vegetarian" if request.form.get("veg") else "No"
        vegan = "Vegan" if request.form.get("vegan") else "No"
        community_friendly = "No" if request.form.get(
            "comm_friendly") else "Yes"
        community_name_show = "No" if request.form.get(
            "comm_name_show") else "Yes"

        form = request.form.to_dict()
        print(form)
        mongo.db.RecipeInfo.find_one({"recipe_name": form["recipe_name"]})
        recipe_update = {
                    "recipe_name": request.form.get("recipe_name"),
                    "feeds": request.form.get("feeds"),
                    "veg": veg,
                    "vegan": vegan,
                    "created_by": session["user"],
                    "cooking": request.form.get("cooking"),
                    "comm_friendly": community_friendly,
                    "ingredients": request.form.get("ingredients"),
                    "picpath": request.form.get("picpath"),
                    "comm_name_show": community_name_show,
                    "recipe_url": request.form.get("recipe_url"),
                    "category": request.form.get("category"),
                        }
        print(recipe_update)
        mongo.db.RecipeInfo.update_one(
            {"recipe_name": form["recipe_name"]}, {"$set": recipe_update})
        flash("Recipe Successfully Updated")
        return redirect(url_for(
            "profile", username=session["user"]))
    print('skipping post')
    return redirect(url_for(
            "profile", username=session["user"]))


@app.route("/submit_recipe", methods=["GET", "POST"])
def submit_recipe():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        user = list(mongo.db.users.find())
        info = list(mongo.db.RecipeInfo.find())

    if request.method == "POST":
        veg = "Vegetarian" if request.form.get(
                "veg") else "No"
        vegan = "Vegan" if request.form.get(
                "vegan") else "No"
        community_friendly = "No" if request.form.get(
            "comm_friendly") else "Yes"
        community_name_show = "Yes" if request.form.get(
            "comm_name_show") else "No"

        form = request.form.to_dict()
        print(form)
        # search for a recipe with the recipe
        # name
        search = mongo.db.RecipeInfo.find_one(
            {"recipe_name": form["recipe_name"]})

        # if their is no recipe with that recipe_name on the form,
        # then None will be returned. So...
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
                "ingredients": request.form.get("ingredients"),
                "picpath": request.form.get("picpath"),
                "comm_name_show": community_name_show,
                "recipe_url": request.form.get("recipe_url"),
                "category": request.form.get("category"),
            }
            mongo.db.RecipeInfo.insert_one(recipe_add)
            flash("Recipe successfully added")
        return render_template(
            "profile.html", username=username, user=user, info=info
        )
    else:
        flash("Duplicate recipe. Please change name and try again.")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
