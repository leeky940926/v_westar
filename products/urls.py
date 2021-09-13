from django.urls import path
from products.views import *

urlpatterns = [
    path('menus', MenusView.as_view()),
    path('categories', CategoryView.as_view()),
    path('nutritions', NutritionViews.as_view()),
    path('product', ProductView.as_view()),
]
