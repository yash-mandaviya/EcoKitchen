from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('food_items/', views.food_item_list, name='food_item_list'),
    path('fooditem/update/<int:pk>/', views.FoodItemUpdateView.as_view(), name='food_item_update'),
    path('fooditem/delete/<int:pk>/', views.FoodItemDeleteView.as_view(), name='food_item_delete'),
    path('add_food_item/', views.add_food_item, name='add_food_item'),
    path('food-item/<int:item_id>/', views.food_item_details, name='food_item_details'),
    path('recipes/', views.recipes, name='recipes'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('delete_recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('recipes/detail/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('export_food_items/', views.export_food_items, name='export_food_items'),
    path('user_history/', views.user_history, name='user_history'),
    path('unregistered/', views.unregistered, name='unregistered'),
    path('unregistered/recipes',views.unregistered_recipe, name='unregistered_recipe'),
    path("unregistered/recipes/<int:recipe_id>/", views.unregistered_recipe_detail, name="unregistered_recipe_detail"),
    path('add-selected-recipes/', views.add_selected_recipes, name='add_selected_recipes')
]
