from django.db import models

# Create your models here.
class Menu(models.Model) :
    name = models.CharField(max_length=20)

    class Meta :
        db_table = 'menus'

class Category(models.Model) :
    menu = models.ForeignKey('Menu',models.CASCADE)
    name = models.CharField(max_length=20)

    class Meta : 
        db_table = 'categories'

class Nut(models.Model) :
    one_serving_kcal = models.DecimalField(max_digits=6,decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=6,decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=6,decimal_places=2)
    sugars_g = models.DecimalField(max_digits=6,decimal_places=2)
    protein_g = models.DecimalField(max_digits=6,decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=6,decimal_places=2)
    size_ml = models.CharField(max_length=20)
    size_fluid_ounce = models.CharField(max_length=20)

    class Meta :
        db_table = 'nutritions'

class Product(models.Model) :
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    kor_name = models.CharField(max_length=20)
    eng_name = models.CharField(max_length=20)
    desc = models.TextField()
    nutr = models.OneToOneField('Nut', on_delete=models.CASCADE)

    class Meta :
        db_table = 'products'

class Images(models.Model) :
    img_url = models.CharField(max_length=2000)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta :
        db_table = 'image'

class Allergy(models.Model) :
    name = models.CharField(max_length=1000)

    class Meta :
        db_table = 'allergy'

class allergyProducts(models.Model) :
    allergy = models.OneToOneField('Allergy', on_delete=models.CASCADE)
    product = models.OneToOneField('Product', on_delete=models.CASCADE)

    class Meta :
        db_table = 'allergyProducts'