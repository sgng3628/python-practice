from django import forms
from .models import Board
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

##form class
# class BoardForm(forms.Form):
#     title = forms.CharField(
#         label='Title'
#         widget=forms.TextInput(attrs={
#             'placeholder':'The title!',
            
#             })
#         )
#     content = forms.CharField(
#         label= 'Content'
#         widget=forms.Textarea(attrs={
#             'row':5,
#             'cals':50,
#             'placeholder':'Fill the Content!',
#             })
#         )
    
    
## model form
#해당 model 에 대한 정보를 메타 정보로 넣어줘서 사용.
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title','content']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', '작성합시다!'))
    
