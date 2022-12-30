from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterationForm(UserCreationForm):
  #  email = forms.EmailField()
    
   # class meta:
    #    model = User   #the model that will be affected ( when form.save() executed, it will save data to user model)
     #   fields= ['username', 'email','password1', 'password2']  # Fields that will have and in what order

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

#update username and password
class UserUpdateForm(forms.ModelForm):
      email = forms.EmailField()

      class Meta:
            model = User
            fields = ['username', 'email']
      
class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['image']