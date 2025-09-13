# logistics_app/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .ai_engine import calculate_eta_mock, calculate_eta_detailed
from django.shortcuts import get_object_or_404
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

from .ai_engine import calculate_eta_mock

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.eta = calculate_eta_mock(order)  # generate ETA
            order.save()
            return redirect('/orders/')
    else:
        form = OrderForm()
    
    return render(request, 'logistics_app/order_form.html', {
    'form': form,
    'is_update': False,  # 👈 flag for create mode
})


# Update list view to show orders
def order_list(request):
    orders = Order.objects.all().order_by('-order_date')
    return render(request, 'logistics_app/order_list.html', {'orders': orders})


# Update Order
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order, read_only=True)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order, read_only=True)
    return render(request, 'logistics_app/order_form.html', {
        'form': form,
        'is_update': True,   # 👈 flag to distinguish edit mode
    })

# Delete Order
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/orders/')
    return render(request, 'logistics_app/order_confirm_delete.html', {'order': order})
