# Integración de un LLM en una arquitectura por microservicios.

## Descripción

En este proyecto se implementó una arquitectura de microservicios integrando un LLM en Flask. El proyecto consta de los siguientes microservicios:

- Servicio de autenticacion:
- Servicio de chat:

Adicionalmente, durante el desarrollo del proyecto se buscó que la arquitectura cumpliera con los cuatro atributos de calidad esenciales: modificabilidad, comprobabilidad, seguridad y capacidad de despliegue, que serán detallados más adelante.

### RamenAI

RamenAI consiste en un chatbot enfocado a entusiastas del ramen. El chat genera recomendaciones y diferentes recetas de acuerdo a tus gustos y basado en el historial de conversaciones pasadas de cada usuario.

## Diagramas 




# Guía de despliegue de Docker

### Prerequisitos

- Docker
- MongoDB uri

1. Clonar el repositorio (clonar branch *OneContainer*), entra a la carpeta de RamenAI 
```
cd RamenAI
```
Paso 2: Crear el Archivo .env
```
OPENAI_API_KEY = "your_api_key"
MONGO_URI = "your_mongodb_uri"
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
MYSQL_USER=your_sql_usesr
MYSQL_PASSWORD=your_password
MYSQL_DB=ramenAI
```
Paso 3: Desplegar la Arquitectura con Docker Compose
```
docker-compose up --build
```

# Abrir el proyecto de forma local (branch main)

### Prerequisitos

- Python
- MySQL (server local)
- MongoDB uri
- *Los siguientes pasos son basados en el main*


## Set up
1. Después de clonar el repositorio desde la branch **main**, entra a la carpeta de RamenAI
```
cd RamenAI
```
2. Se debería de ver una organización así, siendo la primer carpeta RamenIA donde se clonó el repositorio.
```
C:\Users\John\Documents\Code\RamenAI\RamenAI>
```
2. Crea un ambiente virtual
```
py -3 -m venv .venv
```
5. Activa el ambiente virtual
```
.venv\Scripts\activate
```
6. Instala las dependencias del proyecto
```
poetry install
```
8. Corre la aplicación en modo debug.
```
.venv/Scripts/flask --debug --app ramenai.main run
```
### Herramientas de desarrollo
Corre el formatter de RamenAI
```
.venv/Scripts/black ./
```
Corre el linter de RamenAI
```
cd ramenai
../.venv/Scripts/pylint .
```
Corre pruebas de unidad
```
.venv/Scripts/pytest
```
Para ver el coverage y qué líneas aún no se prueban
```
.venv/Scripts/pytest --cov --cov-report term-missing
```
