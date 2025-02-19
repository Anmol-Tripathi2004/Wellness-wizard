from django.shortcuts import render # type: ignore

#EbSCAQqL2ZGQdp/VdetKwg==y8No6ZQWOGUeU7Gl

# Create your views here.
def ccc(request):
    import json
    import requests # type: ignore
    if request.method=='POST':
        query = request.POST['query']
        api_url='https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers = {'X-Api-Key':'EbSCAQqL2ZGQdp/VdetKwg==y8No6ZQWOGUeU7Gl'})
        try:
            api= json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api="OOps!There was an error"
            print(e)
        return render(request,'ccc.html',{'api':api})    
    else:
        return render(request,'ccc.html',{'query':'Enter a valid query'})
    
def home(request):
    return render(request,'index2.html')
# def calculator(request):
#     return render(request,'calculator.html')
def course1(request):
    return render(request, 'course1.html')
def course2(request):
    return render(request, 'course2.html')
def course3(request):
    return render(request, 'course3.html')




 