from django import forms

class QuestionForm(forms.Form):
    Question = forms.CharField(max_length=100)
    Choice1 = forms.CharField(max_length=100)
    Choice2 = forms.CharField(max_length=100)


class deleteForm1(forms.Form):
    Question_ID_ = forms.CharField(max_length=10)

   