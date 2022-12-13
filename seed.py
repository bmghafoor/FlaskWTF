from app import app
from models import Pet, db


with app.app_context():
    db.drop_all()
    db.create_all()

    Pet.query.delete()

    dog = Pet(name="Rocky Boy", species="dog", age = 4, available = True)
    db.session.add(dog)
    db.session.commit()