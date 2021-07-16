from django import forms

from .. models import Category


class CategoryCreationForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(CategoryCreationForm, self).clean()
        category = cleaned_data.get('category')

        if not category:
            raise forms.ValidationError("Please choose category")

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance

class CategoryChangeForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def clean(self):
        cleaned_data = super(CategoryChangeForm,self).clean()
        category = cleaned_data.get('category')

        if not category:
            raise forms.ValidationError("Please add a category")

    def save(self, commit=True):
        instance =  super().save(commit=False)

        if commit:
            instance.save()
        return instance