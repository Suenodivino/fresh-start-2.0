from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.TextChoices):
    Food = 'food'
    Shelter = 'shelter'
    Housing = 'housing'
    Employment = 'employment'

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.Food)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    excerpt = models.CharField(max_length=100, null=True)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = Post.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '_' + str(count)
            count += 1
            queryset = Post.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug
        
        if self.featured:
            try:
                temp = Post.objects.get(featured=True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except Post.DoesNotExist:
                pass

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


