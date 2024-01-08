from django.db import models

class meeting (models.Model):
    Serial= models.IntegerField(null=True)
    Subject=models.CharField(max_length=122)
    Format=models.CharField(max_length=122)
    Link=models.URLField(null=True, blank = True)
    Date=models.DateField(null=True)
    def __str__(self):
        return f"{self.Serial}:{self.Subject}"

class ugSenator(models.Model):
    Name=models.CharField(max_length=50)
    Position=models.CharField(max_length=50)
    Email=models.CharField(max_length=50,null=True)
    Phone_No=models.CharField(max_length=10,null=True)
    Image=models.ImageField(upload_to='ugsenetor/')
    def __str__(self):
       return f"{self.Name}:{self.Position}"
class pgSenator(models.Model):
    Name=models.CharField(max_length=50)
    Position=models.CharField(max_length=50)
    Email=models.CharField(max_length=50,null=True)
    Phone_No=models.CharField(max_length=10,null=True)
    Image=models.ImageField(upload_to='pgsenetor/', height_field=None, width_field=None, max_length=100)

    def __str__(self):
       return f"{self.Name}:{self.Position}"


class facultyExecutivebodie(models.Model):
    Name=models.CharField(max_length=50)
    Position=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Phone_No=models.CharField(max_length=10)
    Image=models.ImageField(upload_to='facultyexective/', height_field=None, width_field=None, max_length=100)
    def __str__(self):
       return f"{self.Name}:{self.Position}"

class studentExecutivebodie(models.Model):
    Name=models.CharField(max_length=50)
    Position=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Phone_No=models.CharField(max_length=10)
    Image=models.ImageField(upload_to='studentexective/', height_field=None, width_field=None, max_length=100)

    def __str__(self):
       return f"{self.Name}:{self.Position}"                    

class upcomingEvent(models.Model):
    Date=models.DateField(null=True)
    Description=models.CharField(max_length=500)
    Image=models.ImageField(upload_to='events/', height_field=None, width_field=None, max_length=100)
    Link=models.URLField(null=True, blank = True)


    def __str__(self):
       return self.Description                     
   