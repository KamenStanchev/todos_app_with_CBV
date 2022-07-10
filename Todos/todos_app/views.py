from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, View, CreateView, DetailView, UpdateView
from .models import Todo


class TodoList(View):
    template_name = 'todo_list.html'

    def get(self, request, *args, **kwargs):
        object_list = Todo.objects.filter(is_done=False)
        return render(request, self.template_name, {'object_list': object_list})

    def post(self, request, *args, **kwargs):
        description = request.POST.get('description')

        if description:
            Todo.objects.create(description=description)
        return redirect('todo_list')


class TodoDetail(DetailView):
    model = Todo
    template_name = 'todo_detail.html'
    # context_object_name = 'todo'
    #
    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(**kwargs)
    #     ctx['ingredients'] = Todo.objects.filter(todo=self.get_object().pk)
    #     return ctx



class TodoUpdate(UpdateView):
    model = Todo
    fields = ['is_done']

    def get_success_url(self):
        return reverse('todo_detail', kwargs={'pk': self.object.pk})