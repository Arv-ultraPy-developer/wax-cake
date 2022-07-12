from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login



# Create your views here.


def sign_up(request):
        if request.method == 'POST':
            email =  request.POST['email'] 
            username =  request.POST['username'] 
            password =  request.POST['password'] 
            password2 =  request.POST['password2'] 

            if password == password2:
                if User.objects.filter(email=email).exists():
                        messages.info(request, 'email already exists')
                        return redirect('signup')

                elif User.objects.filter(username=username).exists():
                        messages.info(request, 'username already exists') 
                        return redirect('signup')      

                else:
                        user = User.objects.create_user(username=username, email=email, password=password)
                        user.save()
                        return redirect('signin')

            else:
                messages.info(request, 'Password not matching')
                return redirect('signup')


        else:
           return render(request,'signup.html')

def sign_in(request):


        if request.method == 'POST':
           
            username =  request.POST['username'] 
            password =  request.POST['password']

            user = auth.authenticate(username=username, password=password)
            
            
            

            if user is not None :
                auth.login(request, user)
                return HttpResponse ('Your Welcome')

               

            else:
                        
                messages.info(request, 'Credentials Invalid')
                return redirect('signin')        

                

        else: 
            return render(request,'signin.html')




        

        

       
       
 
        
    


    

