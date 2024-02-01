"""Create initial database tables"""

from app import db
from models import Hobbies, Interests

db.drop_all()
db.create_all()

db.session.commit()

#######################################
# add interests

basketball = Interests(code="bball", name="Basketball")
golf = Interests(code="golf", name="Golf")

db.session.add_all([basketball, golf])
db.session.commit()

#######################################
# add hobbies

tabletop= Hobbies(code="tabletop", name="tabletop")
skydiving= Hobbies(code="skydiving", name="skydiving")

db.session.add_all([tabletop, skydiving])
db.session.commit()