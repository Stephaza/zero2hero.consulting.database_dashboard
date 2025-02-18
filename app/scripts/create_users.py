users = {
    'user1': {
        'username': 'jasond',
        'password': 'password'
    },
    'user2': {
        'username': 'curator',
        'password': 'password'
    }
}

from app.models.user import User
from app.extensions import db

def create_users():
    for user in users:
        user = User.query.filter_by(username=users[user]['username']).first()
        if user:
            continue
        else:
            new_user = User(username=users[user]['username'], password=users[user]['password'])
            db.session.add(new_user)
            db.session.commit()