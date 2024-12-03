from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
import sys,time
from django.db.models import Q
from django.http import FileResponse
import openai
from django.conf import settings
from .models import QuestionPaper
import PyPDF2

def home(request):
    return render(request,'homepage.html')

def question_papers_list(request):
    papers_by_year = {
        '1st Year': QuestionPaper.objects.filter(year_of_study='1st Year'),
        '2nd Year': QuestionPaper.objects.filter(year_of_study='2nd Year'),
        '3rd Year': QuestionPaper.objects.filter(year_of_study='3rd Year'),
        '4th Year': QuestionPaper.objects.filter(year_of_study='4th Year'),
    }
    return render(request, 'pdfs.html', {'papers_by_year': papers_by_year})

def download_paper(request, pk):
    paper = get_object_or_404(QuestionPaper, pk=pk)
    return FileResponse(paper.file, as_attachment=True)

def papers_view(request):
    # Example query parameters
    year = request.GET.get('year')
    branch = request.GET.get('branch')
    paper_year = request.GET.get('paper_year')

    # Query the database based on filters (adjust as per your models)
    papers = QuestionPaper.objects.all()
    if year:
        papers = papers.filter(year_of_study=year)
    if branch and year != '1st':  # Exclude branch filtering for 1st year
        papers = papers.filter(branch=branch)
    if paper_year:
        papers = papers.filter(paper_year=paper_year)

    # Pass filters and options to the template
    context = {
        'papers': papers,
        'years': ['1st', '2nd', '3rd', '4th'],  # Pass years list to the template
        'branches': ['CSE', 'IT', 'Allied'],  # Pass branches
        'paper_years': papers.values_list('paper_year', flat=True).distinct(),  # Unique paper years
    }
    return render(request, 'papers.html', context)

def get_filtered_papers(request):
    year = request.GET.get('year')
    branch = request.GET.get('branch')
    paper_year = request.GET.get('paper_year')

    papers = QuestionPaper.objects.all()

    if year:
        papers = papers.filter(year_of_study=year)

    if branch and year != "1st":  # 1st year doesn't have a branch filter
        papers = papers.filter(branch=branch)

    if paper_year:
        papers = papers.filter(paper_year=paper_year)

    papers_data = []
    for paper in papers:
        papers_data.append({
            'subject': paper.subject,
            'file_url': paper.file.url,
        })

    return JsonResponse({'papers': papers_data})


def paper_detail(request, paper_id):
    paper = get_object_or_404(QuestionPaper, id=paper_id)
    return render(request, 'paper_detail.html', {'paper_id': paper_id, 'paper': paper})


openai.api_key = settings.OPENAI_API_KEY
def chatbot_api(request, paper_id):
    if request.method == "POST":
        question = request.POST.get("question")
        paper = get_object_or_404(QuestionPaper, id=paper_id)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are assisting with questions based on this content: {paper.text_content}"},
                {"role": "user", "content": question}
            ]
        )
        answer = response['choices'][0]['message']['content']
        return JsonResponse({"answer": answer})
