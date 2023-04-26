from django.db import models

# Create your models here.


class organisations(models.Model):
    VACANCIES = (
        ('0-15','few'),
        ('16-50','high'),
        ('51-100','alot'),
        ('100-1000','mass')
    )

    name = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null=True)
    package_in_LPA = models.IntegerField(max_length=200, null=True)
    experience_in_yrs = models.IntegerField(max_length=200, null=True)
    vacancies = models.CharField(max_length=200, null=True, choices=VACANCIES)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "organisations"


class registration(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    confirm_password = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "registration"