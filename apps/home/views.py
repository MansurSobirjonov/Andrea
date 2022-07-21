from django.shortcuts import render
from .forms import CommentForm
from .models import Post, Tag, Category
from apps.contact.models import Subscribe


def home(request):
    posts = Post.objects.order_by('-id')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    search = request.GET.get('search')
    sbb = request.GET.get('sbb')
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    q = request.GET.get('q')
    if search:
        posts = posts.filter(title__icontains=search)
    if sbb:
        Subscribe.objects.create(email=sbb)
    if tag:
        posts = posts.filter(tags__tag__exact=tag)
    if cat:
        posts = posts.filter(category__title__exact=cat)
    if q:
        posts = Post.objects.filter(author_name=q)
    context = {
        'objects': posts,
        'tags': tags,
        'categories': categories,
        'last_3_posts': posts[:3]

    }

    return render(request, 'index.html', context)


# def home(request):
#     posts = Post.objects.order_by('-id')
#     s = request.GET.get('s')
#     if s:
#         posts = posts.filter(title__icontains=s)
#     t = request.GET.get('t')
#     if t:
#         posts = posts.filter(tags__tag__exact=t)
#     c = request.GET.get('c')
#     if c:
#         posts = posts.filter(category__category__exact=c)
#     email = request.GET.get('email')
#     if email:
#         Subscribe.objects.create(email=email)
#     ctx = {
#         'posts': posts
#     }
#     return render(request, 'index.html', ctx)


def blog_single(request, pk):
    post = Post.objects.get(id=pk)
    form = CommentForm(request.POST or None, request.FILES)
    if form.is_valid():
        commit = form.save(commit=False)
        commit.post = post
        commit.save()
    ctx = {
        'objects': post,
        'form': form,
    }
    return render(request, 'single.html', ctx)


def fashion(request):
    posts = Post.objects.filter(type=0).order_by('-id')
    ctx = {
        'objects': posts
    }
    return render(request, 'fashion.html', ctx)


def travel(request):
    posts = Post.objects.filter(type=1).order_by('-id')
    tags = Tag.objects.all()
    categories = Category.objects.all()

    ctx = {
        'objects': posts,
        'categories': categories,
        'tags': tags,
        'last_3_posts': posts[:3]
    }
    return render(request, 'travel.html', ctx)
