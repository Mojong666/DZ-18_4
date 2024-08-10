from django.shortcuts import render

# Функциональное представление для шаблона function_template.html
def function_view(request):
    return render(request, 'second_task/function_template.html')

# Функциональное представление для шаблона class_template.html
def class_view(request):
    return render(request, 'second_task/class_template.html')

