from django.db import models
from django.contrib.auth.models import User

TYPE = (
    ("Positive",'Positive'),
    ('Negative','Negative')
    )

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=100)
    Expense_type = models.CharField(max_length=8, choices=TYPE)
    amount = models.FloatField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    income = models.FloatField()
    expenses = models.FloatField(blank=True,default=0)
    balance = models.FloatField(blank=True,null=True)