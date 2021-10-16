from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    icon_code = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Faq(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Project(models.Model):
    title = models.CharField(max_length=300)
    # [(value, human readable name),....] to create a radio selection field
    types = [('web','Website'), ('app','Mobile App'), ('ml','ML/DL')]
    type_of_project = models.CharField(max_length=30, default='web', choices = types)
    description = models.TextField()
    done_by = models.CharField(max_length=50)
    bx_icon_code = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Price(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField(default=0)
    description = models.TextField()
    recommended = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=70)
    image = models.ImageField(upload_to='members/')
    description = models.TextField(null=True)
    project_details = models.TextField(null=True, blank=True)
    research_work = models.TextField(null=True, blank=True)
    mail_id = models.CharField(max_length=200, null=True)
    facebook = models.CharField(max_length=200, null=True)
    linkedin = models.CharField(max_length=200, null=True)
    whatsapp = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name

class viewMembers(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=70)
    image = models.ImageField(upload_to='members/')
    description = models.TextField(null=True)
    project_details = models.TextField(null=True, blank=True)
    research_work = models.TextField(null=True, blank=True)
    mail_id = models.CharField(max_length=200, null=True)
    facebook = models.CharField(max_length=200, null=True)
    linkedin = models.CharField(max_length=200, null=True)
    whatsapp = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name
