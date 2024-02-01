from django.shortcuts import render,redirect
from django.http import HttpResponse
import sys,time
from .models import Student
# Create your views here.

def home(request):
    return render(request,'homepage.html')

def pdfs(request):
    if request.method == 'GET':
        selected_year = request.GET.get('year')
        # Fetch data based on the selected year and group by 'name'
        data = Student.objects.filter(year=selected_year).values('name', 'question_papers_link')
        grouped_data = {}  # Dictionary to store data grouped by 'name'
        range=["2018-19","2019-20","2020-21","2021-22","2022-23"]
        if selected_year=='1':
            sel="1st"
        elif selected_year=='2':
            sel="2nd"
        elif selected_year=='3':
            sel="3rd"
        elif selected_year=='4':
            sel="4th"
        else:
            sel="No Year Selected"
        for item in data:
            name = item['name']
            if name not in grouped_data:
                grouped_data[name] = []
            grouped_data[name].append(item['question_papers_link'])
        return render(request, 'pdfs.html', {'grouped_data': grouped_data,'range':range,'selected_year':selected_year,'select':sel})
    return render(request, 'pdfs.html', {'grouped_data': None})
    