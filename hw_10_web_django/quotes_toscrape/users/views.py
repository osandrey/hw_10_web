from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import RegisterForm, LoginForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'users/signup.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(to="quotes:root")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        print('Hey---------------------------')
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Вітаємо {username}. Ваш акаунт успішно створено!")
            return redirect(to="users:signin")
        return render(request, self.template_name, {"form": form})


# Create your views here.
#
# def signup(request):
#     if request.user.is_authenticated:
#         return redirect(to='quotes:root')
#
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("Save")
#             return redirect(to='quotes:root')
#         else:
#             print("Not Save")
#             return render(request, 'users/signup.html', context={"form": form})
#
#     return render(request, 'users/signup.html', context={"form": RegisterForm()})
#

# def login(request):
#     if request.user.is_authenticated:
#         return redirect(to='quotes:root')
#
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             # form.save()
#             print("login ------------------------------")
#             return redirect(to='quotes:root')
#         else:
#             print("------------------------ Not login")
#             return render(request, 'users/signin.html', context={"form": form})
#
#     return render(request, 'users/signin.html', context={"form": LoginForm()})


# class LoginView(View):
#     form_class = LoginForm
#     template_name = 'users/signin.html'
#
#     def dispatch(self, request, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect(to="quotes:main")
#         return super().dispatch(request, *args, **kwargs)
#
#     def get(self, request):
#         return render(request, self.template_name, {"form": self.form_class})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         print('Hey---------------------------', form)
#         # if form.is_valid():
#         #     print('Form valid')
#         #     # form.save()
#         #     username = form.cleaned_data["username"]
#         #     messages.success(request, f"Вітаємо {username}. Вхід успішно виконан!")
#         #     return redirect(to="quotes:main")
#         # return render(request, self.template_name, {"form": form})
#
#         return redirect(to="quotes:main")

def signin(request):
    if request.user.is_authenticated:
        return redirect(to='quotes:root')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:signin')

        login(request, user)
        return redirect(to='quotes:root')

    return render(request, 'users/signin.html', context={"form": LoginForm()})


@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='quotes:root')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'users/password_reset_subject.txt'