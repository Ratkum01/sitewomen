from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "Черновик"
        PUBLISHED = 1, "Опубликовано"

    title = models.CharField(max_length=255, verbose_name='НАЗВАНИЕ ЧЕ ТАМ ?' )
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name="Статус")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, default="")
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, related_name="posts")
    tags = models.ManyToManyField("TagPost", blank=True, related_name="tags")
    husband = models.OneToOneField('Husband',on_delete=models.SET_NULL, null=True, blank=True, related_name='wuman' )

    published = PublishedManager()
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Известный У'
        verbose_name_plural='Известные Ж'
        
        ordering = ["-time_create"]
        indexes = [
            models.Index(fields=["time_create"]),
        ]

    def get_absolute_url(self):
        return reverse("show_post", kwargs={"post_slug": self.slug})


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        

class TagPost(models.Model):
    tag = models.CharField(max_length=255, unique=True, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.tag

    def get_absolute_url(self):
        return reverse("tag", kwargs={"tag_slug": self.slug})


class Husband(models.Model):
    name = models.CharField(
        max_length=255,
        db_index=True,
    )
    age = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name
