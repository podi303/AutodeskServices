from datetime import date
from django.forms import ModelForm, DateInput, TimeInput, TextInput, IntegerField
from django.core.exceptions import ValidationError
from .models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start': TimeInput(attrs={"time": "time"}),
            'duration': TextInput(attrs={"type": "number", "min": "1", "max": "24"})
        }

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("This date has passed. Please elect a future date")
        return d
