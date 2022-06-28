from django.shortcuts import render

#Загрузка основной страницы
def index(request):
    return render(request, 'main/index.html')