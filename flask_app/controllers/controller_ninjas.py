from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models import model_ninjas, model_dojos

# ******************** DISPLAY ROUTES ********************

@app.route('/dojos/<int:id>')
def get_all_ninjas(id):
    ninjas = model_ninjas.Ninja.get_all_ninjas(id = id)
    dojo = model_dojos.Dojo.get_one(id = id)
    return render_template('ninjas_show.html', all_ninjas=ninjas, dojo = dojo)

@app.route('/ninjas')
def add_ninja():
    all_dojos = model_dojos.Dojo.get_all_dojos()
    return render_template('new_ninjas.html', all_dojos = all_dojos)

# ******************** ACTION ROUTES ********************

@app.route('/ninjas/create', methods = ["POST"])
def create_ninja():
    print(request.form)
    ninja_data = {
        "dojo_id": request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]
    }
    model_ninjas.Ninja.create(ninja_data)
    return redirect(f'/dojos/{request.form["dojo_id"]}')