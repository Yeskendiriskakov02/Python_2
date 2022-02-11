from django.db import models

class Top(models.Model):
    users= models.CharField(max_length=200)
    balance = models.IntegerField()


    def __str__(self):
        return f'{self.users}-{self.balance}'

