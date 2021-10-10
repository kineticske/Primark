from flask import Flask, redirect, request
from flask import render_template
from flask import url_for
from flask import jsonify
from static.py.Usuarios import usuarios



app= Flask(__name__)



@app.route('/')

def index():
    return render_template('Index.html')

@app.route('/login')

def login():
    
    return render_template('Login.html')

@app.route('/signin')

def signin():
    return render_template('Signin.html')

@app.route('/favoritos')

def favoritos():
    return render_template('Favoritos.html')

@app.route('/productos')

def Productos():
    return render_template('Productos.html')

@app.route('/compras')

def compras():
    return render_template('Compras.html')


@app.route('/contactenos')

def contactenos():
    return render_template('Contactenos.html')

@app.route('/evaluar')

def evaluar():
    return render_template('Evaluar.html')

@app.route('/validarUsuario', methods=['POST'])

def validarUsuario():

    if (request.method=='POST'):
        correo=request.form['correo']
        contraseña=request.form['contraseña']
        users=None
        nombre=None
        error=False
        for users in usuarios:
            if(users['correo']==correo and users['contraseña']==contraseña):
                nombre=users['primer nombre']
                apellido=users['primer apellido']
                return render_template('index.html',nombre=nombre , apellido=apellido)
                
            error=True
            return render_template('login.html',error=error)



if __name__ == '__main__':
    app.run( port= 5000, debug=True)

