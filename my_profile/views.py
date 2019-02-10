from allauth.account.views import LoginView
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PostForm

@login_required
def profile(request):
    return render(request, 'my_profile/layout.html')


def login(request):

    providers = []
    for provider in get_providers():

        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)
    return LoginView.as_view(
        template_name='accounts/login_form.html',
        extra_context={'providers': providers})(request)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.tag_save()
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'my_profile/post_form.html', {
        'form': form,
        })