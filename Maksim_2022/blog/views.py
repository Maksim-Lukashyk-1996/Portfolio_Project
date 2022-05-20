from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts,
    }
    return render(request, 'blog_index.html', context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    # Создал экземпляр формы и записал в: form
    form = CommentForm()
    # затем мы проверяем, если в request, который пришёл к нам со страницы, есть метод: 'POST'
    if request.method == 'POST':
        # Тогда мы создаём экземпляр нашего класса, с данными которые пришли из: request.POST
        form = CommentForm(request.POST)
        # Проверил или наша форма валидна, всё хорошо и ошибок нет
        if form. is_valid():
            # Тогда создаём экземпляр нашего класса: comment в базу данных, чтобы записать туда данные
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            # Сохраняем нашу форму
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form
    }

    return render(request, "blog_detail.html", context)


def blog_category(request,category):
    post = Post.objects.filter(
        category__name__contains=category
    ).order_by('-created_on')
    context = {
        'post': post,
        'category': category
    }
    return render(request, "blog_category.html", context)


