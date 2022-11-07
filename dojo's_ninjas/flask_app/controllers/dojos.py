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

@app.route('/addDojo', methods=['post'])
def addDojo():
    Dojo.save(request.form)
    return redirect('/')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id 
    }
    return render_template('dojo.html', dojo = Dojo.get_one_with_ninjas(data),  all_dojos = Dojo.get_all())

@app.route('/addNinja', methods=['post'])
def add_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/')