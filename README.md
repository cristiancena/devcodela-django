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

####6 VISTAS Y URLS: Una vista no es nada sin una url que la enlace
	Vistas genéricas: Cada una realiza una tarea en especifico.
		- View: Es la clase padre de todas las vistas genéricas.
				Implementa solo métodos HTTP: get, post, put, delete 
		- TemplateView: Es una vista que renderiza un template y que pasa en 
						el contexto cualquier argumento que pase por url
		- CreateView: 	Crea una instancia de un objeto con una respuesta 
						renderisaza al template
		- DetailView: renderiza el detalle de un solo objeto, por defecto toma 
						la instancia del modelo que se le asigne
		- DeleteView: Elimina un objeto y renderiza una respuesta al template
		- UpdateView: Lo mismo pero para actualizar un objeto
		- ListView: renderiza un listado de objetos asignados en el attr model 
					o en el attr queryset
		- 
	Vistas basadas en clases: 
		Si una vista generica se acerca mucho a lo que queremos realizar y debemos sobreescribir los atributos y métodos que estas nos dan. Si este es el caso, se debe usar una vista basada en clases. Las vistas basadas en clases heredan las funcionalidades de las vistas genericas de django.
		Ej de url:
			url(r'^django/$' , IndexView.as_view()), 
	Vistas basadas en funciones: 
		Se usa para cuando queremos hacer algo muy complejo de implementar en una vista basada en clases. Por ejemplo cuando queremos procesar mas de un formulario en una sola vista.
		Ej de url: 
			url(r'^django/$' , 'apps.home.views.index'),

	El atributo name: 
		toda url lo tiene, el name le da un nombre a la url para poder llamarla por dicho nombre. 
	Los namespaces: 
		Cuando tenemos muchas aplicaciones es comun que entre ellas haya urls con los mismos nombres. 
		Cada aplicacion debe tener su propio archivo de urls ya que django tiene su propio archivo de urls (el archivo principal digamos) en la carpeta del proyecto donde se deben incluir los anteriores. 
		

####7 MOTOR DE TEMPLATES DE DJANGO
	La vista le manda la informacion a un template apoyandose en los shortcuts de django, en este caso usamos el shortcut render
	render recibe como parametro un contexto, un template y la informacion que se enviara a ese template en forma de diccionario y devuelve una respuesta
	Django lee la variable TEMPLATE_DIRS alojada en base.py para saber donde tenemos alojados nuestros templates 
	El contexto (context) es toda informacion que envia una vista a un template en forma de diccionario.
	Procesadores de contexto (context processors): Son funciones que retornan un diccionario, el cual se envia a todos los templates que tengamos sin necesidad de repetir el codigo. Estos nacen ante la necesidad de enviar la misma información a diferentes templates.
	Los procesadores de contexto que vienen por defecto y que más usaremos son:
		auth: para autentificar usuarios
		media: nos envia la variable media_url para poder enlazar las imagenes que se suban al servidor.
		static: nos envia la variable static_url para enlazar los archivos estaticos.
		tz: es el time zone y nos trae la hora actual 
	Logica en los Templates:
	variables: 	{{ person_name }} 	Las enviamos en la vista como diccionario
	tag/etiquetas: 	{% tag %} 
		El tag {% for objeto in diccionario %} sirve para recorrer una lista de objetos
		El tag {% if %} el condicional de toda la vida

	Herencia de templates: Permite construir un template base que contenga todos los elementos comunes en donde definimos bloques que podran ser sobreescritos sobre los tamplates hijos

####8 ARCHIVOS ESTÁTICOS
	Archivos estáticos son: Imagenes, files.js, files.css, etc.
	En django cada aplicacion puede tener sus propios archivos estáticos
	La variable STATICFILES_DIRS solo se usa en un ambiente local por lo tanto esta dentro de local.py ya que en un entorno de produccion nunca debemos servir los archivos estáticos en el mismo servidor donde tengamos nuestro proyecto de django.
	
	La manera correcta de cargar los archivos estáticos es usando el template-tag "load static" 
		{% load static from staticfiles%}
		<link rel="stylesheet" href="{% static "estilos.css" %}">
	Lo que hace es cargar todos los archivos estaticos de una manera dinamica desde los staticfiles.
	Para un entorno local el Debug siempre debe estar en true y para produccion debemos cambiarlo a false

	Como tratar los archivos estaticos en un entorno de produccion?
	STATIC_ROOT es una variable donde indicamos donde queremos coleccionar todos los archivos estaticos del proyecto


####9 CUSTOM USER MODEL: Modelo de usuarios personalizado
	El custom user model nos permite personalizar el modelo de usuarios que django trae por defecto. Personalizar el modelo de usuarios que django trae por defecto conlleva tambien a personalizar la administracion y la autentifición. Para lo cual debemos usar 2 clases abstractas y 1 mixin de permisos:
		AbstractBaseUser: Sirve p crear nuestro modelo de usuarios
		BaseUserManager: Sirve para crear el administrador del modelo
		Permission mixin: Sirve para dar permisos a nuestros usuarios
	
	Creamos nuestro propio modelo de usuarios personalizado:
		1 creamos una app para los usuarios. En root/apps:
			$ django-admin.py startapp users
			y declaramos la app en LOCAL_APPS de  base.py 
		2 creamos el modelo en models.py dentro de nuestra app users
		3 Creamos el manager o administrador
			El attr objects de un modelo es un intermediario entre las transacciones de cada modelo. Ej: model.objects.all() trae todos los objetos de ese modelo. objects es el manager que tiene cada modelo.
		4 Sincronizamos la base de datos
			python manage.py syncdb --settings=SistemaDiscusiones.settings.local
		5 creamos una migracion: Siempre es bueno tener la migracion al inicio 
			de la aplicacion, sino despues podemos tener muchos problemas.
			--initial: xq es la migracion inicial
			python manage.py schemamigration users --initial --settings=SistemaDiscusiones.settings.local
		6 Aplicamos la migracion:	
			--fake: xq hacemos una migracion falsa. Esto se debe a que creamos la tabla usando syncdb, siempre que hagamos esto se debe crear una migracion falsa. Otro escenario es crear las tablas solo usando las migraciones prescindiendo de syncdb
			python manage.py migrate --fake users --settings=SistemaDiscusiones.settings.local


####10 Social login auth
	Usamos la libreria *python social auth* que no solo permite autentificación sino tambien asociar múltiples cuentas de redes sociales a una sola cuenta de usuario
	root-del-proyecto: 	$ pip install python-social-auth
						$ pip freeze --local
	copiamos python-social-auth==0.1.23 y lo pegamos en base.txt del directorio requeriments
	tambien la declaramos en THIRD_PARTY_APPS en base.py como:
	'social.apps.django_app.default',
	sincronizamos la base de datos:
	python manage.py syncdb --settings=SistemaDiscusiones.settings.local







