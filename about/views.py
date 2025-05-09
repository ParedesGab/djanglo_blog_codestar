from django.shortcuts import render
from .models import About
from django.contrib import messages
from .forms import CollaborateForm


def about_me(request):
    """
    Renders the most recent information on the website
    author and allows user collaboration request.
    Displays an individual instance of :model:`about.About`.

    **Context**
    ``about``
        The most recent instance of model :model:`about.About`.
    ``collaborate_form``
        An instance of :form:`about.CollaborateForm`.
    
    **Template**
    :template:`about/about.html`

    """
    about = About.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS, "Collaboration request"
                " received! I endeavour to respond within 2 working days.")

    # if request.method == "POST":
    #     print("Received a POST request")
    #     collaborate_form = CollaborateForm(data=request.POST)
    #     if collaborate_form.is_valid():
    #         collaboration = collaborate_form.save(commit=False)
    #         collaboration.save()
    #         messages.add_message(
    #             request, messages.SUCCESS,
    #             'Collaboration request received! I endeavour to respond within'
    #             ' 2 working days.'
    #             )

    collaborate_form = CollaborateForm()
    return render(
            request,
            "about/about.html",
            {
                "about": about,
                "collaborate_form": collaborate_form
            },
    )
