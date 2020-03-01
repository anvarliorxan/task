from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(label ='Username')
    password = forms.CharField(label ='Password',widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label ='Email')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    confirm = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)


    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password and confirm and password != confirm:
            raise forms.ValidationError('Parollar uygun gelmir')

        values = {
            'username':username,
            'password':password,
            'email':email,
        }
        return values

            
