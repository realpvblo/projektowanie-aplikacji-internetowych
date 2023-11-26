from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.conf import settings
from .models import Image
from .forms import ImageUploadForm, RegistrationForm
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'myapp/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('myapp:panel')  # Przekierowanie po udanym zalogowaniu
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

# def registration_view(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST, instance=User())
#         if form.is_valid():
#             # Zarejestruj użytkownika lub wykonaj inne operacje
#             form.save()
#             # Przekieruj użytkownika na stronę logowania po udanej rejestracji
#             return redirect('myapp:login')
#     else:
#         form = RegistrationForm()

#     return render(request, 'myapp/registration.html', {'form': form})

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:login')
    else:
        form = UserCreationForm()

    return render(request, 'myapp/registration.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('myapp:home')  

@login_required
def panel_view(request):
    images = Image.objects.filter(user=request.user)  # Pobieranie wszystkich zdjęć użytkownika

    context = {
        'images': images,
    }

    return render(request, 'myapp/panel.html', context)

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            image = form.cleaned_data['image']
            Image.objects.create(user=user, image=image)

            # Logowanie informacji o przesłanym pliku
            logger.info(f"Użytkownik {user.username} przesłał plik: {image}")

    else:
        form = ImageUploadForm()

    images = Image.objects.filter(user=request.user)

    context = {
        'form': form,
        'images': images,
    }

    return render(request, 'myapp/panel.html', context)

@login_required
def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)

    # Upewnij się, że tylko właściciel może usunąć zdjęcie
    if image.user == request.user:
        image.delete()
    
    return redirect('myapp:panel')

@csrf_exempt
def reorder_images(request):
    if request.method == "POST":
        image_order = request.POST.getlist("order[]")  # Odbieranie kolejności zdjęć jako lista
        try:
            for idx, image_id in enumerate(image_order):
                image = Image.objects.get(id=image_id)
                image.order = idx
                image.save()
            return JsonResponse({"message": "Kolejność zaktualizowana poprawnie."})
        except Exception as e:
            return JsonResponse({"message": "Błąd aktualizacji kolejności: " + str(e)}, status=400)
    return JsonResponse({"message": "Błąd aktualizacji kolejności."}, status=400)
