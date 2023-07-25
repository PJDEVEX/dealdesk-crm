from django.shortcuts import render, get_list_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import TaskManager
from .forms import TaskManagerFilterForm, TaskManagerForm


@method_decorator(login_required, name='dispatch')
class TaskListView(ListView):
    """
    View class for listing tasks.
    """
    model = TaskManager
    template_name = 'task_manager/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        """
        Get the queryset of tasks based on the filter parameters.
        """
        queryset = super().get_queryset()
        form = TaskManagerFilterForm(self.request.GET)
        if form.is_valid():
            status = form.cleaned_data['status']
            priority = form.cleaned_data['priority']
            assigned_to = form.cleaned_data['assigned_to']
            if status:
                queryset = queryset.filter(status=status)
            if priority:
                queryset = queryset.filter(priority=priority)
            if assigned_to:
                queryset = queryset.filter(assigned_to=assigned_to)
        return queryset

    def get_context_data(self, **kwargs):
        """
        Add context data for rendering the template.
        """
        context = super().get_context_data(**kwargs)
        context['filter_form'] = TaskManagerFilterForm(self.request.GET)
        context['task'] = TaskManager.objects.first()
        return context


@method_decorator(login_required, name='dispatch')
class TaskCreateView(CreateView):
    """
    View class for creating a new task.
    """
    model = TaskManager
    form_class = TaskManagerForm
    template_name = 'task_manager/task_create.html'
    success_url = reverse_lazy('task_manager:task_list')

    def form_invalid(self, form):
        """
        Handle form validation errors and add styling to invalid fields.
        """
        for field in form.errors:
            form[field].field.widget.attrs['class'] += ' is-invalid'
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        """
        Handle form validation when the form is valid.
        """
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class TaskUpdateView(UpdateView):
    """
    View class for updating a task.
    """
    model = TaskManager
    form_class = TaskManagerForm
    template_name = 'task_manager/task_edit.html'
    success_url = reverse_lazy('task_manager:task_list')

    def form_invalid(self, form):
        """
        Handle form validation errors and add styling to invalid fields.
        """
        for field in form.errors:
            form[field].field.widget.attrs['class'] += ' is-invalid'
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        """
        Handle form validation when the form is valid.
        """
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class TaskDeleteView(DeleteView):
    """
    View class for deleting a task.
    """
    model = TaskManager
    template_name = 'task_manager/task_delete.html'
    success_url = reverse_lazy('task_manager:task_list')
