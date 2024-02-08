import Flask

app = Flask(__name__)

if __name__ == '__main__':
  #to run the Server in terminal > flask run -h localhost -p 5000
  app.run()

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fanzone.db"
# initialize the app with the extension
db.init_app(app)

