from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Expense, Deposit

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def expense_index(request):
    expenses = Expense.objects.all()
    # render the expenses/index.html template with the expenses data
    return render(request, 'expenses/index.html', {'expenses': expenses})

def expense_detail(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    return render(request, 'expenses/detail.html', {'expense': expense})

class ExpenseCreate(CreateView):
    model = Expense
    fields = '__all__'
    
class ExpenseUpdate(UpdateView):
    model = Expense
    fields = '__all__'

class ExpenseDelete(DeleteView):
    model = Expense
    success_url = '/expenses/'

class DepositCreate(CreateView):
    model = Deposit
    fields = '__all__'

class DepositList(ListView):
    model = Deposit

class DepositDetail(DetailView):
    model = Deposit