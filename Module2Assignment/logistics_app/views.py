# logistics_app/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .ai_engine import calculate_eta_mock, calculate_eta_detailed
from .forms import OrderForm


def index(request):
    return render(request, 'index.html')


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
