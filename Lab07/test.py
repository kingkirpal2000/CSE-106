from api import db, User

s1 = User(name = "John", grade=99)

db.session.add(s1)

db.session.commit()