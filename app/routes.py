from app import app # type: ignore
from flask import (Flask, render_template, redirect) # type: ignore
# import form class
from app.forms.sample_form import SampleForm # type: ignore
from app.forms.login_form import LoginForm  # type: ignore

@app.route('/')
def index():    
    return render_template('page.html', title = 'Welcome')

@app.route('/help')
def help():        
    return render_template('page.html', title = 'Help')



@app.route('/item/<int:id>')
def item(id):        
    if (id > 0 and id < 100):
        item = {
            "id": id,
            "name": f"Fancy Item {id}",
            "description": "Coming soon!",
        }
        return render_template('item.html', title = 'Item', item = item)
    else:
        return render_template('error.html', title = 'Error', message = 'Item not found. Expected between 1 and 99')

# Forms:
@app.route('/login', methods=['GET', 'POST'])
def login():  
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/') # Submit complete      
    return render_template('login.html', title = 'Login', form = form)

@app.route('/form', methods=['GET', 'POST'])
def form():
    # instantiate form
    form = SampleForm()
    if form.validate_on_submit():
        return 'll'# redirect('/') # Submit complete  
    # send form into Jinja template (with form=form)
    return render_template('form.html', title = 'Sample Form', form = form)

   