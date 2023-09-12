from django.shortcuts import render,redirect
from django.http import HttpResponse
from vegapp.models import recform
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout # return username and password object if user authenticate
from django.contrib.auth.decorators import login_required

    # User is authenticated
@login_required(login_url="/login/")
def show(request):
    if request.method=="POST":

        recname=request.POST.get('name')
        desc=request.POST.get('content')
        file=request.FILES['file']
        new=recform(rec_name=recname,rec_dec=desc,rec_img=file)
        new.save()
        return redirect("/")
    return render(request,"recipe.html")


@login_required(login_url="/login/")
def form(request):
    return render(request,"form.html")


@login_required(login_url="/login/")
def recipedata(request):
    data=recform.objects.all()
    messages.info(request, "Three credits remain in your account.")

    if request.method=="GET":
        # or
    #  if request.GET.get('search'):

      x=request.GET.get('search')
      if x!=None:
       data=recform.objects.filter(rec_name__icontains=x)

    data={
        'data':data,

     }

    return render(request,"recipedata.html",data)


@login_required(login_url="/login/")
def delete(request,id):
    deletedata=recform.objects.get(id = id)
    deletedata.delete()
    return redirect("recipe")

# method 1 update -----------------------------------------------------------

# def updateresipe(request,id):
#     updatedata=recform.objects.get(id = id)
#     return render(request,"update.html",{'updatedata':updatedata})


# def do_update(request,id):
#     try:
#      if request.method=="POST":
#         update_name=request.POST.get('name')
#         update_desc=request.POST.get('content')
#         update_file=request.FILES['file']

#         updatedata=recform.objects.get(id = id)
#         updatedata.rec_name=update_name
#         updatedata.rec_dec=update_desc
#         updatedata.rec_img=update_file
#         updatedata.save()
#         return redirect("recipe")
#      else:
#         return HttpResponse("error")

#     except:
#         return redirect("recipe")

# method 2 update ------------------------------------------------------------------------
# merge in one -----------
@login_required(login_url="/login/")
def updateresipe(request,id):
    updatedata=recform.objects.get(id = id)

    if request.method=="POST":
        recname=request.POST.get('name')
        desc=request.POST.get('content')
        file=request.FILES.get('file')

        updatedata.rec_name=recname
        updatedata.rec_dec=desc
        if file:
          updatedata.rec_img=file

        updatedata.save()
        return redirect("recipe")
    # else:
    #     return HttpResponse("error")

    data={
        'updatedata':updatedata

     }

    return render(request,"update.html",data)




# login ------------------------------------------------------------------------------


def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        # username=email
        user_name=User.objects.filter(username=username)
        if not user_name.exists():
            messages.error(request,"Invalid username ")
            return redirect("/login/")

        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,"invalid password")
            return redirect("/login/")

        else:
            login(request,user)
            return redirect("recipe")


    return render(request,"login.html")

def logout_page(request):
    logout(request)
    return redirect("/login/")


# register --------------------------------------------------------------------------


def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        user_username=User.objects.filter(username=username)
        user_email=User.objects.filter(email=email)

        if user_username.exists():
            messages.warning(request, "Username already taken.")
            return redirect("/register/")

        if user_email.exists():
            messages.warning(request, "Email already taken.")
            return redirect("/register/")
        user=User.objects.create(
        first_name=name,
        username=username,
        email=email

        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully.")
        return redirect("/register/")

    return render(request,"register.html")