from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from app.forms import TodoForm


def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('todo_list'))
        else:
            print('Form errors: {form.errors}')
    else:
        form = TodoForm()
    return render(request, 'create.html', {'form': form})


def all_todos(request):
    return HttpResponse()