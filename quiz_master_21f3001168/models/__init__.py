from app import db
from models.user import User
from models.subject import Subject
from models.chapter import Chapter
from models.quiz import Quiz
from models.question import Question
from models.score import Score

# This allows easier imports from models package
__all__ = ['User', 'Subject', 'Chapter', 'Quiz', 'Question', 'Score']