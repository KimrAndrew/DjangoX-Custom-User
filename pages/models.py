from django.db import models
from django.db.models.fields.related import ForeignKey
from django.urls import reverse_lazy

# Create your models here.
# class Snack(models.Model):
#     title = models.CharField(max_length=64)
#     purchaser = ForeignKey(get_user_model(), on_delete=models.CASCADE)
#     description = models.CharField(max_length=256)
#     def __str__(self):
#         return self.title
    
#     def get_absolute_url(self):
#         return reverse_lazy('snack_detail',args=[str(self.id)])