from django.shortcuts import render
from .models import Profile
import sentry_sdk


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed
# consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum
# lacus d
def index(request):
    try:
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception as e:
        # Enregistrement de l'exception dans les logs de Sentry
        sentry_sdk.capture_exception(e)
        # Gérer l'exception (par exemple, afficher une page d'erreur personnalisée)
        return render(request, 'error.html', {'error_message': str(e)})


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique
# senectus et netus et males
def profile(request, username):
    try:
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Exception as e:
        # Enregistrement de l'exception dans les logs de Sentry
        sentry_sdk.capture_exception(e)
        # Gérer l'exception (par exemple, afficher une page d'erreur personnalisée)
        return render(request, 'error.html', {'error_message': str(e)})
