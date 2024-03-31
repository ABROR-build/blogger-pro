from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from . import models

class ArticleListView(ListView):
    model = models.Article
    template_name = "article_list.html"

class ArticleDetailView(DetailView):
    model = models.Article
    template_name = "article_detail.html"

class ArticleUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = models.Article
    fields = ("title", "summary", "text", "image")
    template_name = "article_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = models.Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    template_name = "article_new.html"
    fields = ("title", "summary", "text", "image")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy("article_list")