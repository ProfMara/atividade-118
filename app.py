from flask import Flask, render_template, request, jsonify
from prever_sentimento import *
app = Flask(__name__)

@app.route("/")

def index():
    #recebendo as entradas

    #passando as entradas para o index.html
    return render_template("index.html")



@app.route("/prever-emocao", methods=['POST'])

def verEmocao():
    text = request.json.get("texto")

    if not text:
        response = {
            "status":"error",
            "message":"Digite um texto ver a emoção"
        }
        return jsonify(response)
    else:
        emocao, emocaoImg = predict(text)
        response = {
            "status":"success",
            "data":{
                "emocao":emocao,
                "emocaoImg": emocaoImg
            }
        }
        return jsonify(response)

#adiciona uma nova rota



app.run(debug=True)


