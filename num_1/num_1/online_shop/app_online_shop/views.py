from django.shortcuts import render, redirect
# подключаем объект для выполнения http-запросов
from django.http import HttpResponse
from .models import OnlineShop
from .forms import AdvertisementForm
from django.urls import reverse

# Create your views here.

# функция, отображающая файл index.html
def index(request):
    # выгружаем все объекты из нашей БД
    online_shops = OnlineShop.objects.all()
    # создаем контекст шаблона
    context = {'online_shops': online_shops}
    return render(request, 'app_advertisement/index.html', context)

# функция, отображающая файл top-sellers.html
def top_sellers(request):
    return render(request, 'app_advertisement/top-sellers.html')

# функция для отображения формы объявления на сайте
def advertisment_post(request):
    # проверка, что обрабатывается POST-запрос
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        # проверка на валидность объекта form
        if form.is_valid():
            advertisement = OnlineShop(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form':form}
    return render(request, 'app_advertisement/advertisement-post.html', context)

def advertisment(request):
    return render(request, 'app_advertisement/advertisement.html')

def login(request):
    return render(request, 'app_auth/login.html')

def profile(request):
    return render(request, 'app_auth/profile.html')

def register(request):
    return render(request, 'app_auth/register.html')