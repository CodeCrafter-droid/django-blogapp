from . import models

def get_categories(request):
    cat = models.category.objects.all()

    return dict(categories=cat)


def get_sociallink(request):
    sociallink = models.sociallinks.objects.all()

    return dict(social=sociallink)