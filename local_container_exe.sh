#!/bin/bash

username=$1
password=$2

echo "Tentative de connexion à Docker..."
docker login -u $username -p $password

if [ $? -ne 0 ]; then
    echo "La connexion a echoue."
    exit 1
else
    echo "Connexion reussie."
fi

echo "Tentative de telechargement de l'image Docker..."
docker pull jinxfly/python-oc-lettings-fr:latest

if [ $? -ne 0 ]; then
    echo "Le telechargement de l'image Docker a echoue."
    exit 1
else
    echo "Telechargement reussi."
fi

echo "Tentative de run du conteneur Docker..."
var=$(docker run -d -p 8000:8000 jinxfly/python-oc-lettings-fr:latest)

if [ $? -ne 0 ]; then
    echo "Le run du conteneur Docker a echoue."
    exit 1
else
    echo "Le run du conteneur Docker a reussi."
    echo "Vous pouvez arreter le processus avec la commande : docker stop ${var:0:12}"
    echo "Vous pouvez acceder au site à l'adresse suivante : http://127.0.0.1:8000/"
fi
