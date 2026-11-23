# Git — Rutina diaria del curso de Python

## 1. Al empezar la clase

Abrir la terminal en la carpeta `Python-clase`.

cd Python-clase

Comprobar que no hay cambios pendientes:

git status

Actualizar mis archivos desde GitHub y descargar las novedades de la profesora:

git pull --ff-only origin main

git fetch upstream

git merge upstream/main -m "Actualizar desde la profesora"

git push origin main

(El `-m` es imprescindible: sin él, Git abre un editor para pedir el mensaje. Ver «Si se abre el editor» abajo.)

## 2. Durante la clase

- Trabajar en `Python-apuntes/`, dentro de `Python-clase/`.
- No modificar los archivos originales de la profesora.

## 3. Al terminar la clase

Comprobar los cambios:

git status

Guardar y subir mis apuntes y ejercicios:

cd Python-clase

git add Python-apuntes/

git commit -m "Inicio modulo 3 y apuntes funciones"

git push origin main

Puedo cambiar el mensaje del commit para indicar lo que he trabajado ese día.

## 4. Cuando cambie de ordenador

**En el ordenador que dejo:**

git status

git add Python-apuntes/

git commit -m "Guardar progreso"

git push origin main

Si no hay cambios pendientes, no necesito hacer commit.

**En el ordenador donde voy a trabajar:**

git pull --ff-only origin main

Si también quiero actualizar los materiales de la profesora:

git fetch upstream

git merge upstream/main -m "Actualizar desde la profesora"

git push origin main

---

## Si se abre el editor (Vim) y no puedo salir

Pasa si hago `git merge` o `git commit` sin `-m "mensaje"`.

1. Pulsar `ESC`.
2. Escribir `:wq` y pulsar `Enter` (guarda y sale; el merge se completa con el mensaje por defecto).

Si en lugar del texto aparece **«ATTENTION / Found a swap file»** (pasa cuando la vez anterior se cerró la terminal con Vim abierto): pulsar `D` (Delete it) y seguir con los pasos 1–2.

Si ya cerré la terminal y `git status` dice **«All conflicts fixed but you are still merging»**:

git commit -m "Actualizar desde la profesora"

---

## Recordatorios

- **origin:** mi fork (`EstelaCFree/Python`).
- **upstream:** repositorio de la profesora (`anaisabelveg/Python_Fundae`).
- **pull:** descargar e integrar cambios.
- **fetch:** descargar novedades sin integrarlas.
- **merge:** integrar cambios.
- **commit:** guardar cambios localmente.
- **push:** subir cambios a GitHub.
- Ejecutar los comandos desde la carpeta `Python-clase`.
- Antes de sincronizar, comprobar que no tengo cambios locales sin guardar en un commit.
- Si Git muestra conflictos o errores, resolverlos antes de continuar.
- **Un commit sin push no se sincroniza con el otro Mac.**
