from django import http
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class BlogListView(ListView):
    model = Post
    template_name = 'blogging/list.html'
    queryset = Post.objects.exclude(published_date__isnull=True).order_by('-published_date')

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")

def list_view(request):
    filtered_posts =  Post.objects.exclude(published_date__isnull=True)
    context = {
        'posts': filtered_posts,
        'empty': len(filtered_posts)
        }
    return render(request, 'blogging/list.html', context)

def detail_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        if(post.published_date == None):
            raise Http404
    except Post.DoesNotExist:
        raise Http404

    context = {'post': post}
    return render(request, 'blogging/detail.html', context)