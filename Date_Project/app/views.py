from django.shortcuts import render
from app.models import Human


def profile_list_view(request):
    context = {'human_list': Human.objects.all()}
    return render(request,
                  "profile_list.html", context)


def create_profile_view(request):
    if request.method == "POST":
        first_name_user = request.POST.get("first_name_user")
        last_name_user = request.POST.get("last_name_user")
        login_user = request.POST.get("login_user")
        password_user = request.POST.get("password_user")
        age_user = request.POST.get("age_user")
        about_user = request.POST.get("about_user")
        hobby_user = request.POST.get("hobby_user")
        music_user = request.POST.get("music_user")
        films_user = request.POST.get("films_user")

        human = Human()
        human.first_name_user = first_name_user
        human.last_name_user = last_name_user
        human.login_user = login_user
        human.password_user = password_user
        human.age_user = age_user
        human.about_user = about_user
        human.hobby_user = hobby_user
        human.music_user = music_user
        human.films_user = films_user
        human.save()

    return render(request, "create_profile.html")


def profile_detail_view(request, human_slug):
    human = Human.objects.get(slug=human_slug)
    context = {'human': human}
    return render(request, "profile_detail.html", context)
