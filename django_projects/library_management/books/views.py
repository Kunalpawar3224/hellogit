from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from books.forms import BookForm

# Create your views here.

class BookView(FormView):
    form_class = BookForm
    template_name = 'book_details.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    #def form_invalid(form):



