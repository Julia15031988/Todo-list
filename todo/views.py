from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Task, Tag
from .forms import TaskForm


class TodoListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "todo/todo_list.html"  # виправлено
    context_object_name = "task_list"
    paginate_by = 10


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:todo-list")  # виправлено


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:todo-list")  # виправлено


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:todo-list")  # виправлено


def switch_done_or_not_done(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:todo-list"))  # виправлено


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"  # виправлено
    context_object_name = "tag_list"


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")  # виправлено


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")  # виправлено


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
