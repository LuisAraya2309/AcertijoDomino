#Libraries
from flask import Flask,render_template,request
from dominoes import *
app = Flask(__name__)


#Routes
@app.route('/',methods=['GET'])
def principal():
    return render_template('index.html')

@app.route('/eleccion',methods=['POST','GET'])
def solucion():
    algoritmo = request.form['algoritmo']
    set = int(request.form['set'])
    matriz = generarMatriz(set)

    if algoritmo == 'backtracking':
        return render_template('backtracking.html',set = set,matriz = matriz)

    return render_template('fuerzaBruta.html',set = set,matriz = matriz)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True)

   