from .models import Theme, Subject
from django.forms.models import model_to_dict


def menu(request):
    themes = Theme.objects.filter(parent=None).prefetch_related('child_themes')
    return {"themes": themes}
