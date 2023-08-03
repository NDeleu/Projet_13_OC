@echo off
SET username=%~1
SET password=%~2

echo Tentative de connexion à Docker...
docker login -u %username% -p %password%
IF %errorlevel% NEQ 0 (
    echo La connexion a echoue.
    exit /b %errorlevel%
) ELSE (
    echo Connexion reussie.
)

echo Tentative de telechargement de l'image Docker...
docker pull jinxfly/python-oc-lettings-fr:latest
IF %errorlevel% NEQ 0 (
    echo Le telechargement de l'image Docker a echoue.
    exit /b %errorlevel%
) ELSE (
    echo Telechargement reussi.
)

echo Tentative de run du conteneur Docker...
FOR /F "tokens=*" %%i IN ('docker run -d -p 8000:8000 jinxfly/python-oc-lettings-fr:latest') DO SET var=%%i
IF %errorlevel% NEQ 0 (
    echo Le run du conteneur Docker a echoue.
    exit /b %errorlevel%
) ELSE (
    echo Le run du conteneur Docker a reussi.
    echo Vous pouvez arreter le processus avec la commande : docker stop %var:~0,12%
    echo Vous pouvez acceder au site à l'adresse suivante : http://127.0.0.1:8000/
)
