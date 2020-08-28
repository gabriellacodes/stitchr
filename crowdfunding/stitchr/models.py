from django.db import models
from django.contrib.auth import get_user_model

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    category = models.CharField(max_length=100)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    
    # ACTION: how to capture gender and size selection best?
    # gender_choice = (
    #     ('M', 'Mens'),
    #     ('F', 'Womens'),
    # )
    # gender_selection = models.CharField(max_length=1, choices = gender_choice)
    # size_choice = (
    #     ('XXS','Extra extra small'),
    #     ('XS','Extra small'),
    #     ('S','Small'),
    #     ('M','Medium'),
    #     ('L','Large'),
    #     ('XL','Extra large'),
    #     ('XXL','Extra extra large'),
    #     )
    # size_selection = models.CharField(max_length=3, choices = size_choice)

class Likes(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='likes'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_likes'
    )