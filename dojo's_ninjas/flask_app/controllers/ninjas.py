from flask_app import app
from flask import render_template,redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template('dojos.html', all_dojos = dojos)
    
@app.route('/ninjas')
def ninjaList():
    ninjas = Ninja.get_all()
    return render_template('ninjas.html', all_ninjas = ninjas)

@app.route('/addNinja')
def add_ninja():
    Ninja.save(request.form)
    return redirect('/')