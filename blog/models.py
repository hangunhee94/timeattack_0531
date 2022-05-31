from django.db import models

# Create your models here.

class CategoryModel(models.Model):
    class Meta:
        db_table = "my_category"

    category = models.CharField(max_length=256)
    description = models.CharField(max_length=256, default='')

class ArticleModel(models.Model):
    class Meta:
        db_table = "my_blog"

    title = models.CharField(max_length=256)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256)
