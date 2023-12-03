from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, View, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from datetime import datetime, date,timedelta


class SignUp(CreateView):
    """ this is a signup class """    
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')    
    
    def form_valid(self, form):
        """ since username is email, user email automatically defined  """
        response = super().form_valid(form)
        user = self.object           
        user.email = user.username
        user.save()
        return response

class Login(LoginView):
    """ login class mad based on login view """
    template_name = 'login.html'
    authetication_form = AuthenticationForm
    next_page = 'todolist'

class Logout(LogoutView):
    next_page = 'login'
        
class TodolistView(View):
    """ DetailView class was not implemented since each user has its own tasks """
    def get(self, request):
        todo = Todolist.objects.filter(user=request.user.id)
        todo_list = list(todo.values())
        current_date = date.today()
        
        for each in todo_list:
            left_days = (each['due_date'] - current_date)
            each['left_days'] = left_days.days
            category = Category.objects.get(id=each['category_id'])
            each['category_id']=category.name
            
        print(type(left_days))
        paginator = Paginator(todo_list, 4)
        if 'page' in request.GET:
            page_num = request.GET['page']
        else:
            page_num = 1
        page = paginator.get_page(page_num)
        
        context = {'page':page}
        return render(request, 'todolist.html', context)

class TodoCreateView(View):
    """ CreateView class was not implemented since each user has its own tasks """
    def get(self, request):
        form= TodoCreateForm()        
        context = {'form': form}
        return render(request, 'todocreate.html', context)
    
    def post(self, request):
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            due_date = form.cleaned_data['due_date']
            category = form.cleaned_data['category']
            user = User.objects.get(id=request.user.id)
            Todolist.objects.create(title = title, content = content, due_date = due_date, category = category, user = user)            
            return redirect('todolist')
        else:
            return render(request, 'todocreate.html', {'form':form})
        
class CategoryCreateView(CreateView):
    """ Category can be inserted only by the user with superuser access """    
    model = Category
    template_name = 'categorycreate.html'
    form_class = CategoryCreateForm
    success_url = reverse_lazy('categorycreate') 

class TodoDetailView(View):
    """ DetailView class was not implemented since each user has its own tasks """
    def get(self, request, pk):
        todo = Todolist.objects.get(user=request.user.id, pk=pk)
        context = {'info':todo}
        return render(request, 'detail.html', context)

    def post(self, request, pk):
        todo = Todolist.objects.get(user=request.user.id, pk=pk)
        todo.status = True
        todo.save()
        return redirect('todolist')

class TodoDeleteView(DeleteView):
    model = Todolist
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('todolist')
    
class TodoUpdatelView(UpdateView):
    model = Todolist
    form_class = TodoCreateForm
    template_name = 'update.html'
    success_url = reverse_lazy('todolist')
