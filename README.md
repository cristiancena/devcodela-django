#Curso de Django de devcode.la

===============================================================================
INSTALACION DE DJANGO
===============================================================================
	setup tools:
		$ sudo apt-get install python-setuptools
	pip:
		$ sudo easy_install pip
	virtual enviroment:
		$ pip install virtualenv
	crear un entorno virtual:
		$ virtualenv {nombre_del_entorno_virtual}
	activar un entorno virtual:
		$ source {nombre_del_entorno_virtual}/bin/activate
	instalar django (dentro de un entorno virtual):
		(entorno_virtual)$ pip install django 
	crear proyecto de django:
		(entorno_virtual)$ django-admin.py startproject {nombre_proyecto}


===============================================================================
OPTIMO ENTORNO DE DESARROLLO
===============================================================================
	Arrancamos el proyecto indicando otro archivo de configuracion:
	python manage.py runserver --settings=!SistemaDiscusiones.settings.local
	Aunque a mi me andubo así: 
		python manage.py runserver --settings=SistemaDiscusiones.settings.local

	El unipath es un paquete de python que nos ayuda en el manejo de rutas a directorios y a archivos:
	Vamos a la terminal, nos aseguramos que tenemos activo nuestro entorno virtual y tipeamos:
	$ pip install unipath

	preguntas:
		tengo que crear el directorio templates o el archivo templates.py? 
		tiene que estar alojado en el mismo directorio que manage.py?

	Requeriments:
		Son archivos de texto donde están todas las dependencias utilizadas por nuestro proyecto. 
		Las dependencias son aplicaciones extra que instalamos p q nuestro proyecto funcione
		Debemos tener tantos archivos requirements como archivos dentro de settings, c-u p un ambiente de trabajo
		¿Como saber que dependencias tengo instaladas en mi entorno virtual?
			$ pip freeze --local 
			Copiamos estas dependencias comunes y las pegamos en base.txt 
		Los requirements sirven para llevar nuestro proyecto a otro ambiente de trabajo, ya que solo vamos a tener que crear un entorno virtual y ejecutar el archivo requirements.txt que corresponda con el comando:
			$ pip install -r requeriments/local.txt
			De este modo tendremos todas las dependencias para continuar con el proyecto en otro lado.


===============================================================================
DEPLOYMENT DE DJANGO EN HEROKU
===============================================================================	


===============================================================================
GIT EN DJANGO
===============================================================================	
	Todo proyecto de Django debe estar alojado en su propio virtualenv
	