#Librerias
from flask import Flask,render_template,request
from dominoes import *
from algoritmos import *

#Creacion de la app
app = Flask(__name__)
matriz = []
#Rutas
@app.route('/',methods=['GET'])
def principal():
    return render_template('index.html')


@app.route('/fuerzaBruta',methods=['POST','GET'])
def solucionFB():
    global matriz
    set = int(request.form['set'])
    matriz = generarMatriz(set)
    return fuerzaBrutaG(matriz)

@app.route('/backtracking',methods=['POST','GET'])
def solucionBT():
    return backtrackingG(matriz)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True)

   