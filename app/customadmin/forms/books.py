from django import forms

from ..models import Book



class BookCreationForm(forms.ModelForm):
    class Meta():
        model = Book
        exclude = ['published_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(BookCreationForm, self).clean()
        title = cleaned_data.get('title')
        author = cleaned_data.get('author')
        price = cleaned_data.get('price')
        pages = cleaned_data.get('pages')
        image = cleaned_data.get('image')
        category = cleaned_data.get('category')
        description = cleaned_data.get('description')

        if not title:
            raise forms.ValidationError(

                "Please add title"
            )
        if not author:
            raise forms.ValidationError(

                "Please add author"

            )
        if not price:
            raise forms.ValidationError(

                "Please add valid price"

            )
        if not pages:
            raise forms.ValidationError(

                "Please add valid total no. of pages"

            )
        if not image:
            raise forms.ValidationError(

                "Please add an image"

            )
        if not category:
            raise forms.ValidationError(

                "Please add category"

            )
        if not description:
            raise forms.ValidationError("Please add description")

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        return instance

class BookChangeForm(forms.ModelForm):
    class Meta():
        model = Book
        fields = [
            "title",
            "author",
            "category",
            "image",
            "price",
            "pages",
            "description",
        ]


    def clean(self):
        cleaned_data=super(BookChangeForm,self).clean()
        title = cleaned_data.get('title')
        author = cleaned_data.get('author')
        price = cleaned_data.get('price')
        pages = cleaned_data.get('pages')
        image = cleaned_data.get('image')
        category = cleaned_data.get('category')
        description = cleaned_data.get('description')

        if not title:
            raise forms.ValidationError("Please add a title")
        if not author:
            raise forms.ValidationError("Please add an author")
        if not price:
            raise forms.ValidationError("Please add a valid price")
        if not pages:
            raise forms.ValidationError("Please add valid total no. of pages")
        if not image:
            raise forms.ValidationError("Please add an image")
        if not category:
            raise forms.ValidationError("Please add a category")
        if not description:
            raise forms.ValidationError("Please add a description")

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance