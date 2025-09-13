# logistics_app/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .ai_engine import calculate_eta_mock, calculate_eta_detailed
from .forms import OrderForm
from .models import Order


#def index(request):
    #return render(request, 'index.html')

def index(request):
    form = OrderForm()
    return render(request, 'index.html', {'form': form})

def predict_eta(request):
    eta = calculate_eta_mock(None)
    return HttpResponse(eta)


def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Optional: Use HTMX success response here
    else:
        form = OrderForm()
    
    return render(request, 'logistics_app/order_form.html', {'form': form})

def order_list(request):
    orders = Order.objects.all().order_by('-order_date')
    return render(request, 'logistics_app/order_list.html', {'orders': orders})