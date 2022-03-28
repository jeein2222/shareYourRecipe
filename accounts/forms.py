from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="E-MAIL")

    class Meta:
        model = User    
        fields = ("username", "password1", "password2", "email")
      

    '''
    # 오류 메시지 customization
    def clean(self):
        # 비밀번호가 6자리 이하일 때
        #username = self.cleaned_data["username"]
        password1 = self.cleaned_data['password1']
        #password2 = self.cleaned_data['password2']
        
        if len(password1) <= 8:
            raise forms.ValidationError("비밀번호는 8자리 이상이어야 합니다.")
        return password1
    
        #elif User.objects.filter(username).exists():
            #raise forms.ValidationError("이미 회원가입한 사용자입니다. 다른 아이디로 시도해주십시오.")
            
        #elif password1 != password2:
            #raise forms.ValidationError("비밀번호가 일치하지 않습니다. 다시 입력해주십시오.")
    '''
            
        
        