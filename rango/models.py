#  -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u"Категории"

    name = models.CharField(u'Название категории', max_length=128, unique=True)
    views = models.IntegerField(u'Количество просмотров', default=0)
    likes = models.IntegerField(u'Понравилось людям', default=0)
    slug = models.SlugField(default='')

    # Override original 'save' to save with slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Page(models.Model):

    class Meta:
        verbose_name = u'Страница'
        verbose_name_plural = u"Страницы"

    category = models.ForeignKey(Category, verbose_name=u"Категория")
    title = models.CharField(u'Заголовок статьи', max_length=128)
    url = models.URLField('Адрес сайта')
    views = models.IntegerField(u'Количество просмотров', default=0)

    def __unicode__(self):
        return self.title


class UserProfile(models.Model):

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    # picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username

