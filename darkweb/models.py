from django.db import models
from django.contrib.auth.models import User





class Blog(models.Model):
    image = models.FileField(upload_to='images',verbose_name='foto : ')
    description = models.TextField(verbose_name='blog haqqinda : ')
    location = models.CharField(max_length=100,verbose_name='location : ')
    title = models.CharField(max_length=100,verbose_name='blog tin ati :')
    published_date = models.DateTimeField(verbose_name='blog alinga waqit : ',auto_now_add=True)
    def str(self):
        return self .title
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Bloglar'



class Comments(models.Model):
    comment_text = models.TextField(verbose_name='comment text')
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    def str(self):
        return f"{self.username} - {self.comment_text[:20]}..."

    class Meta:
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'