from pydantic import BaseModel
from typing import List

class ApiInput(BaseModel):
    text: List[str]

class ApiOutput(BaseModel):
    is_hate: List[int]

app = FastAPI() # creamos el api
model = joblib.load("model.joblib") # cargamos el modelo.

@app.post("/hate") # creamos api que permita requests de tipo post.
async def define_sentiment(data: ApiInput) -> ApiOutput:
    predictions = model.predict(data.texts).flatten().tolist() # generamos la predicción
    preds = ApiOutput(is_hate=predictions) # estructuramos la salida del API.
    return preds # retornamos los resultados

# Crear repositorio
!mkdir mlapi
!mv main.py model.joblib mlapi/
%cd mlapi/

# Inicia el repositorio
!git config --global user.email "wlpuertasb@unal.edu.co"
!git config --global user.name "LeonardoPuertas"
!git config --global init.defaultBranch master
!git init

# Requerimientos
%%writefile requirements.txt
pandas: 2.0.3
tensorflow: 2.15.0
keras: 2.15.0
os: no tiene versión ya que es un módulo de Python incorporado
re: no tiene versión ya que es un módulo de Python incorporado
numpy: 1.25.2
matplotlib: 3.7.1
sklearn: 1.2.2
mlflow: 3.7.1
mlflow.sklearn: 1.2.2


%%writefile railway.json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "uvicorn main:app --host 0.0.0.0 --port $PORT",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}

##
!git add railway.json requirements.txt main.py model.joblib
!git commit -m "Agregamos los archivos del API."

token = "2gFhe2SWcQgNt73UPJ7nBlm2EJw_3eQELDPvsE85c62pA6Fxk"  # Agregue su token dentro de las comillas.
repo_url = "https://github.com/cdtafurd/mlds6_project/edit/master/docs/deployment/deploymentdoc.md" # Agregue la url de su repositorio dentro de las comillas.

import re
pat = re.compile(r"(https://)(.*)")

# Formatear la URL
import os
match = re.match(pat, repo_url)
url_token = "".join([match.group(1), token, "@", match.group(2)])
os.environ["GITHUB"] = url_token

!git remote add origin $GITHUB

!git push origin master

model_url = "https://mlapi-production-272c.up.railway.app" 