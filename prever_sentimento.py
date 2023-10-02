import pandas as pd
import numpy as np
import csv
import tensorflow

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

dataframe = pd.read_csv("./static/data_files/tweet_emotions.csv")

dataset = []

for i in range(len(dataframe)):
    frase = dataframe.loc[i, "content"]
    dataset.append(frase)


model = load_model("./static/model_files/Tweet_Emotion.h5")

tokenizer = Tokenizer(num_words= 40000, oov_token="<OOV>")
tokenizer.fit_on_texts(dataset)

emocaoUrl = {
    "vazio":        [0,  "./static/emoticons/vazio.png"],
    "tristeza":     [1,  "./static/emoticons/tristeza.png"],
    "entusiasmo":   [2,  "./static/emoticons/entusiasmo.png"],
    "neutro":       [3,  "./static/emoticons/neutro.png"],
    "preocupação":  [4,  "./static/emoticons/preocupação.png"],
    "surpresa":     [5,  "./static/emoticons/surpresa.png"],
    "amor":         [6,  "./static/emoticons/amor.png"],
    "diversão":     [7,  "./static/emoticons/diversão.png"],
    "ódio":         [8,  "./static/emoticons/ódio.png"],
    "felicidade":   [9,  "./static/emoticons/felicidade.png"],
    "tédio":        [10, "./static/emoticons/tédio.png"],
    "alívio":       [11, "./static/emoticons/alívio.png"],
    "raiva":        [12, "./static/emoticons/raiva.png"],
}


def predict(text):
    pEmocao = ''
    pImg = ''
    if text !='':
        frase = []
        frase.append(text)
        fraseNum = tokenizer.texts_to_sequences(frase)
        
        padded = pad_sequences(
            fraseNum, maxlen=100, padding='post', truncating='post'
        )

        padded = np.array(padded)

        label = np.argmax(model.predict(padded), axis=1)
        print(label)
        for key, value in emocaoUrl.items():
            if value[0]==label:
                pImg = value[1]
                pEmocao = key
        
        return pEmocao, pImg

#ler os dados do arquivo cvs e mostra
