from django.shortcuts import render
from django.views.generic import View

from .forms import LoginForm


# To show the initial page
class Login(View):

    template = "login.html"
    context = locals()

    def get(self, request):
        '''
        Get request to access the login page
        :param request:
        :return: template
        '''
        form = LoginForm()
        self.context['form'] = form

        return render(request, self.template, self.context)


    def post(self, request):
        '''
        Post request when login form or registration submits
        :param request:
        :return:
        '''

