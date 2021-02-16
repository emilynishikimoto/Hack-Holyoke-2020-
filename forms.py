from django import forms

class ModelForm(forms.Form):
    monthInput = forms.DecimalField(label='Month (MM)', decimal_places=0, max_digits=2)
    dayInput = forms.DecimalField(label='Day (DD)', decimal_places=0, max_digits=2)
    yearInput = forms.DecimalField(label='Year (YYYY)', decimal_places=0, max_digits=4)
    currentCasesInput = forms.DecimalField(label='Current Number of Cases', decimal_places=0, max_digits=8)
    # def is_valid(self):
    #     return(self.month > 0  and self.day > 0 and self.year >= 2020)    