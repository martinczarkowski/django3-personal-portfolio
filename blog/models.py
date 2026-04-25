from django.db import models


class Blog(models.Model):
    LANGUAGE_CHOICES = [('en', 'English'), ('cs', 'Czech')]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now=False, auto_now_add=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='en')

    def __str__(self):
        return f'[{self.language.upper()}] {self.title}'
