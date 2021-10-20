from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.core.views import PostOnlyView
from petstagram.pets.forms import PetForm, EditPetForm
from petstagram.pets.models import Pet, Like


def list_pets(request):
    all_pets = Pet.objects.all()
    context = {
        'pets': all_pets,
    }
    return render(request, 'pet_list.html', context)

class CommentPetView(LoginRequiredMixin, PostOnlyView):
    form_class = CommentForm

    def form_valid(self, form):
        pet = Pet.objects.get(pk=self.kwargs['pk'])
        comment = Comment(
            text=form.cleaned_data['text'],
            pet=pet,
            user=self.request.user,
        )
        comment.save()

        return redirect('pet details', pet.id)

    def form_invalid(self, form):
        pass
'''''
@login_required
def comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()

    return redirect('pet details', pet.id)
'''''
class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pet_detail.html'
    context_object_name = 'pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = context['pet']

        pet.likes_count = pet.like_set.count()
        is_owner = pet.user == self.request.user

        is_liked_by_user = pet.like_set.filter(user_id=self.request.user.id) \
            .exists()
        context['comment_form'] = CommentForm(
            initial={
                'pet_pk': self.object.id,
            }
        )
        context['comments'] = pet.comment_set.all()
        context['is_owner'] = is_owner
        context['is_liked'] = is_liked_by_user

        return context

'''''
def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    is_owner = pet.user == request.user

    is_liked_by_user = pet.like_set.filter(user_id=request.user.id) \
        .exists()

    context = {
        'pet': pet,
        'comment_form': CommentForm(),
        'comments': pet.comment_set.all(),
        'is_owner': is_owner,
        'is_liked': is_liked_by_user,
    }
    return render(request, 'pet_detail.html', context)
'''''

@login_required
def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like_object_by_user = pet.like_set.filter(user_id=request.user.id)\
    .first()
    if like_object_by_user:
        like_object_by_user.delete()
    else:
        like = Like(
            pet=pet,
            user=request.user,
        )
        like.save()
    return redirect('pet details', pet.id)

@login_required
def create_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('list pets')
    else:
        form = PetForm()

    context = {
        'form':form,
    }
    return render(request, 'pet_create.html', context)

class EditPetView(LoginRequiredMixin, UpdateView):
    model = Pet
    template_name = 'pet_edit.html'
    form_class = EditPetForm
    success_url = reverse_lazy('list pets')

@login_required
def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('list pets')
    else:
        context = {
            'pet': pet,
        }
        return render(request, 'pet_delete.html', context)