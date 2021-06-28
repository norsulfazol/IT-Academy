from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Author, Post

def home(request):
    print("hello")
    return render(request, 'home.html')

def posts(request, query='reverse'):
    all_posts = Post.objects.all()

    print(query)

    if query == 'reverse':
        all_posts = all_posts[::-1]

    result = '<h1>All Posts:</h1><ul>'

    viewed_posts = request.session.get('viewed_posts', {})
    print(viewed_posts)

    return render(request, 'posts.html', {'posts': all_posts, 'viewed_posts': viewed_posts})

def post(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
    except:
        return HttpResponseNotFound('Ooooops')
    
    print(type(p.id))

    viewed_posts = request.session.get('viewed_posts', {})
    viewed_posts[post_id] = post_id
    request.session['viewed_posts'] = viewed_posts
    return render(request, 'post.html', {'post': p})

def add_post(request): pass
