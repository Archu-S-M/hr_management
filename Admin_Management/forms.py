from django import forms


# Login form

class LoginForm(forms.Form):
    admin_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Admin Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                 'placeholder': 'Password'}))
