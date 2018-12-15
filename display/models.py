from django.db import models
import time


def photo_filename(instance, filename):
    path_construction = 'photos/' + str(time.time())
    return path_construction

# Create your models here.


class Photos(models.Model):
    photo_id = models.IntegerField(primary_key=True)
    filename_path = models.ImageField(upload_to=photo_filename, height_field=None, width_field=None, max_length=100)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)  # one user can have many photos
    win_count = models.IntegerField
    loss_count = models.IntegerField
    category_id = models.ForeignKey('Categories', on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.photo_id)


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=100)
    email = models.EmailField(max_length=100, default='')
    portfolio = models.TextField(max_length=500, default='')
    images_uploaded = models.IntegerField

    def __str__(self):
        return self.name


class Categories(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.TextField(max_length=50)

    def __str__(self):
        return self.category_name



