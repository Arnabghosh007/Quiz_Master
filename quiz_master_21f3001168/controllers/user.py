from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.quiz import Quiz
from models.score import Score

user_bp = Blueprint('user', __name__)

@user_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_admin:
        return redirect(url_for('admin.dashboard'))
        
    available_quizzes = Quiz.query.all()
    user_scores = Score.query.filter_by(user_id=current_user.id).all()
    return render_template('user/dashboard.html', 
                         quizzes=available_quizzes,
                         scores=user_scores)