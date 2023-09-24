from django import forms

class ModeratorForm(forms.Form):
    category=forms.ChoiceField(choices=[('sports','SPORTS'),('nature','NATURE'),('ourcollege','OURCOLLEGE'),('technology','TECHNOLOGY')],label="Category:")
    moderator_name=forms.CharField(label="Moderator Name:")
    userid=forms.IntegerField(label="User ID:")
    password=forms.CharField(label="Password",widget=forms.PasswordInput)
    mobile_num=forms.IntegerField(label="Mobile number:")
    email_id=forms.EmailField(label="Email ID:")
