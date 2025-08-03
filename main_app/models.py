from django.db import models
from django.urls import reverse

# Create your models here.

CATEGORIES = (
    ('O', 'Other'),
    ('E', 'Entertainment'),
    ('G', 'Grocery'),
    ('H', 'Housing'),
    ('U', 'Utilities'),
    ('T', 'Transportation'),
    ('M', 'Memberships'),
    ('P', 'Personal')
    
)

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateField('Transaction Date')
    category = models.CharField(
        max_length=1,
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
    )



    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('expense-detail', kwargs={'expense_id': self.id})