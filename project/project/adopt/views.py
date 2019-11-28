from django.http import HttpResponse
from django import render

from .models import Pet

def all_pets(request):
    pets = Pet.objects.all()
    context = {
            'pets': pets
            }
    return render(request, 'adopt/all.html', context)
            
    response_text = 'Check out these pets!'
    for pet in Pet.objects.all():
        response_text += f'{pet.species}, '
    return HttpResponse(response_text)


def pet_details(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return HttpResponse(f"Hi, I'm pet {pet.id}")
