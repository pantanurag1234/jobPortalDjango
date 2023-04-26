from django.forms import ModelForm
from .models import organisations,registration

class landingForm(ModelForm):
    class Meta:
        model = organisations
        fields = ['name', 'position', 'package_in_LPA', 'experience_in_yrs']

# class regForm(ModelForm):
#     class Meta:
#         model = registration
#         fields = ['name', 'email', 'password', 'confirm_password']