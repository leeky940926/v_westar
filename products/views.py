import json

from django.http import JsonResponse
from django.views import View

from products.models import *

class NutritionViews(View) :
    def post(self, request) :
        data = json.loads(request.body)
       
        nutritions = Nutrition.objects.create(
            one_serving_kcal = data['one_serving_kcal'],
            sodium_mg = data['sodium_mg'],
            saturated_fat_g = data['saturated_fat_g'],
            sugars_g = data['sugars_g'],
            protein_g = data['protein_g'],
            caffeine_mg = data['caffeine_mg'],
            size_ml = data['size_ml'],
            size_fluid_ounce = data['size_fluid_ounce']
        )
        return JsonResponse({'Message' : 'Created'}, status=201)
    
    def get(self, request) :
        nutritions = Nutrition.objects.all()
        result = []

        for nutrition in nutritions :
            result.append(
                {
                    'one_serving_kcal' : nutrition.one_serving_kcal ,
                    'sodium_mg' : nutrition.sodium_mg,
                    'saturated_fat_g' : nutrition.saturated_fat_g,
                    'sugars_g' : nutrition.sugars_g,
                    'protein_g' : nutrition.protein_g,
                    'caffeine_mg' : nutrition.caffeine_mg,
                    'size_ml' : nutrition.size_ml,
                    'size_fluid_ounce' : nutrition.size_fluid_ounce
                }
            )
        return JsonResponse({'result =':result}, status=200)

class MenusView(View) :
    def get(self, request) :
        menus = Menu.objects.all()
        result = []

        for menu in menus :
            result.append(
                {
                    'name' : menu.name
                }
            )
        return JsonResponse({'menu_result':result}, status=200)

    def post(self, request) :
        data = json.loads(request.body)
        name = Menu.objects.create(name=data['name'])

        return JsonResponse({'message':'created'}, status=201)

class CategoryView(View) :
    def get(self, request) :
        category = Category.objects.all()
      
        result = []

        for categories in category :
            result.append(
                {
                    'name' : categories.name,
                    'menu' : categories.menu_id

                }
            )
          
        return JsonResponse({'result' : result}, status=200)
    
    def post(self, request) :
        data = json.loads(request.body)
    
        Category.objects.create(name=data['name'], menu = Menu.objects.get(id=int(data['menu'])))
        
        return JsonResponse({'message' : 'created'}, status = 201)

class ProductView(View) :
    def get(self, request) :
     
        products = Product.objects.all()
        result = []

        for product in products :
            result.append(
                {
                    'category' : product.category_id,
                    'kor_name' : product.kor_name,
                    'eng_name' : product.eng_name,
                    'desc' : product.desc,
                    'nutr' : product.nutr_id
                }
            )
        return JsonResponse({'result =':result}, status=200)
    
    def post(self, request) :
        data = json.loads(request.body) 
      
        Product.objects.create(
        kor_name = data['kor_name'],
        eng_name = data['eng_name'],
        desc = data['desc'],
        category = Category.objects.get(id=int(data['category_id'])),
        nutr = Nutrition.objects.get(id=int(data['nutr_id']))
            )
        return JsonResponse({'message':'created'}, status=201)
