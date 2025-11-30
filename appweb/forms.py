from django import forms

class ClientForm(forms.Form):
    SEX_CHOICES = (
        ('M','Male'),
        ('F','Female')
    )
    dni = forms.CharField(max_length=20, label='DNI')
    name = forms.CharField(max_length=150, label='Name', required=True)
    last_name = forms.CharField(max_length=150, label='Last_name', required=True)
    email = forms.EmailField(label='Email', required=True)
    address = forms.CharField(label='Address', max_length=200, required=True)
    phone = forms.CharField(label='Phone', max_length=30, required=False)
    sex= forms.ChoiceField(label='Sex', choices=SEX_CHOICES, required=False)
    birth_date = forms.DateField(label='Birth date', required=False, input_formats=['%Y-%m-%d'],widget=forms.DateInput(attrs={'type': 'date'}))



