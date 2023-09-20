from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from .forms import ProfileUpdateForm, CommentForm, CourseCreateForm, CourseContentForm, MessageForm
from .models import Comments, Course, CourseMessage, CourseRegistered
from core.decorators import mentor_required

USER = get_user_model()

# =================================== Dashboard Views =================================== 
@login_required
def dashboard(request):
    context = {
        'title' : 'داشبورد'
    }
    return render(request, 'dashboard/base.html', context)
        
# =================================== Profile Views =================================== 
def profile(request):
    registered_courses = request.user.courses_registered.all()
    messages = CourseMessage.objects.filter(course__registrations__student=request.user)
    print('*'*30)
    print(messages)
    context = {
        'registered_courses': registered_courses,
        'msg': messages,
        'title' : 'پروفایل',
    }
    return render(request, 'dashboard/profile.html', context)


@login_required
def update_profile(request):
    """ update user profile """
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'پروفایل شما با موفقیت اپدیت شد')
            return redirect('dashboard:dashboard')
    else:
        form = ProfileUpdateForm(instance=request.user)

    context = {
        'form': form,
        'title': 'اطلاعات شخصی'
    }
    return render(request, 'dashboard/update-profile.html', context)

# =================================== Contact Us Views =================================== 
def contact_view(request):
    form = CommentForm()
    context = {}
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            user = request.user
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            # admin email
            admin_email = settings.EMAIL_HOST_USER
            # admin_email = 'AliMirzaee1945@proton.me'
            # admin_email = 'mirzaeea450@gmail.com'
            try:
                contact_msg = Comments.objects.create(user=user, subject=subject, message=message)
                contact_msg.save()
                send_mail(
                    'Rasor Contatcs',
                    f'From: {user.email}\n{user.username}\n\nSubject:{subject}\nMessage:\n{message}',
                    settings.EMAIL_HOST_USER,
                    [admin_email],
                    fail_silently=False,
                )
                context['done'] = 'done'
                # form.save()
                return redirect('dashboard:dashboard')
            except:
                # return redirect('dashboard:contact-us')
                context['form_error'] = 'error'
                return render(request, 'dashboard/contact.html', context)
                
            # Comment.save(request, name=name, email=email, subject=subject, message=message)
    
    context = {
        'form': form,
        'title': 'تماس با ما',
    }
    return render(request, 'dashboard/contact.html', context)

# =================================== Course Views =================================== 
@mentor_required
def create_course(request):
    if request.method == 'POST':
        form = CourseCreateForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.mentor = request.user
            course.save()
            return redirect('dashboard:course_detail', course_id=course.id)
    else:
        form = CourseCreateForm()
    context = {
        'form': form,
        'title' : 'ایجاد دوره'
    }
    return render(request, 'dashboard/create_course.html', context)


@mentor_required
def course_content(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseContentForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.course = course
            content.save()
            return redirect('dashboard:course_content', course_id=course.id)
    else:
        form = CourseContentForm()
    context = {
        'form': form,
        'title': 'جزییات دوره',
    }
    return render(request, 'dashboard/course_content.html', context)


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    messages = course.messages.all()
    registered_students = CourseRegistered.objects.filter(course=course)
    registered_students_ids = registered_students.values_list('student_id', flat=True)
    # implement student msg form
    student_messages = CourseMessage.objects.filter(sender=request.user, course__id__in=registered_students_ids)

    context = {
        'course': course,
        'messages': messages, 
        'student_messages': student_messages,
        'title': course.title,
    }
    return render(request, 'dashboard/course_detail.html', context)
        


def course_list(request):
    courses = Course.objects.all()
    context = {
        'items': courses,
        'title': 'لیست دوره ها'    
    }
    
    return render(request, 'dashboard/course_list.html', context)

# =================================== Course Content Views =================================== 
@login_required
@mentor_required
def create_message(request, course_id):
    """ mentor create messages for the course """
    form = MessageForm()
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            user = request.user 
            message = CourseMessage.objects.create(
                course=course,
                sender=user,
                content=content,
            )

            return redirect('dashboard:course_detail', course_id=course_id)
    context = {
        'form': form,
        'course': course,
        'title': 'ایجاد اعلان',
    }
    return render(request, 'dashboard/create_message.html', context)