from django.shortcuts import render,redirect
from django.http import HttpResponse
import sys,time
from .models import Student
# Create your views here.

def home(request):
    return render(request,'homepage.html')

def pdfs(request):
    students = Student.objects.all()
    
    selected_year = request.GET.get('year')
    if selected_year:
        pdf_links = Student.objects.filter(year=selected_year).values_list('question_papers_link', flat=True)
    else:
        pdf_links = None

    return render(request, 'pdfs.html', {'students': students, 'pdf_links': pdf_links,'selected_year':selected_year})
    