from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import resolve
from django.contrib.auth import authenticate, login, logout

from Admin_Management.user_access import user_pages

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

        self.context["pages"], self.context["access"] = user_property_values["pages"], user_property_values["access"]

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

        self.context["pages"], self.context["access"] = user_property_values["pages"], user_property_values["access"]

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

        self.context["pages"], self.context["access"] = user_property_values["pages"], user_property_values["access"]

        current_url = resolve(request.path_info).url_name

        if current_url in self.context["access"] or self.context["access"] == ["All"]:
            return render(request, self.template, self.context)

        elif "Register" in self.context["access"]:
            return redirect("Register")

        else:
            return redirect("Login")

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

        self.context["pages"], self.context["access"] = user_property_values["pages"], user_property_values["access"]

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

        self.context["pages"], self.context["access"] = user_property_values["pages"], user_property_values["access"]

        current_url = resolve(request.path_info).url_name

        if current_url in self.context["access"] or self.context["access"] == ["All"]:
            return render(request, self.template, self.context)

        elif "Register" in self.context["access"]:
            return redirect("Register")

        else:
            return redirect("Login")