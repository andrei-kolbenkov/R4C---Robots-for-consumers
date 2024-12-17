from django import forms
from .models import Robot

class RobotForm(forms.ModelForm):
    ALLOWED_MODELS = ['R2', '13', 'X5']  # Список допустимых моделей

    class Meta:
        model = Robot
        fields = ['model', 'version', 'created']

    def clean_model(self):
        model = self.cleaned_data.get('model')
        if model not in self.ALLOWED_MODELS:
            raise forms.ValidationError(f"Model '{model}' is not allowed.")
        return model