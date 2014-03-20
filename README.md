#Curso de DJANGO de [devcode.la](http://www.devcode.la/)

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
+ Instalamos el conector de python con postgres dentro del entorno virtual virtualenv_django:  
	(virtualenv_django)➜  devcodela-django git:(master) ✗   
		`pip install pscopg2`  
		`pip freeze --local`  (Copiamos esta dependencia a requirements.txt)
+ Sincronizamos la DB `python manage.py syncdb --settings=SistemaDiscusiones.settings.local`
	Nos pregunta si queremos crear un superusuario, le damos que si.
	el usuario que aquí creamos es con el que ingresaremos en el admin
+ Verificamos las tablas que se han creado en la db:  
	`su postgres`  
	postgres@chicha:/home/chicha$ `psql Discusiones`  
	`Discusiones=# \d`  
	Con `\q` salimos

#####
	List of relations
	 Schema |               Name                |   Type   |    Owner    
	--------+-----------------------------------+----------+-------------
	 public | auth_group                        | table    | cursodjango
	 public | auth_group_id_seq                 | sequence | cursodjango
	 public | auth_group_permissions            | table    | cursodjango
	 public | auth_group_permissions_id_seq     | sequence | cursodjango
	 public | auth_permission                   | table    | cursodjango
	 public | auth_permission_id_seq            | sequence | cursodjango
	 public | auth_user                         | table    | cursodjango
	 public | auth_user_groups                  | table    | cursodjango
	 public | auth_user_groups_id_seq           | sequence | cursodjango
	 public | auth_user_id_seq                  | sequence | cursodjango
	 public | auth_user_user_permissions        | table    | cursodjango
	 public | auth_user_user_permissions_id_seq | sequence | cursodjango
	 public | django_admin_log                  | table    | cursodjango
	 public | django_admin_log_id_seq           | sequence | cursodjango
	 public | django_content_type               | table    | cursodjango
	 public | django_content_type_id_seq        | sequence | cursodjango
	 public | django_session                    | table    | cursodjango
	(17 rows)

+ Instalamos South: Cuando modificamos los modelos de django toca modificar las tablas a mano, y esto es un bajón, pero se soluciona con south, que hace todo por nosotros:
	`pip install south` 
+ llevamos esta nueva dependencia al archivo de requeriments base.txt
	`pip freeze --local`
+ Sincronizamos la db, para generar la tabla de migraciones que trae south


####5 DISEÑO DE APLICACIONES
	Las aplicaiones de django son librerías pequeñas diseñadas para representar un aspecto simple del proyecto. El proyecto esta formado por multiples aplicaciones.
	El Third Party Packages son aplicaciones reusables de djago que podemos obtener del paquete de herramientas de python e instalarlas con pip dentro de nuestro entorno virtual (ej: south). 
	creamos la carpeta {proyecto}/apps y dentro hacemos:
	`django-admin.py startapp {nombre_de_la_aplicacion}` 
	nombre_aplicacion
		\__ __init__.py #es p q la carpeta se convierta en un modulo
		\__ admin.py #cambios q tienen que ver con el administrador
		\__ models.py #los modelos de la aplicación
		\__ test.py #las pruebas unitarias
		\__ views.py #las vistas de la aplicación
	Todas las aplicaciones deben colocarse en la tupla LOCAL_APPS

	quedamos en 04:00