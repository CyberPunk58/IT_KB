from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

menu = ["Login", "Отправка картриджей"]

menu = [
    {'title': 'Login', 'url_name': 'login'},
    {'title': 'Cartridges', 'url_name': 'cartridges'},

]

data_db = [
    {'id': 1, 'title': 'OpenOffice_4.1.15_Win_x86', 'content': 'Здесь будет дистрибутив офиса', 'is_published': True},
    {'id': 2, 'title': 'Chrome', 'content': 'Здесь будет дистрибутив Chrome', 'is_published': True},
    {'id': 3, 'title': '7z', 'content': 'Здесь будет дистрибутив 7z', 'is_published': True},

]

def index(request):
    data = {
        'title': "Главная страница",
        'menu':menu,
        'posts': data_db,
    }
    return render(request, 'main/index.html', context=data)

def login(request):
    data = {'title': "Login"}
    return render(request, 'main/login.html', data)

def about(request):
    return HttpResponse('Home page')

def login(request, post_id):
    return HttpResponse("Форма для логина")

def cartridges (request, post_id):
    return HttpResponse("Форма для отправки картриджей")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")