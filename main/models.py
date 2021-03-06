from tabnanny import verbose
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


# Create your models here.


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    name = models.CharField(max_length=20, blank=True, null= True)
    score = models.IntegerField(default=80, blank=True, null= True)
    image = models.FileField(blank=True, null= True, upload_to='skills')
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    user = models.OneToOneField (User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null= True, upload_to= 'avatar')
    title = models.CharField (max_length=200, blank=True, null=True)
    bio = models.TextField (blank=True, null=True)
    skills = models.ManyToManyField (Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to='cv')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'



class ContactProfile(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ['timestamp']

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField (max_length=200, blank=False, null=False, verbose_name='Name')
    email = models.EmailField(blank=False, null=False, verbose_name='Email')
    message = models.TextField (blank=False, null=False, verbose_name='Message')

    def __str__(self):
        return f'{self.name}'


class Testimonial(models.Model):

    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonials'
        ordering = ['name']

    thumbnail = models.ImageField(blank=True, null= True, upload_to= 'thumbnail')
    name = models.CharField (max_length=200, blank=True, null=True)
    role = models.CharField (max_length=200, blank=True, null=True)
    quote = models.CharField (max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Medias'
        verbose_name = 'Media'
        ordering = ['name']

    image = models.ImageField(blank=True, null= True, upload_to= 'media')
    url = models.URLField (blank=True, null=True, verbose_name='url')
    name = models.CharField(max_length=200 ,blank=True, null=True, verbose_name='name')
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Porfolios'
        verbose_name = 'Portfolio'
        ordering = ['name']

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField (max_length=200, blank=True, null=True, verbose_name='name')
    description = models.CharField(max_length=500 ,blank=True, null=True, verbose_name='description')
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to= 'media')
    url = models.URLField (blank=True, null=True, verbose_name='url')
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return f'/portfolio/{self.slug}'


class Blog(models.Model):

    class Meta:
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'
        ordering = ['datetime']

    datetime = models.DateTimeField(auto_now_add=True)
    author = models.CharField (max_length=200, blank=True, null=True, verbose_name='author')
    name = models.CharField (max_length=200, blank=True, null=True, verbose_name='name')
    description = models.CharField(max_length=500 ,blank=True, null=True, verbose_name='description')
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to= 'blog')
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return f'/blog/{self.slug}'


class Certificate(models.Model):

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField (max_length=200, blank=True, null=True, verbose_name='name')
    title = models.CharField(max_length=500 ,blank=True, null=True, verbose_name='title')
    description = models.CharField(max_length=500 ,blank=True, null=True, verbose_name='description')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'