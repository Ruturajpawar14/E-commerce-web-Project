from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import myForm
from contactEnquiry.models import contactEnquiry

def saveEnquiry(request):
    n=" "
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        
        data=contactEnquiry(name=name,email=email,phone=phone)
        data.save()
        n="Data Inserted"

           
    return render(request,"contact.html", {'n':n})

    





 
def Homepage(request):
    return render(request,"index.html")

def Aboutpage(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"About.html", {'output':output})

def Blogpage(request):
    return render(request,"Blog.html")

def Chartpage(request):
    return render(request,"Chart.html")

def shop(request):
    return render(request,"Shop.html")


def Contactpage(request):
    return render(request,"Contact.html")
def sproduct(request):
    return render(request,"sproduct.html")
    
def course(request):
    return HttpResponse("Welcone to Request page")



def userform(request):
    final=0
    fn=myForm()
    data={'form':fn}
    try:
        if request.method=="POST":
    #    n1=int(request.GET['num1'])
    #    n2=int(request.GET['num2'])
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            final=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'form':fn,
                'output':final
            }
            # return HttpResponseRedirect('/About')
    except:
       pass
    return render(request, "userform.html",data)






# def marksheet(request):
#     if request.method=="POST":
#         s1=eval(request.POST.get("subject1"))
#         s2=eval(request.POST.get("subject2"))
#         s3=eval(request.POST.get("subject3"))
#         s4=eval(request.POST.get("subject4"))
#         s5=eval(request.POST.get("subject5"))
#         t=s1+s2+s3+s4+s5
#         print(t)
   
#         return render(request, "Marksheet.html")        
#     return render(request, "Marksheet.html")