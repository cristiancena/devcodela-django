from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import User

class UserAdmin(UserAdmin):

	fieldsets = (
		('User', 			{'fields' : ('username', 'password')}),
		('Persona Info', 	{'fields' : ('first_name', 'last_name', 'email', 'avatar')}),
		('Permissions', 	{'fields' : ('is_active', 'is_staff','is_superuser','groups','iser_permissions' )})
	)

# Registramos el modelo User para que el administrador de django lo reconozca y lo muestre
# Le pasamos ademas un segundo parametro con la clase UserAdmin para que se visualize a uestro gusto
admin.site.register(User, UserAdmin)