from django.forms import ModelForm
from .models import BaiViet


class PostForm(ModelForm):
    class Meta:
        model = BaiViet
        fields = ['title', 'content']
