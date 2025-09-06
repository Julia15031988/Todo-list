from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Task, Tag
from .forms import TaskForm


class TodoListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "todo_service/todo_list.html"
    context_object_name = "task_list"
    paginate_by = 10


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_service/task_form.html"
    success_url = reverse_lazy("todo:todo-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_service/task_form.html"
    success_url = reverse_lazy("todo:todo-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = "todo_service/task_confirm_delete.html"
    success_url = reverse_lazy("todo_:todo-list")


def switch_done_or_not_done(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:todo-list"))


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    template_name = "todo_service/tag_list.html"
    context_object_name = "tag_list"


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "todo_service/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "todo_service/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    template_name = "todo_service/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")
