from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models import model_dojos


# ******************** DISPLAY ROUTES ********************

@app.route('/dojos')
def get_all_dojos():
    dojos = model_dojos.Dojo.get_all_dojos()
    return render_template('dojos_show.html', all_dojos=dojos)

@app.route('/dojos/add_new')
def add_dojo():
    return render_template('dojos_show.html')

# ******************** ACTION ROUTES ********************

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    print('dojos')
    dojo_data = {
        "name": request.form['name'],
    }
    model_dojos.Dojo.add_dojo(dojo_data)
    return redirect('/dojos')
