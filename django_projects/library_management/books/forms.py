from django.forms import Form
from django import forms
from books.models import Books


class BookForm(forms.Form):
    book_name = forms.CharField(max_length=100)
    book_unique_id = forms.IntegerField()
    author_name = forms.CharField(max_length=100)
    publication_information = forms.CharField(max_length=200, widget=forms.Textarea())
    book_version = forms.FloatField()


    def save(self):
        book_name = book_name
        book_unique_id = book_unique_id
        author_name = author_name
        publication_information = publication_information
        book_version = book_version

        self.save()



