from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm


from .models import ShopUser
from django import forms




class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username','password')


    def __init__(self, *args,**kwargs):
        super (ShopUserLoginForm,self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username','password','password1','password2','email','age','avatar')


    def __init__(self, *args,**kwargs):
        super (ShopUserRegisterForm,self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Вы слишком молоды')

        return data

class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('username','first_name','email','age','password')


    def __init__(self, *args,**kwargs):
        super(ShopUserEditForm,self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError('Вы слишком молоды')

        return data