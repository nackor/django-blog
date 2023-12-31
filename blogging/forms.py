from django import forms
from blogging.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("title","text",'published_date')