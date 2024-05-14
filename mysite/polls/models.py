import datetime

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class SVGImage(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='svg_images/', editable=False)
    users = models.ManyToManyField(User, related_name='images')
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    description = models.TextField(default='', editable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.image:
            content = ContentFile('')
            self.image.save('blank.svg', content, save=False)
            self.reload_svg()
        self.description = str(self)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.reload_svg()
        self.description = str(self)

    def reload_svg(self):
        with open(self.image.path, 'w') as f:
            f.write(f'<svg width="{self.width}" height="{self.height}" xmlns="http://www.w3.org/2000/svg">')
            f.write(f'<rect width="{self.width}" height="{self.height}" fill="none" stroke="black" stroke-width="2"/>')
            for i in Square.objects.filter(image_id=self.id):
                f.write(f'<rect x="{i.x}" y="{i.y}" width="{i.width}" height="{i.height}" fill="{i.color}"/>')
            f.write('</svg>')

    def __str__(self):
        return 'size: ' + str(self.width) + 'x' + str(self.height) + '\n' + 'artists:' + str(self.users.all())


class Square(models.Model):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.image.reload_svg()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.image.reload_svg()

    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    color = models.CharField(max_length=200)
    image = models.ForeignKey(SVGImage, on_delete=models.CASCADE)
