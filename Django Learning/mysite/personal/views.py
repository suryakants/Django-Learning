from django.shortcuts import render

def  index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/basic.html', {"content" : ["If you have any query about our product, please email us","abc@gmail.com"]})