from django.shortcuts import render

# Create your views here.
from .models import Profile


def my_recommendation_view(request):
    print("I am here ")
    print("user: ", request.user)
    profile = Profile.objects.get(user=request.user)
    print(profile)
    my_recs = profile.get_recommended_profiles()
    context = {'my_recs': my_recs}
    return render(request, 'profile.html', context)