from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from send_mail import db, app


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def get_reset_token(self, expire_time=120):
        serial_key = Serializer(app.config['SECRET_KEY'], expire_time)
        return serial_key.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        serial_key = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = serial_key.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"
