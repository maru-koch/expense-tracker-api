from django.db import models
from authentication.models import User

class Expense(models.Model):

    CATEGORY_TYPE = [
        ('ONLINE_SERVICES', 'Online_Services'),
        ('TRAVEL', 'Travel'),
        ('FOOD', 'Food'),
        ('OTHER', 'Other'),
    ]

    category = models.CharField(choices = CATEGORY_TYPE, max_length=200)
    amount = models.DecimalField(decimal_places= 2, max_digits=10)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField(null = False, blank = False)
