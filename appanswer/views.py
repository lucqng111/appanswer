from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import FirstPage, ImageOfFirstPage, Password, SecondPage, Answer
from .myclass import PasswordAuthentication

# Create your views here.

authentication = PasswordAuthentication(0)


def first_page(request):
    if authentication.status == 1:
        global content_first_page, image_of_first_page
        try:
            content_first_page = FirstPage.objects.get()
            image_of_first_page = ImageOfFirstPage.objects.get()
        except:
            print("Http response")

        content = {"content": content_first_page, "img": image_of_first_page}
        return render(request, "appanswer/first_page.html", content)
    else:
        return HttpResponse("Chua nhap password")


def post_first_page(request):
    global content_second_page
    get_choice = request.POST['choice']
    if get_choice == 'yes' or get_choice == 'no':
        authentication.status = 2
        try:
            content_second_page = SecondPage.objects.get()
        except:
            print("http response")

        content = {"content": content_second_page}
        # return render(request, "appanswer/second_page.html", content)
        return redirect("/appanswer/second_page")
    else:
        return HttpResponse("You must choose")


def second_page(request):
    global content_second_page
    if authentication.status == 2:
        try:
            content_second_page = SecondPage.objects.get()
        except:
            print("http response")

        content = {"content": content_second_page}
        return render(request, "appanswer/second_page.html", content)
    else:
        return HttpResponse("You must choose at first page")


def post_second_page(request):
    get_answer = request.POST['answer']
    # temp_answer = Answer(get_answer)
    ans = Answer(content=get_answer)
    ans.save()
    return redirect("/appanswer/thank_you")


def thank(request):
    return render(request, "appanswer/thank_you.html")


def inputs(request):
    return render(request, "appanswer/input.html")


def get_inputs(request):
    global get_password, code, content_first_page, image_of_first_page
    try:
        get_password = request.POST['pass']
        code = Password.objects.get()
    except:
        print("Http response ")
    if get_password == code.password:
        authentication.modifyStatus(1)
        try:
            content_first_page = FirstPage.objects.get()
            image_of_first_page = ImageOfFirstPage.objects.get()
        except:
            print("Http response")

        content = {"content": content_first_page, "img": image_of_first_page}
        # return render(request, "appanswer/first_page.html", content)
        return redirect("/appanswer/first_page")
    else:
        return render(request, "appanswer/input.html")


def get(request):
    content = {"abc": 1}
    return JsonResponse(content)

