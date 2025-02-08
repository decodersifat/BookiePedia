from django.shortcuts import render, get_object_or_404, redirect
from .models import Books, Profile , Contact
from django.contrib.auth.models import User
from .forms import BookForm,UserRegistrationForm,ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login 

def index(request):
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            return redirect('index')
    else:
        contact = ContactForm()

    return render(request, 'index.html', {'contact':contact})

def book_list(request):
    books = Books.objects.all().order_by('-created_at')
    return render(request, 'books_list.html', {'books': books})


@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if not request.FILES.get('photo'):
            form.add_error('photo', 'This field is required for this action.')
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})

@login_required
def book_edit(request, book_id):
    book = get_object_or_404(Books, pk=book_id, user=request.user)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})


@login_required
def book_delete(request, book_id):
    book = get_object_or_404(Books, pk=book_id, user=request.user)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    
    return render(request, 'book_confirm_delete.html', {'book': book})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the user instance
            user = form.save()

            # Create the associated profile with the form data
            Profile.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                second_name=form.cleaned_data['second_name'],
                phone=form.cleaned_data['phone'],
                profile_picture=form.cleaned_data['profile_picture']
            )

            # Log the user in immediately after registration
            login(request, user)
            return redirect('book_list')  # Or any other page you want to redirect after registration
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    books = Books.objects.filter(user = request.user).order_by('-created_at')
    profile = Profile.objects.all()
    return render(request, 'profile.html', {'profile': profile, 'books': books})

@login_required
def post(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    return render(request, 'post_details.html',{'book': book})


def home_redirect(request):
    return redirect('/book/book-list/')

def userProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    books = Books.objects.filter(user=user) 

    return render(request, 'user_profile.html', {'profile': profile, 'books': books, 'user': user})