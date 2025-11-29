from django.db import models
class MyStudent(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=10)
    middle_name = models.CharField(null=True,blank=True)
    last_name = models.CharField(max_length=10)
    email = models.CharField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['first_name']
        db_table = 'students'
    def __str__(self):
        return f"{self.first_name} ({self.email})"

class Teachers(models.Model):
    tr_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=10)
    second_name = models.CharField(max_length=10)
    department = models.CharField(max_length=10)
    email = models.CharField(unique=True)

    class Meta:
        ordering = ['first_name']
        db_table = 'teachers'
    def __str__(self):
        return f"{self.first_name} ({self.email})"

# Create your models here.
