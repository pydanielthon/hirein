from django import forms
from allauth.account.forms import LoginForm, SignupForm



class SimpleLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(SimpleLoginForm, self).__init__(*args, **kwargs)
        # change fields
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'email',
                                                             'placeholder': 'name@example.com',
                                                             'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'type': 'password',
                                                                    'placeholder': '*************',
                                                                    'class': 'form-control'})
        # change label
        self.fields['login'].label = ''
        self.fields['password'].label = ''



class SimpleSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(SimpleSignupForm, self).__init__(*args, **kwargs)
        #change fields
        self.fields['email'].widget = forms.TextInput(attrs={'type': 'email',
                                                             'placeholder': 'name@example.com',
                                                             'class': 'form-control'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'type': 'password',
                                                                     'placeholder': '*************',
                                                                     'class': 'form-control'})
        #change labels
        self.fields['email'].label = ''
        # self.fields['email2'].label = ''
        self.fields['password1'].label = ''