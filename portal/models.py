from django.db import models

class QuestionPaper(models.Model):
    YEAR_CHOICES = [
        ('1st', '1st Year'),
        ('2nd', '2nd Year'),
        ('3rd', '3rd Year'),
        ('4th', '4th Year'),
    ]
    BRANCH_CHOICES = [
        ('CSE', 'Computer Science Engineering'),
        ('IT', 'Information Technology'),
        ('Allied', 'Allied Branches'),
    ]
    
    year_of_study = models.CharField(max_length=10, choices=YEAR_CHOICES)
    branch = models.CharField(max_length=10, choices=BRANCH_CHOICES, blank=True, null=True)  # Optional for 1st year
    paper_year = models.CharField(max_length=9)  # e.g., "2018-19"
    subject = models.CharField(max_length=100)
    file = models.FileField(upload_to="papers/")
    text_content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.subject} ({self.year_of_study} - {self.paper_year})"
    
    def save(self, *args, **kwargs):
        if self.file and not self.text_content:
            try:
                self.text_content = extract_text_from_pdf(self.file.path)
            except Exception as e:
                print(f"Error extracting text for {self.subject}: {e}")
        super().save(*args, **kwargs)
        
    def extract_text_from_pdf(file_path):
        text = ""
        with open(file_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                text += page.extract_text()
        return text

