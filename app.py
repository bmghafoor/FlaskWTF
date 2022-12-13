from flask import Flask, render_template, flash, redirect, render_template, request
from models import db, connect_db, Pet
from forms import PetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///flask_wtforms"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

connect_db(app)

@app.route("/")
def homepage():
    """Show Pets"""

    pets = Pet.query.all()

    return render_template('homepage.html',pets=pets)

@app.route("/add", methods = ['GET','POST'])
def add():
    """Show page to add pets."""
    form = PetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')

    else:
        return render_template("add.html", form=form)

@app.route('/pet/<int:id>')

def show_pet(id):
    """Show info on a pet"""
    pet = Pet.query.get_or_404(id)

    return render_template('pet.html', pet = pet)


@app.route("/pet/<int:id>/edit", methods=["GET", "POST"])
def edit_pet(id):
    """Edit pet."""

    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        return redirect('/')

    else:
        
        return render_template("edit.html", form=form, pet=pet)
