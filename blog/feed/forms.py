from django.forms import ModelForm, Textarea

from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model= Post
        widgets = {
            'content': Textarea(attrs={'cols': 60, 'rows': 40}),
        }
        fields = ['title', 'photo', 'is_published', 'content']


class CommentForm(ModelForm):
    class Meta:
        model  = Comment
        widgets = {
            'content': Textarea(attrs={'cols': 60, 'rows': 40}),
        }
        fields=['content', 'is_published', 'photo']