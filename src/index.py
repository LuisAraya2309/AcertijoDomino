#Libraries
from flask import Flask

app = Flask(__name__)


#Routes
@app.route('/',methods=['GET'])
def principal():
    return "Bienvenido a la pagina web"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True)

   