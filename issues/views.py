from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Issues, Status

# Create your views here.


class IssueListView(ListView):
    template_name = "issues/list.html"
    model = Issues


class ToDoIssueListView(ListView):
    template_name = "issues/list.html"
    model = Issues

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="To do")
        context["issues_list"] = Issues.objects.filter(status=pending_status).reverse()
        return context


class InProgressIssueListView(ListView):
    template_name = "issues/list.html"
    model = Issues

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="In progress")
        context["issues_list"] = Issues.objects.filter(status=pending_status).reverse()
        return context


class DoneIssueListView(ListView):
    template_name = "issues/list.html"
    model = Issues

    def test_func(self):
        return self.request.user.role.name in ["Agent", "Manager"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="Done")
        context["issues_list"] = Issues.objects.filter(status=pending_status).reverse()
        return context


class IssueDetailView(DetailView):
    template_name = "issues/detail.html"
    model = Issues


class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = "issues/create.html"
    model = Issues
    fields = ["title", "summary", "description"]
    exclude = ["status", "assignee"]

    def form_valid(self, form):
        form.instance.requester = self.request.user
        return super().form_valid(form)


class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/edit.html"
    model = Issues
    fields = ["title", "summary", "status", "description", "assignee"]

    def test_func(self):
        # post_obj = self.get_object()
        return self.request.user.role.name in ["Agent", "Manager"]


class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "issues/delete.html"
    model = Issues
    success_url = reverse_lazy("list")

    def test_func(self):
        # post_obj = self.get_object()
        return self.request.user.role.name in ["Agent", "Manager"]
