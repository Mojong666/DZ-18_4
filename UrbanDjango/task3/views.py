from django.shortcuts import render

def index_view(request):
    return render(request, 'third_task/index.html')

def shop_view(request):
    items = {
        'Игровая приставка': '30000 руб.',
        'Контроллер': '4000 руб.',
        'Игровая гарнитура': '5000 руб.'
    }
    return render(request, 'third_task/shop.html', {'items': items})

def cart_view(request):
    return render(request, 'third_task/cart.html')
