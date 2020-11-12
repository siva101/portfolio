from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    pub_date=models.DateTimeField()
    body=models.TextField()

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:50]
    def pubdate(self):
        return self.pub_date.strftime('%b %e %Y')

