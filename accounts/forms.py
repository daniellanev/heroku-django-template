from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist!")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
        return super(UserLoginForm, self).clean()
        

class UserRegisterForm(forms.ModelForm):
    
    # overiding the defualt in meta (ie adding the widget to password)
    # username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
   
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'confirm_password',
        ]
    
    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if not re.match("^[A-Za-z]*$", username):
    #         regex=r'^[a-zA-Z0-9]*$'
    
    #     return username


    # gives immediate field error compared to def clean(self): which will give an error when processing the form
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords must match!")
        return password


    