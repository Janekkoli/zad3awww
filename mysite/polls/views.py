from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.http import Http404
from .models import Question, SVGImage, Square
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # SVGImage.reload()
    context = {"latest_question_list": latest_question_list, "images_list": SVGImage.objects.all()}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'polls/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect to a success page.

@login_required
def artist(request, svg_id):
    svg = SVGImage.objects.get(id=svg_id)

    svg.dataa = str(svg.data())
    print(svg.data())
    return render(request, 'polls/artist.html', {'svg': svg})


@login_required
def delete_square(request, square_id):
    square = get_object_or_404(Square, id=square_id)
    if request.user not in square.image.users.all():
        return HttpResponseForbidden("You are not the owner of this square.")
    square.delete()
    return redirect('show_svg', svg_id=square.image.id)


@login_required
def add_square(request, svg_id):
    svg = get_object_or_404(SVGImage, id=svg_id)
    if request.user not in svg.users.all():
        return HttpResponseForbidden("You are not the owner of this image.")
    if request.method == 'POST':
        x = request.POST.get('x')
        y = request.POST.get('y')
        width = request.POST.get('width')
        height = request.POST.get('height')
        color = request.POST.get('color')
        Square.objects.create(x=x, y=y, width=width, height=height, color=color, image=svg).save()
    return redirect('show_svg', svg_id=svg.id)


def show_svg(request, svg_id):
    svg = SVGImage.objects.get(id=svg_id)
    if request.user not in svg.users.all():
        return render(request, 'polls/show_svg.html', {'svg': svg, 'list_of_squares': [], 'artist': False})
    list_of_squares = Square.objects.filter(image_id=svg_id)
    return render(request, 'polls/show_svg.html', {'svg': svg, 'list_of_squares': list_of_squares, 'artist': True})
