from django.db import models

# Create your models here.
# yourapp/models.py

class Student(models.Model):
    name = models.CharField(max_length=100)
    year_choices = [
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
        ('4', '4th Year'),
    ]
    year = models.CharField(max_length=1, choices=year_choices)
    question_papers_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.get_year_display()}"
