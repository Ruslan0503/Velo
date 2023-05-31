from django.db import models

# Create your models here.
class PostCompetition(models.Model):
    title = models.TextField()
    body = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

class ImageList1(models.Model):
    which_Post = models.ForeignKey(PostCompetition, on_delete = models.CASCADE)
    images = models.FileField(blank=True, null=True, upload_to='images/')

    class Meta:
        ordering = ['-id']

class VideoList1(models.Model):
    which_Post = models.ForeignKey(PostCompetition, on_delete = models.CASCADE)
    video = models.FileField(blank=True, null=True, upload_to='videos/')

    class Meta:
        ordering = ['-id']
    

class PostNews(models.Model):
    title = models.TextField()
    body = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'PostNews'    

class ImageList(models.Model):
    which_Post = models.ForeignKey(PostNews, on_delete = models.CASCADE)
    images = models.FileField(blank=True, null=True, upload_to='images/')

    class Meta:
        ordering = ['-id']

class VideoList(models.Model):
    which_Post = models.ForeignKey(PostNews, on_delete = models.CASCADE)
    video = models.FileField(blank=True, null=True, upload_to='videos/')

    class Meta:
        ordering = ['-id']
    
