## Set up
1. Después de clonar el repositorio, entra a la carpeta de RamenIA
```
cd LearnIA
```
2. Se debería de ver una organización así, siendo la primer carpeta RamenIA donde se clonó el repositorio.
```
C:\Users\John\Documents\Code\RamenIA\RamenIA>
```
3. Entra a la carpeta del proyecto.
```
C:\Users\John\Documents\Code\RamenIA\RamenIA\RamenIA>
```
4. Crea un ambiente virtual
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
7. Regresa a la carpeta principal del repositorio.
```
cd ..
```
8. Corre la aplicación en modo debug.
```
./RamenAI/.venv/Scripts/flask --debug --app RamenAI.main run
```
### Herramientas de desarrollo
Corre el formatter de RamenAI
```
./RamenAI/.venv/Scripts/black ./
```
Corre el linter de RamenAI
```
cd RamenAI
.venv/Scripts/pylint .
```
