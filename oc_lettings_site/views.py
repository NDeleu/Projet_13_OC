from django.shortcuts import render
import sentry_sdk


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie
# quam lobortis leo consectetur ullamcorper non id est. Praesent dictum, nulla
# eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum,
# eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis
# tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi,
# pellentesque iaculis enim cursus in. Praesent volutpat porttitor magna,
# non finibus neque cursus id.
def index(request):
    """
    Affiche la page d'accueil du site.

    Args:
        request (HttpRequest): L'objet HttpRequest
            qui représente la requête HTTP.

    Returns:
        HttpResponse: L'objet HttpResponse qui représente
            la réponse HTTP contenant la page d'accueil.

    """
    try:
        return render(request, 'oc_lettings_site/index.html')
    except Exception as e:
        # Enregistrement de l'exception dans les logs de Sentry
        sentry_sdk.capture_exception(e)
        # Gérer l'exception (par exemple, afficher une page d'erreur personnalisée)
        return render(request, 'error.html', {'error_message': str(e)}, status=500)


def trigger_error(request):
    """
    Déclenche une erreur de division par zéro pour tester
        la capture d'exception par Sentry.

    Args:
        request (HttpRequest): L'objet HttpRequest
            qui représente la requête HTTP.

    Returns:
        HttpResponse: L'objet HttpResponse qui représente
            la réponse HTTP contenant la page d'erreur.

    """
    try:
        division_by_zero = 1 / 0
        print(division_by_zero)
    except ZeroDivisionError as e:
        sentry_sdk.capture_exception(e)
        return render(
            request, 'error.html', {'error_message': str(e)}, status=500)
