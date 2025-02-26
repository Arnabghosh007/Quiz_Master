from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models.question import Question
from models.quiz import Quiz
from app import db
from controllers.admin import admin_required

question_bp = Blueprint('question', __name__)

@question_bp.route('/admin/quiz/<int:quiz_id>/questions')
@admin_required
def question_list(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    return render_template('admin/question_list.html', quiz=quiz)

@question_bp.route('/admin/quiz/<int:quiz_id>/question/add', methods=['GET', 'POST'])
@admin_required
def add_question(quiz_id):
    if request.method == 'POST':
        question = Question(
            quiz_id=quiz_id,
            question_text=request.form.get('question_text'),
            option1=request.form.get('option1'),
            option2=request.form.get('option2'),
            option3=request.form.get('option3'),
            option4=request.form.get('option4'),
            correct_option=int(request.form.get('correct_option'))
        )
        db.session.add(question)
        db.session.commit()
        flash('Question added successfully')
        return redirect(url_for('question.question_list', quiz_id=quiz_id))
    return render_template('admin/add_question.html', quiz_id=quiz_id)