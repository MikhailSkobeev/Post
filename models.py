from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User, max_length=64, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):

    t = 'Tanks'
    h = 'Hily'
    d = 'DD'
    m = 'Merchants'
    gm = 'Guild Masters'
    qg = 'Quest Givers'
    b = 'Blacksmiths'
    tan = 'Tanners'
    pm = 'Potion Makers'
    sm = 'Spell Master'
    category = 'CT'

    category_choices = (
        (category, 'Категории'),
        (t, 'Танки'),
        (h, 'Хилы'),
        (d, 'ДД'),
        (m, 'Торговцы'),
        (gm, 'Гильдмастеры'),
        (qg, 'Квестгиверы'),
        (b, 'Кузнецы'),
        (tan, 'Кожевники'),
        (pm, 'Зельевары'),
        (sm, 'Мастер заклинаний'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categoryType = models.CharField(max_length=2, choices=category_choices, default=category)
    dateCreation = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)