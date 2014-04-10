from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

#para administrar usuarios
class UserManager(BaseUserManager):

	def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
		if not email:
			raise ValueError('El email debe ser obligatorio')
		email = self.normalize_email(email)
		user  = self.model(username=username, email=email, is_active=True, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)	
		user.set_password(password)
		user.save(using = self._db) #p q use la db por defecto
		return user

	def create_user(self, username, email, password=None, **extra_fields):
		return self._create_user( username, email, password, False, False, **extra_fields)

	def create_superuser(self, username, email, password=None, **extra_fields):
		return self._create_user( username, email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

	username 	= models.CharField(max_length=50, unique=True)
	email 		= models.EmailField(max_length=50, unique=True)
	first_name 	= models.CharField(max_length=100)
	last_name 	= models.CharField(max_length=100)
	avatar 		= models.URLField()

	objects 	= UserManager()

	is_active 	= models.BooleanField(default=True)
	is_staff 	= models.BooleanField(default=False)

	USERNAME_FIELD 	= 'username'
	REQUIRED_FIELDS = ['email']

	def get_short_name(self):
		return self.username