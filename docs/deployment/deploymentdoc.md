# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Multicapa1: Es una red neuronal multicapa con dos capas ocultas (la primera con 100 neuronas y la segunda con 2 neuronas), utilizando la extracción de características mediante la técnica de bolsa de palabras.
- **Plataforma de despliegue:** Fast Api
- **Requisitos técnicos:** Las versión de python es 3.10.12 (main, Nov 20 2023, 15:14:05), en la cual se usaron los siguientes paquetes en sus respectivas versiones

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

- **Requisitos de seguridad:** No necesita proceso de autentificación pues se trabaja internamente remitiendo la consulta al área encargada.
- **Diagrama de arquitectura:** 
![Captura de pantalla 2024-05-30 185727](https://github.com/cdtafurd/mlds6_project/assets/119061844/6510066a-0548-4a8c-8214-cc20183b04a0)


## Código de despliegue

- **Archivo principal:** despliegue.py
- **Rutas de acceso a los archivos:** Modelo elegido para el despliegue: https://github.com/cdtafurd/mlds6_project/blob/master/docs/deployment/model.joblib
- **Variables de entorno:** (lista de variables de entorno necesarias para el despliegue)

  - `API_KEY`
  - `MODEL_PATH`
  - `LOG_LEVEL`

## Documentación del despliegue

### Instrucciones de instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/cdtafurd/mlds6_project
   cd mlds6_project
   ```

2. Crear un entorno virtual y activarlo:
   ```bash
   python3.10 -m venv env
   source env/bin/activate
   ```

3. Instalar los paquetes requeridos:
   ```bash
   pip install -r requirements.txt
   ```

### Instrucciones de configuración

1. Configurar las variables de entorno necesarias:
   ```bash
   export API_KEY="api_key"
   export MODEL_PATH="./model.joblib"
   export LOG_LEVEL="INFO"
   ```

2. Editar el archivo de configuración `config.yaml` para ajustar parámetros específicos de la implementación.

### Instrucciones de uso

1. Iniciar la aplicación:
   ```bash
   uvicorn despliegue:app --host 0.0.0.0 --port 8000
   ```

2. Enviar una solicitud POST al endpoint `/hate` con el siguiente formato:
   ```json
   {
     "text": ["sample text"]
   }
   ```

3. Recibir la respuesta con las predicciones:
   ```json
   {
     "is_hate": [0, 1]
   }
   ```

### Instrucciones de mantenimiento

1. Monitorear los logs de la aplicación para detectar cualquier problema:
   ```bash
   tail -f logs/app.log
   ```

2. Realizar copias de seguridad periódicas del modelo y los datos relacionados.

3. Actualizar los paquetes y el modelo según sea necesario:
   ```bash
   pip install --upgrade -r requirements.txt
   ```

## Código de despliegue adicional

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib

class ApiInput(BaseModel):
    text: List[str]

class ApiOutput(BaseModel):
    is_hate: List[int]

app = FastAPI()
model = joblib.load("model.joblib")

@app.post("/hate")
async def define_sentiment(data: ApiInput) -> ApiOutput:
    predictions = model.predict(data.text).tolist()
    return ApiOutput(is_hate=predictions)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

## Script de configuración del repositorio

```bash
mkdir mlapi
mv despliegue.py model.joblib mlapi/
cd mlapi/

git config --global user.email "wlpuertasb@unal.edu.co"
git config --global user.name "LeonardoPuertas"
git config --global init.defaultBranch master
git init

cat <<EOF >requirements.txt
pandas==2.0.3
tensorflow==2.15.0
keras==2.15.0
os
re
numpy==1.25.2
matplotlib==3.7.1
sklearn==1.2.2
mlflow==3.7.1
mlflow.sklearn==1.2.2
EOF

cat <<EOF >railway.json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "uvicorn despliegue:app --host 0.0.0.0 --port \$PORT",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
EOF

git add railway.json requirements.txt despliegue.py model.joblib
git commit -m "Agregamos los archivos del API."

token=""
repo_url="https://github.com/cdtafurd/mlds6_project/edit/master/docs/deployment/deploymentdoc.md"

url_token="${repo_url/https:\/\//https:\/\/$token@}"
export GITHUB=$url_token

git remote add origin $GITHUB
git push origin master
```

## Información Adicional

- **Endpoint de la API:** [API en producción](https://mlapi-production-272c.up.railway.app)
- **Repositorio del proyecto:** [Repositorio GitHub](https://github.com/cdtafurd/mlds6_project)

