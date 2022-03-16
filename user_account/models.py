from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone



class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None , fname = '' , lname = ''):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)
		user.firstname = fname; 
		user.lastname= lname; 
		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.is_active = True
		user.save(using=self._db)
		return user


def upload_location(instance, filename, **kwargs):
	file_path = 'account/image/{filename}'.format(
			 title=str(instance.username), filename=filename
		) 
	return file_path

def upload_cover(instance, filename, **kwargs):
	file_path = 'account/cover/{filename}'.format(
			 title=str(instance.username), filename=filename
		) 
	return file_path


class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=False)
	image 					= models.ImageField(upload_to=upload_location, blank=True , null=True , default = 'a2.jpg' )
	cover					= models.ImageField(upload_to=upload_cover, blank=True , null=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	firstname 				= models.CharField(max_length=40 , default = '', null=True)
	lastname 				= models.CharField(max_length=40 , default = '', null=True)
	bio						= models.CharField(max_length=100, default = '', null=True)
	phone					= PhoneNumberField(null=True, blank= True)
	date_birth				= models.DateField(max_length=8 ,default= timezone.now  , blank = True) 
	province				= models.CharField(max_length=30,null = True , default = '')
	job						= models.CharField(max_length = 30 , null = True , default = '')
	gender					= models.CharField(max_length = 7 , null = True , default = 'male')
	

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']
	objects = MyAccountManager()
	def __str__(self):
		return self.email

	# For checking permissions.
	def has_perm(self, perm, obj=None):
		return self.is_admin
	# Does this user have permission to view this app? 
	def has_module_perms(self, app_label):
		return True
	@property
	def _image(self):

		if self.image :
			return self.image
		return None

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


