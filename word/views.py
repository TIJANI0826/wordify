from django.shortcuts import render

# Create your views here.
def about(request):
	return render(request,'about.html')

def blog_single(request):
	return render(request,'blog-single.html')
def category(request):
	return render(request,'category.html')
def contact(request):
	return render(request,'contact.html')
def index(request):
	return render(request,'index.html')
