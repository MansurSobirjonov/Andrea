from django.db import models
from django.contrib.auth.models import User

TYPE = (
    (0, 'FASHION'),
    (1, 'TRAVEL'),
)


class Tag(models.Model):
    tag = models.CharField(max_length=221)

    def __str__(self):
        return self.tag


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


# get_<field_name>_display
def post_image_path(instance, filename):
    return 'posts/%s/%s' % (instance.get_type_display(), filename)


class Post(models.Model):
    title = models.CharField(max_length=222)
    slug = models.SlugField()
    image = models.ImageField(upload_to='home/', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    type = models.IntegerField(choices=TYPE)

    def __str__(self):
        return self.title

    def post_comments_count(self):
        return self.comment_set.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=221)
    avatar = models.ImageField(upload_to='comments', null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
