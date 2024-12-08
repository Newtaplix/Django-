from django.shortcuts import render, redirect
from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.loader import render_to_string
from .models import (GeneralInfo, Services, Testemonail, FrequentlyAskedQuestions,
                     ContactFormLog, Blog)

# Create your views here.
def index(request):
    all_records = GeneralInfo.objects.first()
    services = Services.objects.all()
    testimonails = Testemonail.objects.all()
    questions = FrequentlyAskedQuestions.objects.all()

    recent_blogs = Blog.objects.all().order_by("-created")[:3]

    default_val = " "

    context = {
        "company_name": getattr(all_records,"company_name", default_val),
        "location": getattr(all_records,"location", default_val),
        "email": getattr(all_records,"email", default_val),
        "phone":  getattr(all_records,"phone", default_val),
        "open_hours":  getattr(all_records,"open_hours", default_val),
        "video_url":  getattr(all_records,"video_url", default_val),
        "facebook_url":  getattr(all_records,"facebook_url", default_val),
        "instagram_url":  getattr(all_records,"instagram_url", default_val),
        "twitter_url": getattr(all_records,"twitter_url", default_val),

        "services": services,
        "testimonails": testimonails,
        "FAQs": questions,
        "recent_blogs": recent_blogs,
    }
    return render(request, "home.html", context)

def contact_form(request):
    if request.method == "POST":
        print("The form has been submitted")
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        context = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message,   
        }
        html_content = render_to_string('email.html', context)
        is_success = False
        is_error  = False
        error_message = ""
        try:
            send_mail(
                subject=subject,
                message=None,
                html_message=html_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False
            )
        except Exception as e:
            is_error = True
            error_message = str(e)
            messages.error(request, "Email not sent")
        else:
            is_success = True
            messages.success(request, "Mail sent successfully")

        ContactFormLog.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message,
            action_time = timezone.now(),
            is_success = is_success,
            is_error = is_error,
            error_message = error_message
        )
    return redirect("home")

def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    recent_blogs = Blog.objects.all().exclude(id=blog_id).order_by("-created")[:2]
    context = {
        "blog": blog,
        "recent_blogs": recent_blogs,
    }
    return render(request, "blog_detail.html", context)
def blogs(request):
    all_blogs = Blog.objects.all().order_by("-created")
    paginator = Paginator(all_blogs, 3)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context = {
        "blogs": blogs,
    }
    return render(request, "blogs.html", context)
