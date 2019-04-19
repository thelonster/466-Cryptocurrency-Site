from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegister(UserCreationForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=True)

    class Meta(): 
        model = User
        fields = ('username','email', 'password1', 'password2')
        help_texts = {'username': None, 'password1': None, 'password2': None}
    
    #def save(self, commit=True):
     #   user = super(UserRegister, self).save(commit=False)
      #  user.username = self.cleaned_data['username']
       # user.email = self.cleaned_data['email']

        #if commit:
            #user.save()
        
       # return user