# Integración de un LLM en una arquitectura por microservicios.

En este proyecto se implementó una arquitectura de microservicios integrando un LLM en Flask.




# Docker







# Abrir el proyecto de forma local

## Set up
1. Después de clonar el repositorio, entra a la carpeta de RamenAI
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
