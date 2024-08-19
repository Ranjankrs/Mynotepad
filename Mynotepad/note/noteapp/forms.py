from django.forms import ModelForm

from noteapp.models import NOTE
class NOTEForm(ModelForm):
    class Meta:
        model = NOTE
        fields = ['title' ,'description']