# Libras Sign Recognition API

API para reconhecimento de sinais do alfabeto em Libras utilizando Visão Computacional e Machine Learning.

O sistema captura a imagem da webcam, detecta a mão com MediaPipe, extrai os pontos da mão (landmarks) e utiliza um modelo treinado com Scikit-Learn para classificar a letra correspondente.  
O resultado é disponibilizado através de uma API REST construída com FastAPI.

---

## Arquitetura


Webcam
↓
OpenCV
↓
MediaPipe (Hand Tracking)
↓
Extração de Landmarks
↓
Modelo de Machine Learning (Scikit-Learn)
↓
FastAPI
↓
Resposta JSON


---

## Tecnologias Utilizadas

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

## Estrutura do Projeto


libras-sign-recognition-api/
│
├── coletar_dados.py
├── treinar_modelo.py
├── api.py
├── main.py
├── requirements.txt
└── dados/ (criado manualmente)


---

## Ambiente Virtual

Recomenda-se o uso de ambiente virtual para:

- Isolar dependências
- Evitar conflitos com outros projetos
- Garantir reprodutibilidade

### Criar ambiente virtual

#### Windows
" ```bash"
python -m venv venv
venv\Scripts\activate
Linux / macOS
python3 -m venv venv
source venv/bin/activate
Instalar dependências
pip install -r requirements.txt
Preparação do Dataset

Antes da coleta de dados, é necessário criar manualmente a pasta:

dados/

Dentro dela, crie uma subpasta para cada classe (letra) que deseja treinar:

dados/
   ├── A/
   ├── B/
   ├── C/
   └── D/

Cada subpasta representa uma classe do modelo de classificação.

Coleta de Dados

Execute:

python coletar_dados.py

Durante a execução:

A webcam será ativada.

Posicione a mão representando a letra desejada.

Os dados extraídos serão armazenados automaticamente na pasta correspondente.

A qualidade e diversidade dos dados coletados impactam diretamente a precisão do modelo.

Treinamento do Modelo

Após coletar os dados necessários:

python treinar_modelo.py

Esse processo irá:

Ler os dados da pasta dados/

Treinar o modelo de classificação

Gerar o arquivo modelo.pkl

Execução da API

Inicie o servidor com:

uvicorn api:app --reload

A aplicação ficará disponível em:

http://127.0.0.1:8000

Documentação interativa da API (Swagger):

http://127.0.0.1:8000/docs
Exemplo de Resposta
{
  "letra": "D"
}
Objetivo do Projeto

Este projeto demonstra:

Aplicação prática de Visão Computacional

Treinamento e inferência de modelo de Machine Learning

Construção de API REST com FastAPI

Estruturação modular de backend

Integração possível com aplicações externas (ex: cliente Java)

Observações

É necessário possuir webcam funcional.

Boa iluminação melhora significativamente a precisão.

O desempenho do modelo depende da quantidade e qualidade dos dados coletados.

Possíveis Evoluções

Expansão para todas as letras do alfabeto

Ampliação do dataset

Utilização de redes neurais para maior robustez

Desenvolvimento de interface web

Deploy em ambiente de nuvem
