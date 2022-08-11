from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length= 50)
    date = models.DateField()
    desc = models.TextField()
    img = models.ImageField(upload_to='images/')

def __str__(self):
    return self.title


class Libraray(models.Model):
    genre_choice = (
    ("Science", "Science"),
    ("Languages", "Languages"),
    ("Children Literature", "Children Literature"),
    ("Magazines", "Magazines"),
 
)
    genre = models.CharField(max_length=20, choices = genre_choice, default='Children Literature')
    title = models.CharField(max_length=20)
    file = models.FileField(upload_to='uploads/', max_length=254)

    def __str__(self):
        return self.title
