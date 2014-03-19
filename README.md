#Curso de DJANGO de [devcode.la](http://www.devcode.la/)

####GIT EN DJANGO	
+ Todo proyecto de Django debe estar alojado en su propio virtualenv
+ Repo en github: 
	nombre: cristiancena/devcodela-django	
	http:	https://github.com/cristiancena/devcodela-django.git
	ssh: 	git@github.com:cristiancena/devcodela-django.git
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
`$ git clone {https...repositorio.git}` Clona el repositorio
`$ pip install -r requeriments.txt` Instala las dependencias

####DEPLOYMENT DE DJANGO EN HEROKU
	

####2 INSTALACION DE DJANGO
*	setup tools:
	`$ sudo apt-get install python-setuptools`
*	pip:
	`$ sudo easy_install pip`
*	virtual enviroment:
	`$ pip install virtualenv`
*	crear un entorno virtual:
	`$ virtualenv {nombre_del_entorno_virtual}`
*	activar un entorno virtual:
	`$ source {nombre_del_entorno_virtual}/bin/activate`
*	instalar django (dentro de un entorno virtual):
	`(entorno_virtual)$ pip install django`
*	crear proyecto de django:
	`(entorno_virtual)$ django-admin.py startproject {nombre_proyecto}`


####3 OPTIMO ENTORNO DE DESARROLLO
+	Arrancamos el proyecto indicando otro archivo de configuracion:
	`$ python manage.py runserver --settings=!SistemaDiscusiones.settings.local`
+	Aunque a mi me andubo así: 
	`$ python manage.py runserver --settings=SistemaDiscusiones.settings.local`
+	El unipath es un paquete de python que nos ayuda en el manejo de rutas a directorios y a archivos:
	* Vamos a la terminal, nos aseguramos que tenemos activo nuestro entorno virtual y tipeamos:
		`$ pip install unipath`
+	Requeriments:
	* Son archivos de texto donde están todas las dependencias utilizadas por nuestro proyecto. 
	* Las dependencias son aplicaciones extra que instalamos p q nuestro proyecto funcione
	* Debemos tener tantos archivos requirements como archivos dentro de settings, cada uno para un ambiente de trabajo
	* ¿Como saber que dependencias tengo instaladas en mi entorno virtual?
		`$ pip freeze --local`		
		- Copiamos estas dependencias comunes y las pegamos en base.txt 
		- Los requirements sirven para llevar nuestro proyecto a otro ambiente de trabajo, ya que solo vamos a tener que crear un entorno virtual y ejecutar el archivo *requirements.txt* que corresponda con el comando:
			+ `$ pip install -r requeriments/local.txt`
			+ De este modo tendremos todas las dependencias para continuar con el proyecto en otro lado.

####4 CONEXION DE DJANGO CON POSTGRESQL
+  libreria para conectarse con postgresql en linux `sudo apt-get install libpq-dev python-dev`
+ instalar postgre `sudo apt-get install postgresql`
+ iniciamos el servicio `sudo service postgresql start`
+ clave para el usuario postgres `sudo passwd postgres`
+ ingresamos al usuario postgres `su postgres` (nos pide la clave, ok)
+ creamos un nuevo usuario:	`createuser cursodjango` 
+ creamos una db `createdb Discusiones`
+ cambiamos la clave del usuario cursodjango (le creamos una)
	* para ello entramos en la db: `psql Discusiones`
	* luego: `Discusiones=# ALTER USER cursodjango WITH PASSWORD 'pass';`
+ Llevamos estos datos de configuracion a nuestro settings de django (local.py)
+ Instalar el conector de python con postgres:
	* 






####5 DISEÑO DE APLICACIONES