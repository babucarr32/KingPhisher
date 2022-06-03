from django.shortcuts import render

def facebook(request):
    return render(request, 'facebook.html')

def signup(request):
    if request.method == 'POST': #User has info and wants an an account
        print( request.POST['username'])
        print( request.POST['password'])
        return render(request, 'facebook.html')