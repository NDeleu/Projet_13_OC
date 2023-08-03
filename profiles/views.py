from django.shortcuts import render, get_object_or_404
from .models import Profile
import sentry_sdk


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed
# consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum
# lacus d
def index(request):
    """
    Affiche la liste de tous les profils.

    Args:
        request (HttpRequest): L'objet HttpRequest
            qui représente la requête HTTP.

    Returns:
        HttpResponse: L'objet HttpResponse qui représente la réponse HTTP.

    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique
# senectus et netus et males
def profile(request, username):
    """
    Affiche le profil d'un utilisateur en fonction de son nom d'utilisateur.

    Args:
        request (HttpRequest): L'objet HttpRequest
            qui représente la requête HTTP.
        username (str): Le nom d'utilisateur de l'utilisateur
            dont le profil doit être affiché.

    Returns:
        HttpResponse: L'objet HttpResponse qui représente la réponse HTTP.

    """
    try:
        profile = get_object_or_404(Profile, user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return render(request, 'error.html', {'error_message': str(e)})
