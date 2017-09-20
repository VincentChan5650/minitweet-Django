from django import forms

class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=120)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label = 'Confirm Password')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password')

        if password != password2:
            raise forms.ValidationError("Password must be matched!")
        return password2
