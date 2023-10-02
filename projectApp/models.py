from django.db import models

class Flower(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, default='please add description')
    meaning = models.CharField(max_length=2000, default='please add meaning')
    care_information = models.CharField(max_length=1000, default='please add care information')
    planting = models.CharField(max_length=1000, default='please add planting')
    disease = models.CharField(max_length=2000, default='please add disease')
    image = models.TextField(null=True)    # blob
    tips = models.CharField(max_length=1000, default='please add facts')

    class Meta:
        db_table = "flower"

    def __str__(self):
        return self.name


class TrainModel(models.Model):
    image_id = models.IntegerField(primary_key=True)
    image_dataset = models.TextField(null=True)    # blob
    id = models.IntegerField()

    class Meta:
        db_table = "flower_dataset"

    def __str__(self):
        return self.image_dataset