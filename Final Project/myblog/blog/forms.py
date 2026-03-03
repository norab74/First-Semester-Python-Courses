
from django import forms
from .models import Post, CommentOnPost

# ----- Comment form -----
class BlogCommentBox(forms.ModelForm):
    class Meta:
        model = CommentOnPost
        fields = ['name', 'comment_contents']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Anonymous'
            }),
            'comment_contents': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Send me a note!'
            }),
        }

# ----- Post form (TinyMCE optional) -----
# If you want TinyMCE, keep the import; otherwise remove it and use a plain Textarea.
try:
    from tinymce.widgets import TinyMCE
    USE_TINYMCE = True
except Exception:
    USE_TINYMCE = False

class PostForm(forms.ModelForm):
    class Meta:
        model = Post                     # <-- the actual model class
        fields = ['post_title', 'post_contents']
        widgets = {
            'post_title': forms.TextInput(attrs={
                'placeholder': 'Post Title',
                'class': 'input-title',
            }),
            # Use TinyMCE if available; otherwise fallback to Textarea.
            'post_contents': TinyMCE(attrs={'cols': 80, 'rows': 20}) if USE_TINYMCE
                            else forms.Textarea(attrs={'id': 'post_contents', 'rows': 20}),
        }
