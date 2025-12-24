from django.db import models

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('Campus', 'Campus'),
        ('Events', 'Events'),
        ('Tech', 'Tech'),
        ('Academics', 'Academics'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='articles/')
    author = models.CharField(max_length=100, default="Admin")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
