from app import db
from models.user import User

def init_db():
    """Initialize the database and create admin user if not exists."""
    db.create_all()
    create_admin_if_not_exists()

def create_admin_if_not_exists():
    """Create admin user if it doesn't exist."""
    admin = User.query.filter_by(is_admin=True).first()
    if not admin:
        admin = User(
            username='admin@example.com',
            full_name='Admin User',
            is_admin=True
        )
        admin.set_password('admin123')
        db.session.add(admin)
        db.session.commit()