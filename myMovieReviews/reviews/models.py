from django.db import models

# Create your models here.
class Review(models.Model):
  GENRE_CHOICES = [
        ('SF', 'SF'),
        ('코미디', '코미디'),
        ('액션', '액션'),
        ('드라마', '드라마'),
        ('공포', '공포'),
        ('로맨스', '로맨스'),
  ]
  
  title = models.CharField(max_length=200)
  year = models.IntegerField() #개봉 년도
  genre = models.CharField(max_length=50, choices=GENRE_CHOICES) #장르
  rating = models.FloatField() #별점
  content = models.TextField() #리뷰 내용
  director = models.CharField(max_length=100) #감독
  actors = models.CharField(max_length=200)
  running_time = models.IntegerField() #러닝타임
  created_at = models.DateTimeField(auto_now_add=True)
  
  def running_time_display(self):
    hours = self.running_time // 60
    minutes = self.running_time % 60
    return f"{hours}시간 {minutes}분"

  def __str__(self):
    return self.title