from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author_anonymous", "text"]
        labels = {
            "author_anonymous": "Your Name",
            "text": "Comment",
        }
