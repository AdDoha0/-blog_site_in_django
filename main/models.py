from django.db import models
from django.urls import reverse_lazy

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    is_published = models.BooleanField(default=False, db_index=True, verbose_name="Статус")
    is_featured = models.BooleanField(default=False, verbose_name="Главный пост")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name="Категории")


    class Meta:
        verbose_name = 'Хадис'
        verbose_name_plural = 'Хадисы'


    def save(self, *args, **kwargs):
        # Если пост помечен как избранный
        if self.is_featured:
            # Удаляет отметку избранного у других постов
            Post.objects.filter(is_featured=True).exclude(id=self.id).update(is_featured=False)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('main:category', kwargs={'cat_slug': self.slug})