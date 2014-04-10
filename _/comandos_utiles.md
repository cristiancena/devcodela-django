#para iniciar el entorno virtual 
`source <entorno>/bin/activate`

#en la raiz del proyecto, para arrancar el servidor local
`python manage.py runserver --settings=SistemaDiscusiones.settings.local`

#para ver las dependencias 
`pip freeze --local`

#en la carpeta rootproject/apps
`django-admin.py startapp nombreapp`

#para sincronizar la db con los modelos
`python manage.py syncdb --settings=SistemaDiscusiones.settings.local`

#para crear una migracion
`python manage.py schemamigration nombremodelo --initial --settings=SistemaDiscusiones.settings.local`

#para crear un superusuario de django
`python manage.py createsuperuser --settings=SistemaDiscusiones.settings.local`

#para instalar las dependencias que tenemos en requeriments.txt http://rukbottoland.com/blog/c%C3%B3mo-instalar-paquetes-python-con-requirementstxt/
`pip install -r requirements.txt`

#comandos postgre: http://caronates.wordpress.com/2010/01/12/comandos-para-postgres/
	
`sudo service postgresql start`  	iniciamos el servicio
`su postgres`						nos logueamos
`createuser nombreUsuario`			creamos un usuario
`createdb nombreDb`					creamos una db
`psql nombreDb`						entramos en una db
`\q`								salimos
`\dt`								lista las tablas de una db
`\du`								lista los usuarios 