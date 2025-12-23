from django.shortcuts import render, get_object_or_404
from .models import Article


def home(request):
    """Home page showing list of all articles."""
    articles = Article.objects.all().order_by("-created_at")
    return render(request, "home.html", {"articles": articles})


def detail(request, pk):
    """Detail page for a single article."""
    article = get_object_or_404(Article, pk=pk)
    return render(request, "detail.html", {"article": article})