from django import http
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from blogging.models import Post
from blogging.forms import PostForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class BlogListView(ListView):
    model = Post
    template_name = "blogging/list.html"
    queryset = Post.objects.exclude(published_date__isnull=True).order_by(
        "-published_date"
    )


class BlogDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"
    queryset = Post.objects.exclude(published_date__isnull=True).order_by(
        "-published_date"
    )
    def post(self, request, *args, **kwargs):
        post_form = self.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
        

        context = {"object": post_form}
        return render(request, "polling/detail.html", context)

def add_post(request):
        post_form = self.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")
