from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, FileExtensionValidator
from django.db import models
from django.conf import settings


class Article(models.Model):
    ARTICLE_TYPE_CHOICES = (
        ('laba', "Лабораторна робота"),
        ('kursova', "Курсова робота"),
        ('bach_diplom', "Бакалаврська робота"),
        ('mag_diplom', "Магістерська робота"),
    )
    name = models.CharField(max_length=256, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def file_size_validator(file: models.FileField):
        """
        Function that checks whether file size not exceed the limit
        :param image: django.db.models.ImageField, user's image
        :return: None, ValidationError if image size exceeds the limit
        """
        file_size = file.file.size
        megabyte_limit = 10
        if file_size > megabyte_limit * 1024 * 1024:
            raise ValidationError(f"File size should be {megabyte_limit} Mb")

    file = models.FileField(upload_to="articles", validators=[FileExtensionValidator(
        allowed_extensions=['pdf', 'docx', 'doc']),
        file_size_validator])
    description = models.TextField(blank=True)
    type = models.CharField(max_length=64, choices=ARTICLE_TYPE_CHOICES, default='laba')
    created_at = models.DateTimeField(editable=False, auto_now_add=True)

    def __str__(self):
        """
        Magic method is redefined to show all information about Article.
        :return: subject id and theme
        """
        return f"{self.name}"

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Article class.
        :return: class, id
        """
        return f"{Article.__name__}(id={self.id})"
