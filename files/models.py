from django.db import models


class Files(models.Model):
    name = models.CharField(max_length=50)
    uploaded_file = models.FileField(verbose_name=None, name=None, upload_to='files/csv')
    published_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} , was uploaded on {}'.format(self.name, self.published_on)
