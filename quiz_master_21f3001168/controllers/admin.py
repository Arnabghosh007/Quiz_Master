from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models.subject import Subject
from models.chapter import Chapter
from models.quiz import Quiz
from models.user import User
from app import db

admin_bp = Blueprint('admin', __name__)

def admin_required(f):
    @login_required
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            flash('Access denied')
            return redirect(url_for('user.dashboard'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/admin/dashboard')
@admin_required
def dashboard():
    subjects = Subject.query.all()
    users = User.query.filter_by(is_admin=False).all()
    return render_template('admin/dashboard.html', subjects=subjects, users=users)

@admin_bp.route('/admin/subject', methods=['GET', 'POST'])
@admin_required
def manage_subject():
    if request.method == 'POST':
        subject = Subject(
            name=request.form.get('name'),
            description=request.form.get('description')
        )
        db.session.add(subject)
        db.session.commit()
        flash('Subject created successfully')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/subject_manage.html')

@admin_bp.route('/admin/chapter/<int:subject_id>', methods=['GET', 'POST'])
@admin_required
def manage_chapter(subject_id):
    subject = Subject.query.get_or_404(subject_id)
    if request.method == 'POST':
        chapter = Chapter(
            name=request.form.get('name'),
            description=request.form.get('description'),
            subject_id=subject_id
        )
        db.session.add(chapter)
        db.session.commit()
        flash('Chapter created successfully')
        return redirect(url_for('admin.dashboard'))
    return render_template('admin/chapter_manage.html', subject=subject)