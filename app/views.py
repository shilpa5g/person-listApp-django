from django.shortcuts import render
from .models import Person
from .forms import PersonForm
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def person_list(request):
	persons = Person.objects.all()
	return render(request, 'app/person_list.html', {'persons':persons})

def person_new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'app/person_edit.html', {'form': form})

def person_edit(request,pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('person_list')
    else:
        form = PersonForm(instance=person)
    return render(request, 'app/person_edit.html', {'form': form})

def person_delete(request, pk):
    data_to_be_deleted = get_object_or_404(Person, pk = pk)
    if request.method == 'POST':
        data_to_be_deleted.delete()
        return redirect('person_list')

    return render(request, 'app/person_delete.html', {'data_to_be_deleted': data_to_be_deleted})

def person_detail(request, pk):
    data = get_object_or_404(Person, pk = pk)

    return render(request, 'app/person_detail.html', {'data': data})