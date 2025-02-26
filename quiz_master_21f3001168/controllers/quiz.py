from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models.quiz import Quiz
from models.score import Score
from datetime import datetime
from app import db

quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/admin/chapter/<int:chapter_id>/quiz/add', methods=['GET', 'POST'])
@login_required
def add_quiz(chapter_id):
    if request.method == 'POST':
        quiz = Quiz(
            title=request.form.get('title'),
            chapter_id=chapter_id,
            date_of_quiz=datetime.strptime(request.form.get('date'), '%Y-%m-%d'),
            duration_minutes=int(request.form.get('duration'))
        )
        db.session.add(quiz)
        db.session.commit()
        flash('Quiz created successfully')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/quiz_manage.html', chapter_id=chapter_id)

@quiz_bp.route('/quiz/<int:quiz_id>/take')
@login_required
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    return render_template('user/take_quiz.html', quiz=quiz)

@quiz_bp.route('/quiz/<int:quiz_id>/submit', methods=['POST'])
@login_required
def submit_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    score = 0
    
    for question in quiz.questions:
        user_answer = request.form.get(f'question_{question.id}')
        if user_answer and int(user_answer) == question.correct_option:
            score += 1
            
    percentage = (score / len(quiz.questions)) * 100 if quiz.questions else 0
    quiz_score = Score(
        quiz_id=quiz_id,
        user_id=current_user.id,
        score=percentage
    )
    db.session.add(quiz_score)
    db.session.commit()
    flash(f'Quiz submitted successfully. Your score: {percentage:.2f}%')
    return redirect(url_for('user.dashboard'))