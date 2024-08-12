# 2024-2-Tester-Tarea

En este repositorio se encuentran distintos tests para la tarea del curso.

Para correrlo los pasos son los siguientes:


* primero correr el servidor de su api.
>Rails S

* Luego se debe correr el main del backend en el tester .

>python main.py

Este retornara los test que se logran pasar y seran guardados en un json. Teniendo el json, la idea es que creen un servidor de python que entregue ese json. Esto lo puedne hacer con 

>python -m http.server 8000

y luego para revisar el tester en su navegador colocar 

> http://localhost:8000/frontend/

Esto deberia mostrarles una pagina donde pueden desglosar el resultado del tester y apretando cada test decirle a que se debe el error y algun hint para arreglarlo.

Recordar que no revisaremos con exactamente los mismos test pero si logran pasar todos los publicos no deberian tener problemas con los privados.