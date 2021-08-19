import factory
from . import models
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)
    # fields
    is_staff = False
    is_superuser = False
    is_active = True
    username = factory.Sequence(lambda n: "Member_%03d" % (n % 3))
    # first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    # username = factory.Faker('name')


class BoardConfigFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BoardConfig
        django_get_or_create = ('route',)
    # fields
    name = factory.Faker('sentence')
    display_name = factory.Faker('sentence')
    # route = factory.Sequence(lambda n: "Sample_%03d" % (n%3))
    route = 'discussion'
    

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BoardPost
    # fields
    author = factory.SubFactory(UserFactory)
    board = factory.SubFactory(BoardConfigFactory)
    title = factory.Faker('sentence')
    contents = factory.Faker('sentence')
    hit = factory.Faker('pyint', min_value=0, max_value=200)
