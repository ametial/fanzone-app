import Flask

app = Flask(__name__)

if __name__ == '__main__':
  #to run the Server in terminal > flask run -h localhost -p 5000
  app.run()

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fanzone.db"
# initialize the app with the extension
db.init_app(app)

@app.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    #return render_template("user/list.html", users=users)

@app.route("/users", methods=["POST"])
def user_create(request: Request):
  if request.method == "POST":
      user = User(
        username=request.form["username"],
        email=request.form["email"],
        )
      db.session.add(user)
      db.session.commit()
      return Response(response={"message": "OK"} status=201)
    
      return redirect(url_for("user_detail", id=user.id))

    return render_template("user/create.html")

@app.route("/user/<int:user_id>", methods=["GET"])
def user_detail(user_id: int):
    user = db.get_or_404(User, id)
   return Response(response={"user": user}, status=200)
  #return render_template("user/detail.html", user=user)

@app.route("/user/<int:user_id>", methods=["PUT"])
def user_update(user_id: int, request: Request:):
  user = db.get_or_404(User, id)
  if user:
    user.email = request.form["email"]
    user.username = request.form["username"]
    db.session.add(user)
    db.session.commit()


    #return render_template("user/detail.html", user=user)

@app.route("/user/<int:id>", methods=["DELETE"])
def user_delete(id):
    user = db.get_or_404(User, id)

    if request.method == "POST":
      db.session.delete(user)
      db.session.commit()
      return redirect(url_for("user_list"))

    #return render_template("user/delete.html", user=user)
