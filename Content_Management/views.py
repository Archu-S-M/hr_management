from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import resolve
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage

from Admin_Management.user_access import user_pages

from urllib import request as urlRequest


#==================================================================


# View for dashboard
class Dashboard(LoginRequiredMixin, View):

    login_url = "/"
    redirect_field_name = "Login"

    template = "Content_Management/dashboard.html"
    context = locals()

    def get(self, request):

        user_properties = user_pages(request.user)
        user_property_values = user_properties.getUserViews()

        self.context["pages"], self.context["access"] = (user_property_values["pages"],
                                                         user_property_values["access"])

        current_url = resolve(request.path_info).url_name

        if current_url in self.context["access"] or self.context["access"] == ["All"]:
            return render(request, self.template, self.context)

        elif "Register" in self.context["access"]:
            return redirect("Register")

        else:
            return redirect("Login")

# ===========================================================================
# View for Mange Consultancy
class ManageConsultancy(LoginRequiredMixin, View):

    login_url = "/"
    redirect_field_name = "Login"

    template = "Content_Management/manage_consultancy.html"
    context = locals()

    def get(self, request):

        user_properties = user_pages(request.user)
        user_property_values = user_properties.getUserViews()

        self.context["pages"], self.context["access"] = (user_property_values["pages"],
                                                         user_property_values["access"])

        current_url = resolve(request.path_info).url_name

        if current_url in self.context["access"] or self.context["access"] == ["All"]:
            return render(request, self.template, self.context)

        elif "Register" in self.context["access"]:
            return redirect("Register")

        else:
            return redirect("Login")


# ===========================================================================
# View for candidate profile
class CandidateProfile(LoginRequiredMixin, View):

    login_url = "/"
    redirect_field_name = "Login"

    template = "Content_Management/candidate_profile.html"
    context = locals()

    def get(self, request):

        user_properties = user_pages(request.user)
        user_property_values = user_properties.getUserViews()

        self.context["pages"], self.context["access"] = (user_property_values["pages"],
                                                         user_property_values["access"])

        current_url = resolve(request.path_info).url_name



        if current_url in self.context["access"] or self.context["access"] == ["All"]:
            return render(request, self.template, self.context)

        elif "Register" in self.context["access"]:
            return redirect("Register")

        else:
            return redirect("Login")



    # Uploading or updating candidate profiles
    def post(self, request):

        print(request.POST)
        # get the data from the request
        data = request.POST

        post_method = data["submit"]
        # if post_method == "Create/Update":

        name = data["name"]
        age  = data["age"]
        experience = data["experience"]
        email = data["email"]
        no = data["contact_no"]
        skill_set = data["skills"]
        interview_time = data["interview_time"]

        # get the uploaded files
        candidate_resume = request.FILES['resume']
        interview_video = request.FILES['interview_video']

        # change the file names before move into the media directory
        # The directory will contains the file names with email id as the postscript
        video_name = interview_video.name
        extension = video_name.split(".")[-1]
        new_video_name = "Video-%s.%s" % (email, extension)
        print(interview_video.size)

        resume_name = candidate_resume.name
        extension = resume_name.split(".")[-1]
        new_resume_name = "Resume-%s.%s" % (email, extension)
        print(candidate_resume.size)

        # move the files to the media directory
        fs = FileSystemStorage()
        video  = fs.save(new_video_name, interview_video)
        resume = fs.save(new_resume_name, candidate_resume)


        return redirect("CandidateProfile")

# ===========================================================================
# View for questionnaire
class Questionnaire(LoginRequiredMixin, View):

    login_url = "/"
    redirect_field_name = "Login"

    template = "Content_Management/questionnaire.html"
    context = locals()

    def get(self, request):

        user_properties = user_pages(request.user)
        user_property_values = user_properties.getUserViews()

        self.context["pages"], self.context["access"] = (user_property_values["pages"],
                                                         user_property_values["access"])

        current_url = resolve(request.path_info).url_name

        if current_url in self.context["access"] or self.context["access"] == ["All"]:
            return render(request, self.template, self.context)

        elif "Register" in self.context["access"]:
            return redirect("Register")

        else:
            return redirect("Login")

# ===========================================================================
# View for Candidates eligibility
class Eligibility(LoginRequiredMixin, View):

    login_url = "/"
    redirect_field_name = "Login"

    template = "Content_Management/eligibility.html"
    context = locals()

    def get(self, request):

        user_properties = user_pages(request.user)
        user_property_values = user_properties.getUserViews()

        self.context["pages"], self.context["access"] = (user_property_values["pages"],
                                                         user_property_values["access"])

        current_url = resolve(request.path_info).url_name

        if current_url in self.context["access"] or self.context["access"] == ["All"]:
            return render(request, self.template, self.context)

        elif "Register" in self.context["access"]:
            return redirect("Register")

        else:
            return redirect("Login")