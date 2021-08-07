from django.db import models


class FileUpload(models.Model):
    title = models.CharField(verbose_name="画像のタイトル", max_length=100)
    image = models.ImageField(verbose_name="画像",upload_to="images/upload_files/")

    def __str__(self):
        return self.title