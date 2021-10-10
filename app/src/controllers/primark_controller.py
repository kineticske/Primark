from flask import render_template, redirect, url_for, request, abort
from static.py.Usuarios import usuarios

def index():
    return render_template('index.html')

def login():    
    return render_template('login.html')

def signin():
    return render_template('signin.html')

def favoritos():
    return render_template('favoritos.html')

def productos():
    return render_template('productos.html')

def compras():
    return render_template('compras.html')

def contactenos():
    return render_template('contactenos.html')

def evaluar():
    return render_template('evaluar.html')


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
                return render_template('User.html',nombre=nombre , apellido=apellido)
            error=True
            return render_template('login.html',error=error)