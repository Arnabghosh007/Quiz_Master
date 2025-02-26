from datetime import datetime

def validate_quiz_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        return date_obj >= datetime.now().date()
    except ValueError:
        return False

def validate_time_duration(duration_str):
    try:
        hours, minutes = map(int, duration_str.split(':'))
        return 0 <= hours <= 23 and 0 <= minutes <= 59
    except (ValueError, TypeError):
        return False

def validate_email(email):
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_password(password):
    return len(password) >= 6

def validate_date_of_birth(dob_str):
    try:
        dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
        today = datetime.now().date()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return 10 <= age <= 100
    except ValueError:
        return False