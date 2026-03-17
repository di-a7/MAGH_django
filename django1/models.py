from django.db import models

# Create your models here.
class Todolist(models.Model):
   title = models.CharField(max_length=100)
   description = models.TextField()
   status = models.BooleanField(default=False,null=True, blank=True)

# models.py -> migration_file -> database_table
# create_class  makemigrations     migrate
# select * from django1_todolist 