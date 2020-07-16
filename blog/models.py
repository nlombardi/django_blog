from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model): # creates a post table in the database
    title = models.CharField(max_length=100) # creates title field in the table
    content = models.TextField()
    # auto_now = True sets it to current date every time its edited, more like modified now, can also do auto_now_add
    date_posted = models.DateTimeField(default=timezone.now)
    # models.CASCADE will delete the posts if a user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(default='default.jpg', upload_to='blog_pics')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self): # overriding the save method in the parent class
        super().save() # runs the parent class save method

        img = Image.open(self.post_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.post_image.path)


# Create your models here.
