from django.db import models
from django.utils import timezone

class Berita(models.Model):
    title = models.CharField(max_length=200, verbose_name="Judul Berita")
    content = models.TextField(verbose_name="Isi Berita")
    image = models.ImageField(upload_to='berita_images/', null=True, blank=True, verbose_name="Gambar")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="Tanggal Publikasi")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Berita"
        ordering = ['-published_date']
