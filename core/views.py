from django.views import generic
from posts.models import Post

class Home(generic.ListView):
    template_name = 'core/home.html'
    model = Post
    context_object_name = 'posts'
