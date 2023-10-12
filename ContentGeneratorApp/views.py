from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .services import generate_content_with_openai
from .forms import ArticleForm
from .forms import KeywordForm, ArticleForm

def create_article(request):
    preview_form = None
    
    if request.method == "POST":
        form = KeywordForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            title = generate_content_with_openai(f"Create a catchy and SEO-optimized unique original article title about '{keyword}'.")
            
            # Define the detailed prompt for the body
            body_prompt = f"""
            Write a comprehensive guide on the topic '{title}'. The guide should include:

            <h2>An introduction to the topic.</h2>
            <h2>A section discussing the potential benefits associated with the topic.</h2>
            <h2>A section discussing potential risks or downsides associated with the topic.</h2>
            <h2>A section on how to prepare or use the topic in a practical way.</h2>
            <h2>A section discussing alternatives if the topic is not suitable.</h2>
            <h2>A section with tips for incorporating the topic into everyday life.</h2>
            <h2>A conclusion summarizing the key points.</h2>

            The guide should be structured with headers for each section, and include lists and tables where appropriate. The content should be informative, engaging, and suitable for a general audience please add html tags, headers, strong the main keyword, lists, tables.
            """
            body = generate_content_with_openai(body_prompt)
            preview_form = ArticleForm(initial={'title': title, 'body': body})
    else:
        form = KeywordForm()

    return render(request, 'create_article.html', {'form': form, 'preview_form': preview_form})

def save_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('display_article', article_id=article.id)
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})

    
def display_article(request, article_id):
    """
    View to display a single article.
    """
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'display_article.html', {'article': article})