from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  #Retrieves the logged in user
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'placeholder': 'Title of the post'})
        self.fields['content'].widget.attrs.update({'placeholder': 'Content of the post'})

    def save(self, commit=True):
        post = super().save(commit=False)
        if self.user:
            post.author = self.user  # Automatically associates the author
        if commit:
            post.save()
        return post
