from django.shortcuts import render, get_object_or_404
from .models import Letting
import sentry_sdk


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa. Integer est nunc, pulvinar a
# tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus
# orci luctus et ultrices posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    Affiche la liste de toutes les locations disponibles.

    Récupère toutes les instances du modèle Letting et
        les affiche sur la page d'accueil.

    Args:
        request (HttpRequest): L'objet HttpRequest représentant
            la requête HTTP en cours.

    Returns:
        HttpResponse: Une réponse HTTP avec le contenu
            HTML de la page d'accueil affichant les locations.

    Raises:
        Exception: Si une erreur se produit lors
            de la récupération des locations.

    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan
# porta nisl id eleifend. Praesent dignissim, odio eu consequat pretium, purus
# urna vulputate arcu, vitae efficitur
#  lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas
#  auctor, est ut luctus congue, dui enim mattis enim, ac condimentum velit
#  libero in magna. Suspendisse potenti. In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque
# justo mattis ullamcorper ac non tellus. In tristique mauris eu velit
# fermentum, tempus pharetra est luctus. Vivamus consequat aliquam libero,
# eget bibendum lorem. Sed non dolor risus. Mauris condimentum auctor
# elementum. Donec quis nisi ligula. Integer vehicula tincidunt enim,
# ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
    Affiche les détails d'une location spécifique.

    Récupère une instance du modèle Letting en fonction de
    l'ID donné et affiche ses détails.

    Args:
        request (HttpRequest): L'objet HttpRequest représentant
            la requête HTTP en cours.
        letting_id (int): L'ID de la location à afficher.

    Returns:
        HttpResponse: Une réponse HTTP avec le contenu HTML de la page
        affichant les détails de la location.

    Raises:
        Http404: Si la location avec l'ID donné n'existe pas.
        Exception: Si une erreur se produit lors de la
            récupération de la location.

    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return render(
            request, 'error.html', {'error_message': str(e)}, status=500)
