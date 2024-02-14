from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    naziv = models.CharField(max_length=255)

    class Meta:
        ordering = ('naziv',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.naziv
    
class Item(models.Model):
    kategorija = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    naziv = models.CharField(max_length=255)
    opis = models.TextField(blank=True, null=True)
    cijena = models.FloatField()
    slika = models.ImageField(upload_to='item_images', blank=True, null=True)
    #dostupno = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv
    
    def liked_by(self, user):
        if isinstance(user, User):
            return user.like_set.filter(item=self).count() > 0
        else:
            return False
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)