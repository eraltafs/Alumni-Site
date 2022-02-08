from django.db import models

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

# Create your models here.


class Registration(models.Model):
    name = models.CharField(max_length=122)
    passout = models.CharField(max_length=122, null=True)
    receipt = models.CharField(max_length=122, null=True)
    branch = models.CharField(max_length=122, null=True)
    email = models.CharField(max_length=122)
    phone1 = models.CharField(max_length=12, null=True)
    phone2 = models.CharField(max_length=12, null=True)
    birthday = models.DateField(null=True)
    profession = models.CharField(max_length=122, null=True)
    address1 = models.TextField(null=True)
    phone3 = models.CharField(max_length=12, null=True)
    address2 = models.TextField(null=True)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.name}-{self.branch}-{self.passout}"


class Story(models.Model):
    name = models.CharField(max_length=122)
    passout = models.CharField(max_length=122, null=True)

    branch = models.CharField(max_length=122, null=True)
    email = models.CharField(max_length=122)
    phone1 = models.CharField(max_length=12, null=True)
    phone2 = models.CharField(max_length=12, null=True)
    birthday = models.DateField(null=True)
    profession = models.CharField(max_length=122, null=True)
    address1 = models.TextField(null=True)
    phone3 = models.CharField(max_length=12, null=True)
    address2 = models.TextField(null=True)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.name}-{self.branch}-{self.passout}"


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Registered(models.Model):
    passout = models.CharField(max_length=122, null=True)
    branch = models.CharField(max_length=122, null=True)
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    address_work = models.TextField(null=True)
    permanent_address = models.TextField(null=True)
    def __str__(self):
        return f"{self.name}-{self.branch}-{self.passout}"