from django import forms

class SendForm(forms.Form):
      subject=forms.CharField(max_length=200)
      message=forms.CharField(widget=forms.Textarea)
      email =forms.EmailField()
