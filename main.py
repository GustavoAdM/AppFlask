from flask import Flask, render_template, request, redirect, session
from ext.db.database import buscardados, infoUser
from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'ab12AB12abc12ABC12@'
app.permanent_session_lifetime = timedelta(seconds=180)
# -------------------Rotas Principais-----------------


@app.route('/')
def index():
    return render_template('paginalogin.html')


@app.route('/user')
def dashboard():
    if 'email' in session:
        return render_template('dashboard.html', usuario=infoUser(session['email']))
    else:
        return redirect('/')

# --------------------Rotas Secundarias---------------


@app.route('/', methods=['POST', 'GET'])
def index_post():
    if request.method == 'POST':
        email = request.form.get('email')
        pasw = request.form.get('senha')
        if buscardados(email, pasw):
            session['email'] = email
            session.permanent = True
            return redirect('/user')
        else:
            return render_template('paginalogin.html', erro='active')



@app.route('/user', methods=['POST', 'GET'])
def dashboard_post():
    return render_template('dashboard.html', usuario=infoUser(session['email']))



@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
    
