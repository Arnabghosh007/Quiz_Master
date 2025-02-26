from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Change this to a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

# Import blueprints after db initialization
from controllers.auth import auth_bp
from controllers.admin import admin_bp
from controllers.user import user_bp
from controllers.quiz import quiz_bp
from controllers.question import question_bp

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)
app.register_blueprint(quiz_bp)
app.register_blueprint(question_bp)

# Create admin user when database is initialized
def create_admin():
    from models.user import User
    admin = User.query.filter_by(is_admin=True).first()
    if not admin:
        admin = User(
            username='admin@example.com',
            full_name='Admin User',
            is_admin=True
        )
        admin.set_password('admin123')  # Change this password
        db.session.add(admin)
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_admin()
    app.run(debug=True)
