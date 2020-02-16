from django.db import models
from django.utils.safestring import mark_safe
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor_uploader.fields import RichTextUploadingField

class Skill(models.Model):
    name = models.CharField(unique=True, max_length=400)
    progress = models.PositiveSmallIntegerField(help_text='Enter a number from 0 to 100', default=0)

    def __str__(self):
        return "{} | {}%".format(self.name, self.progress)

    class Meta:
        ordering = ['-progress']

class Profile(models.Model):
    background_image = ThumbnailerImageField(upload_to='large_profile/', blank=True, null=True)
    image = ThumbnailerImageField(upload_to='profile/')
    name = models.CharField(unique=True, max_length=400)
    profile_type = models.CharField(max_length=1500)
    profile_type_list = models.TextField(max_length=2000, help_text='Used in top slider')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True)
    bio = RichTextUploadingField(verbose_name='Bio', max_length=5000)
    skills = models.ManyToManyField(Skill)
    work_completed = models.PositiveIntegerField(default=0)
    experience_years = models.PositiveSmallIntegerField(default=0)
    total_clients = models.PositiveIntegerField(default=0)
    awards_won = models.PositiveIntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)
    mod_at = models.DateTimeField(auto_now=True)
    address = models.TextField(max_length=10000, blank=True, null=True)
    facebook_url = models.URLField(max_length=1000, blank=True, null=True)
    instagram_url = models.URLField(max_length=1000, blank=True, null=True)
    twitter_url = models.URLField(max_length=1000, blank=True, null=True)
    pinterest_url = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    icon_class = models.CharField(max_length=100, help_text=mark_safe('''
    Check for icons from : <a href="https://fontawesome.com/icons?d=gallery&m=free" target="_blank">FontAwesome Icons</a>
    '''))
    name = models.CharField(unique=True, max_length=1000)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Category(models.Model):
    name = models.CharField(unique=True, max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

class Testimonial(models.Model):
    image = ThumbnailerImageField(upload_to='testimonial/')
    name = models.CharField(unique=True, max_length=500)
    description = RichTextUploadingField(verbose_name='Description', max_length=5000)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Work(models.Model):
    image = ThumbnailerImageField(upload_to='posts/')
    name = models.CharField(unique=True, max_length=500)
    description = RichTextUploadingField(verbose_name='Description', max_length=5000)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    mod_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-added_at']

class Post(models.Model):
    image = ThumbnailerImageField(upload_to='posts/')
    title = models.CharField(unique=True, max_length=1000)
    content = RichTextUploadingField(verbose_name='Content', max_length=5000)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    added_at = models.DateTimeField(auto_now_add=True)
    mod_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-added_at']
