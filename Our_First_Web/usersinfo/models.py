from django.db import models

# Create your models here.

class User(models.Model):

	genders = [('1','Male'), ('2','Female'), ('3', 'Nan')]

	username = models.CharField(max_length=50, verbose_name='player name')
	nickname = models.CharField(max_length=50)
	score = models.PositiveIntegerField(default=0) 
	online = models.BooleanField(default=True)
	image = models.ImageField(upload_to='profile_images/', default='profile_images/me_image.jpg')
	gender = models.CharField(max_length=10, choices=genders, default=genders[2])

	def __str__(self):
		return(self.username)

	class Meta:
		verbose_name = 'NewPlayer'
		ordering = ['-score']

# score = models.PositiveIntegerField()
# upload_to='profile_images/' specifies that uploaded images will be stored in the profile_images/ directory within your media root. Django will create this directory if it does not already exist.
# online by default is true, we will need to make it false when a user logs out
		
class Player(models.Model):
	Player_Name = models.CharField(max_length=50, verbose_name='Nan')
	
	def __str__(self):
		return(self.Player_Name)
	
class PlayerHistory(models.Model):
	Name = models.CharField(max_length=50, verbose_name='Nan')
	Previous_Games = models.ManyToManyField(Player)
	def __str__(self):
		return(self.Name)