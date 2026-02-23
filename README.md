# 🤟 Libras Sign Recognition API

API para reconhecimento de sinais do alfabeto em Libras utilizando Visão Computacional e Machine Learning.

O sistema captura a imagem da webcam, detecta a mão com MediaPipe, extrai os pontos da mão (landmarks) e utiliza um modelo treinado com Scikit-Learn para classificar a letra correspondente.  
O resultado é disponibilizado através de uma API REST construída com FastAPI.

---

## 📌 Arquitetura


Webcam
↓
OpenCV
↓
MediaPipe (Hand Tracking)
↓
Extração de Landmarks
↓
Modelo Machine Learning (Scikit-Learn)
↓
FastAPI
↓
Resposta JSON


---

## 🚀 Tecnologias Utilizadas

| Tecnologia      | Finalidade |
|---------------|------------|
| Python 3.10+  | Linguagem principal |
| OpenCV        | Captura de vídeo |
| MediaPipe     | Detecção e rastreamento das mãos |
| NumPy         | Manipulação de dados |
| Scikit-learn  | Treinamento do modelo |
| FastAPI       | Criação da API REST |
| Uvicorn       | Servidor ASGI |

---

## 📂 Estrutura do Projeto


libras-sign-recognition-api/
│
├── coletar_dados.py
├── treinar_modelo.py
├── api.py
├── main.py
├── requirements.txt
└── dados/ (criado manualmente)


---

## 🧠 Ambiente Virtual

Recomenda-se fortemente o uso de um ambiente virtual para:

- Isolar dependências
- Evitar conflitos com outros projetos
- Garantir que o projeto funcione corretamente em diferentes máquinas

---

## ⚙️ Instalação e Execução

### 1️⃣ Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd libras-sign-recognition-api
2️⃣ Criar e ativar ambiente virtual
Windows
python -m venv venv
venv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
3️⃣ Instalar dependências
pip install -r requirements.txt
📁 Preparação do Dataset

Antes de coletar dados, é necessário criar manualmente a pasta:

dados/

Dentro dela, crie uma subpasta para cada letra que deseja treinar:

dados/
   ├── A/
   ├── B/
   ├── C/
   └── D/

Cada subpasta representa uma classe do modelo.

📸 Coleta de Dados

Execute:

python coletar_dados.py

A webcam será ativada

Posicione a mão representando a letra desejada

Os dados serão salvos automaticamente na pasta correspondente

🧠 Treinamento do Modelo

Após coletar os dados:

python treinar_modelo.py

Esse processo irá:

Ler os dados da pasta dados/

Treinar o modelo de classificação

Gerar o arquivo modelo.pkl

🌐 Executando a API
uvicorn api:app --reload

A aplicação ficará disponível em:

http://127.0.0.1:8000

Documentação interativa:

http://127.0.0.1:8000/docs
📤 Exemplo de Resposta
{
  "letra": "D"
}
🎯 Objetivo do Projeto

Este projeto demonstra:

Aplicação prática de Visão Computacional

Treinamento e utilização de modelo de Machine Learning

Construção de API REST com FastAPI

Estruturação organizada de projeto backend

Possibilidade de integração com outras linguagens (ex: Java)

⚠️ Observações

É necessário possuir webcam funcional

Boa iluminação melhora a precisão

A qualidade do modelo depende da quantidade e variedade de dados coletados

🔮 Possíveis Evoluções

Expandir para todas as letras do alfabeto

Aumentar o dataset

Melhorar o modelo utilizando redes neurais

Criar interface web para visualização

Realizar deploy em ambiente de nuvem
