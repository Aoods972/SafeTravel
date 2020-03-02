from SafeTravel import db, login_manager, app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	__tablename__ = 'SF_users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"User('{self.name}', '{self.email}')"

class Emergency(db. Model):
	__tablename__ = 'SF_emergencies'
	id = db.Column(db.Integer, primary_key=True)
	userID = db.Column(db.Integer, nullable=False)
	time = db.Column(db.String(255), nullable=False)
	lat = db.Column(db.Float, nullable=False)
	lng = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Emergency, userID: ('{self.userID}', emergency id: '{self.id}')"

