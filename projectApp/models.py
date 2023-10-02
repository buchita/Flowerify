from django.db import models
# from django.db import ModelForm, Textarea


class Flower(models.Model):
    # id = models.CharField(max_length=3)
    # description = models.CharField(max_length=100)
    caption = models.CharField(max_length=100, default='')
    flowerName = models.CharField(max_length=100)
    # id = models.IntegerField(default=0)
    img = models.ImageField(upload_to='images/', default='')
    # def __init__(self):
    #     return self.description

    class Meta:
        db_table = "image"

    def __str__(self):
        #return self.description

        return self.flowerName