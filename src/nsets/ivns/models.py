
# Create your models here.
from django.db import models
#from django.db.models import FloatField
from django.forms import ModelForm
from django import forms

class Input(models.Model):
    textA = '<[.1,.5],[.3,.4],[.2,.5]>  <[.3,.4],[.2,.6],[.2,.4]>\n<[.2,.3],[.1,.3],[.4,.7]>  <[.1,.7],[.3,.4],[.5,.6]>\n<[.4,.5],[.2,.3],[.1,.3]>  <[.5,.8],[.1,.2],[.4,.7]>\n<[.5,.6],[.3,.4],[.4,.5]>  <[.2,.5],[.4,.6],[.3,.8]>'
    textB = '<[.3,.4],[.2,.6],[.1,.3]>  <[.4,.6],[.3,.4],[.3,.5]>\n<[.4,.7],[.2,.6],[.4,.5]>  <[.2,.3],[.3,.4],[.4,.7]>\n<[.1,.3],[.2,.4],[.2,.3]>  <[.2,.6],[.3,.5],[.3,.6]>\n<[.3,.4],[.2,.3],[.3,.5]>  <[.1,.2],[.1,.4],[.2,.6]>'
    A = models.TextField(default=textA)
    B = models.TextField(default=textB)
    productScalar= models.FloatField(default=1)
    #dScalar= models.FloatField(default=1)

    #powerScalar = models.FloatField(default=1)


class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = '__all__'
        widgets = {
            'A': forms.Textarea(attrs={'rows': 8, 'cols': 80}),
            'B': forms.Textarea(attrs={'rows': 8, 'cols': 80}),

        }

class InputNorm(models.Model):
    text = '<[.1,.5],[.3,.4],[.2,.5]>  <[.3,.4],[.2,.6],[.2,.4]>\n<[.2,.3],[.1,.3],[.4,.7]>  <[.1,.7],[.3,.4],[.5,.6]>\n<[.4,.5],[.2,.3],[.1,.3]>  <[.5,.8],[.1,.2],[.4,.7]>\n<[.5,.6],[.3,.4],[.4,.5]>  <[.2,.5],[.4,.6],[.3,.8]>'
    matrix = models.TextField(default=text)
    beneficial=models.BooleanField(default=True)

class InputNormForm(ModelForm):
    class Meta:
        model = InputNorm
        fields = '__all__'
        widgets = {
            'matrix': forms.Textarea(attrs={'rows': 8, 'cols': 120}),
        }


