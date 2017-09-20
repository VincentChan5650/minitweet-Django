from django import forms
from .models import Tweet

class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'Creare Your Tweet!',
                                                                    'class':'form-control'}))
    class Meta:
        model = Tweet
        fields = [
            # 'user',
            'content'
        ]
        exclude = []

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        # validation
        return content
