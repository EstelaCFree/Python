# Git — Rutina diaria del curso de Python

## 1. Al empezar la clase

Abrir la terminal en la carpeta `Python-clase`.

Comprobar que no hay cambios pendientes:

git status

Actualizar mis archivos desde GitHub y descargar las novedades de la profesora:

git pull --ff-only origin main

git fetch upstream

git merge upstream/main

git push origin main

## 2. Durante la clase

- Trabajar en `Python-apuntes/`, dentro de `Python-clase/`.
- No modificar los archivos originales de la profesora.

## 3. Al terminar la clase

Comprobar los cambios:

git status

Guardar y subir mis apuntes y ejercicios:

git add Python-apuntes/

git commit -m "Apuntes y ejercicios de clase"

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

git merge upstream/main

git push origin main

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
