from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('expenses/', views.expense_index, name='expense-index'),
    path('expenses/<int:expense_id>/', views.expense_detail, name='expense-detail'),
    path('expenses/create/', views.ExpenseCreate.as_view(), name='expense-create'),
    path('expenses/<int:pk>/update/', views.ExpenseUpdate.as_view(), name='expense-update'),
    path('expenses/<int:pk>/delete/', views.ExpenseDelete.as_view(), name='expense-delete'),

]



