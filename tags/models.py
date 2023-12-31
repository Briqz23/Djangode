from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType #permite generic relationships
from django.contrib.contenttypes.models import GenericForeignKey #permite generic relationships


class LikedItem():
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
# Create your models here. 
class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    #x tag aplicada a y objeto
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
