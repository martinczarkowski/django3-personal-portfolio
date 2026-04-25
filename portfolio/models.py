from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/', height_field=None, width_field=None, max_length=None)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Messages(models.Model):
    created = models.DateField(auto_now_add=True)
    subject = models.CharField(max_length=250)
    message = models.TextField(blank=True)
    from_email = models.CharField(max_length=250)
    
    def __str__(self):
        return self.subject
    

