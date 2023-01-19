from django import forms


class CouponAddForm(forms.Form):
    code = forms.CharField()
