from django.urls import path, include
from . import views
urlpatterns = [
    path('get/categories/', views.get_category, name='get_category'),
    path('get/category/', views.get_category, name='get_category'),
    path('get/expenses/category/', views.get_expenses_category, name='get_expenses_category'),
    path('get/income/category/', views.get_income_category, name='get_income_category'),
    path('get/balance/', views.get_balance, name='get_balance'),    
    path('get/currency/', views.get_currency, name='get_currency'),
    path('get/accounts/', views.get_accounts, name='get_accounts'),
    path('get/account/<int:account_id>/', views.get_account, name='get_account'),
    path('delete/account/<int:account_id>/', views.delete_account, name='delete_account'),
    path('get/expenses/subcategory/', views.get_expenses_sub_category, name='get_expenses_sub_category'),   
    path('get/income/subcategory/', views.get_income_sub_category, name='get_income_sub_category'),   
    path('add/balance/', views.add_balance, name='add_balance'),
    path('add/currency/', views.add_currency, name='add_currency'),
    path('add/account/', views.add_account, name='add_account'),    
    path('add/categories/', views.add_category, name='add_category'),
    path('add/category/', views.add_category, name='add_category'),
    path('add/income/category/', views.add_income_category, name='add_income_category'),
    path('add/expenses/category/', views.add_expenses_category, name='add_expenses_category'),       
    path('add/income/subcategory/', views.add_income_sub_category, name='add_income_sub_category'),
    path('add/expenses/subcategory/', views.add_expenses_sub_category, name='add_expenses_sub_category'),   
 	path('add/income/',views.add_income, name='add_income'),
 	path('get/income/',views.get_income, name='get_income'), 	
 	path('add/expenses/',views.add_expenses, name='add_expenses'),
 	path('get/expenses/',views.get_expenses, name='get_expenses'),
 	path('get/full/',views.get_full, name='get_full'),
]