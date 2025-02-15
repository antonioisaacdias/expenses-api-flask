from flask import Flask
from flask_migrate import Migrate
from database import db
from config import Config
from routes import bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)