from django import forms
from .models import *


class productform(forms.ModelForm):
    class Meta:
        model=frame_orders
        fields=['user','frame_name','name','email','phone','img']

class galleryform(forms.ModelForm):
    class Meta:
        model=gallery
        fields=['image']

class pro(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']


class designform(forms.ModelForm):
    class Meta:
        model=designs
        fields=['name','phone','your','model','explain']
class addform(forms.ModelForm):
    class Meta:
        model=addframe
        fields='__all__'
class bookingform(forms.ModelForm):
    class Meta:
        model=bookings
        fields=['name','phone','event','date','place','amount','time','status','message']
