from django.db import models
# from django.conf import settings
# from django_project import settings as my_settings

# settings.configure("django_project.settings.py", 
#                    DEBUG=True,
#                    INSTALLED_APPS=my_settings.INSTALLED_APPS)

# Create your models here.

# super user
# yking19
# Imgoingin@20

class RK_Ashram_marg(models.Model):
    
    id = models.AutoField(primary_key=True)
    Tree_code = models.CharField(max_length=8, unique=True, null=False, error_messages ={ 
                    "unique":"The Tree code you have entered is already exists."
                    } )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    common_name = models.CharField(max_length=45, null=False)
    scientific_name = models.CharField(max_length=45)
    Age = models.IntegerField(null=False)
    Height = models.FloatField(null=False)
    Diameter_girth = models.FloatField(null=False)
    closest_address = models.CharField(max_length=45, null=False)
    Longitude = models.DecimalField(max_digits=8, decimal_places=6,
                                 unique=True, null=False, 
                                 error_messages={"unique" : "Longitude value already exists"})
    Latitude = models.DecimalField(max_digits=8, decimal_places=6,
                                 unique=True, null=False, 
                                 error_messages={"unique" : "Latitude value already exists"})
    specie_code = models.CharField(max_length=8)
    condition = models.CharField(max_length=45)

    def __unicode__(self):
        return self.id

