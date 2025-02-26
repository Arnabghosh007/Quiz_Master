from controllers.auth import auth_bp
from controllers.admin import admin_bp
from controllers.user import user_bp
from controllers.quiz import quiz_bp
from controllers.question import question_bp

# This allows easier imports from controllers package
__all__ = ['auth_bp', 'admin_bp', 'user_bp', 'quiz_bp', 'question_bp']