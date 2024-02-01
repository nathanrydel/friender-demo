"""Create initial database tables"""

from app import db
from models import User, Hobby, Interest

db.drop_all()
db.create_all()

db.session.commit()


#######################################
# add users
# all users have password of password

u1 = User.signup("test", "test@example.com", "password",
                 "94304", "8005551234", "test_fname", "test_lname")

u2 = User.signup("mctest2", "test2@example.com", "password",
                 "94022", "8005552345", "mctest_fname", "mctest_lname")

db.session.add_all([u1, u2])
db.session.commit()

#######################################
# add interests

basketball = Interest(code="basketball", name="Basketball")
golf = Interest(code="golf", name="Golf")
rockclimbing = Interest(code="rock-climbing", name="Rock Climbing")
skiing = Interest(code="skiing", name="Skiing")

db.session.add_all([basketball, golf, rockclimbing, skiing])
db.session.commit()

#######################################
# add hobbies

tabletop = Hobby(code="table-top-rpgs", name="Table Top RPGs")
skydiving = Hobby(code="sky-diving", name="Sky Diving")

db.session.add_all([tabletop, skydiving])
db.session.commit()
