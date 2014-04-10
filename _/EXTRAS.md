#Curso de DJANGO de [devcode.la](http://www.devcode.la/)

####GIT EN DJANGO  
+ Todo proyecto de Django debe estar alojado en su propio virtualenv
+ Repo en github:  
    nombre: cristiancena/devcodela-django  
    http:   https://github.com/cristiancena/devcodela-django.git  
    ssh:    git@github.com:cristiancena/devcodela-django.git  
    * Ayuda inicial:
        - Create a new repository on the command line  
            touch README.md  
            git init  
            git add README.md  
            git commit -m "first commit"  
            git remote add origin git@github.com:cristiancena/devcodela-django.git  
            git push -u origin master  
        - Push an existing repository from the command line  
            git remote add origin git@github.com:cristiancena/devcodela-django.git  
            git push -u origin master  
+ Como crear una clave publica para git:  
    http://librosweb.es/pro_git/capitulo_4/generando_tu_clave_publica_ssh.html  
+ Clonar un repositorio de django  
    Clonamos el repositorio `$ git clone {https...repositorio.git}`  
    Instala las dependencias `$ pip install -r requeriments.txt`   


####DEPLOYMENT DE DJANGO EN HEROKU 
requisitos: git, python, virtualenv, postgresql, heroku toolbet y una cuenta en heroku
nos logueamos en heroku: `heroku login`
creamos y entramos en la carpeta que contendrá el proyecto `mkdir mysite && cd mysite`
creamos un entorno virtual: misite$ `virtualenv mientorno` 
... y lo activamos: misite$ `source/mientorno/bin/activate`
instalamos algunos paquetes que necesitaremos: misite$ `pip install django-toolbelt`
creamos el proyecto django: `django-admin.py startproject mysite .` 
El '.' hace que django extraiga todas las carpetas en el mismo directorio donde se ejecuta
el comando y no en una nueva carpeta
Creamos un archivo llamado Procfile en la raiz: `touch Procfile` y añadimos en su interior:
`web: gunicorn mysite.wsgi` esto es un comando que ejecutará dyno, la unidad básica de heroku
creamos, tb en la raiz, un archivo requeriments.txt donde colocaremos las dependencias 
`pip freeze > requirements.txt` 


####TASTYPIE EN DJANGO 
    

####MANIPULACION BÁSICA DE POSTGRESQL 
    

####SOUTH EN DJANGO 
    
