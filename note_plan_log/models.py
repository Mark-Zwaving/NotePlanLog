from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, AbstractUser, UserManager

class WebUser(models.Model):
    GENDER_OPT = (
        ( 'M',  'Male' ),
        ( 'F',  'Female' ),
        ( 'N', 'Non-binair' ),
    )
    phone          =  models.CharField( max_length=12 )
    gender         =  models.CharField( max_length=1, choices=GENDER_OPT )
    function       =  models.CharField( max_length=5 )
    birthday_date  =  models.DateField( null=True, blank=True )
    user           =  models.OneToOneField( User, unique=True, on_delete=models.CASCADE )

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        WebUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.webuser.save()

class Note( models.Model ):
    date      =  models.DateField( )
    title     =  models.CharField( max_length=100 )
    text      =  models.TextField( )
    created   =  models.DateTimeField( auto_now_add=True )
    user      =  models.ForeignKey( User, on_delete=models.CASCADE)
    is_active =  models.SmallIntegerField( )

    def __str__(self):
        return self.title

class Plan( models.Model ):
    date       =  models.DateField( )
    time_start =  models.TimeField( )
    time_end   =  models.TimeField( )
    title      =  models.CharField( max_length=100 )
    text       =  models.TextField( )
    last_saved =  models.DateTimeField( auto_now_add=True )
    user       =  models.ForeignKey( User, on_delete=models.CASCADE )
    is_active  =  models.SmallIntegerField( )

    def __str__(self):
        return self.title

class Log( models.Model ):
    date       =  models.DateField( )
    time_start =  models.TimeField( )
    time_end   =  models.TimeField( )
    title      =  models.CharField( max_length=150 )
    text       =  models.TextField( )
    succes     =  models.TextField( )
    setback    =  models.TextField( )
    reflect    =  models.TextField( )
    last_saved =  models.DateTimeField( auto_now_add=True )
    user       =  models.ForeignKey( User, on_delete=models.CASCADE )
    is_active  =  models.SmallIntegerField( )

    def __str__(self):
        return self.title

class Settings( models.Model ):
    language  =  models.CharField( max_length=5, default='EN' )
    saved     =  models.DateTimeField( auto_now_add=True )
    user      =  models.ForeignKey( User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
