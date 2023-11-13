from django import forms
from django.core.exceptions import ValidationError  # Add this import

from women.models import Category, Husband, Women


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Категория не выбрана",
        label="Категория",
    )
    husband = forms.ModelChoiceField(
        queryset=Husband.objects.all(),
        empty_label="Нет пары",
        required=False,
        label="выберите пару",
    )

    class Meta:
        model = Women
        fields = ["title", "slug", "content", 'photo', "is_published", "cat", "husband", "tags"]
        widgets = {  # Fix the attribute name to 'widgets'
            "title": forms.TextInput(attrs={"class": "form-input"}),
            "content": forms.Textarea(attrs={"cols": 50, "rows": 5}),
        }
        labels = {"slug": "URLLLL"}

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) > 20:
            raise ValidationError("Длинна превышает 20 символов")  # Fix the typo here
        return title

class UploadFileForm(forms.Form):
    file = forms.ImageField(label="Файл")
