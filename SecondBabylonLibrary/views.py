from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from urllib import request
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import Books.models

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/main"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/login")


def index(request):
    return render(request, 'main.html')

def books_searching(request):
    return render(request, 'books_searching.html')

def borrowed_books(request):
    return render(request, 'borrowed_books.html')

def reading_book(request):
    return render(request, 'reading_book.html')

def registration(request):
    return render(request, 'registration.html')

def read(request, reading_id):
    reading = Books.models.ReadingList.objects.get(pk=reading_id)
    book = Books.models.Book.objects.get(pk=reading.book_id.id)
    return render(request, 'read.html', {'book': book, 'last_page': reading.last_page, 'reading_id': reading.id})

@csrf_exempt
def ajax(request):
    message = ""
    if request.is_ajax():
        if request.method == 'POST':
            reading_id = int(request.POST.get('reading_id', None))
            print(reading_id)
            new_last_page = int(request.POST.get('new_last_page', None))
            print(new_last_page)
            reading = Books.models.ReadingList.objects.get(pk=reading_id)
            reading.last_page = new_last_page
            reading.save()
    return HttpResponse(message)