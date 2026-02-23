import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

X = []
y = []

#Caminha pelas pastas
for letra in os.listdir("dados"):
    pasta = os.path.join("dados", letra)

    for arquivo in os.listdir(pasta):
        caminho = os.path.join(pasta, arquivo)
        dados = np.load(caminho)

        X.append(dados)
        y.append(letra)

#Treinar modelo
modelo = RandomForestClassifier()
modelo.fit(X, y)

#Salvar modelo
with open("modelo.pkl", "wb") as f:
    pickle.dump(modelo, f)

print("Modelo treinado e salvo.")