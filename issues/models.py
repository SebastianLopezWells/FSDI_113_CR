from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

#from symbol import return_stmt


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Issues(models.Model):
    title = models.CharField(max_length=256)
    summary = models.CharField(max_length=512)
    description = models.TextField()
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        default = 1
    )
    requester = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name = "requester"
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE, 
        blank=True, null=True,  
        related_name = "assignee",
        default = 1
    )
    
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
