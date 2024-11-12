from django.db import models

# Create your models here.

class PracticeModelForm(models.Model):
    # auto_field = models.AutoField(primary_key=True)
    # big_auto_field = models.BigAutoField(primary_key=True)
    email_field = models.EmailField()
    char_field = models.CharField(max_length=50)
    big_integer_field = models.BigIntegerField()
    boolean_field = models.BooleanField()
    binary_field = models.BinaryField()
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    duration_field = models.DurationField()
    file_field = models.FileField(upload_to='files/')
    # file_path_field = models.FilePathField(path='/path/to/files/')