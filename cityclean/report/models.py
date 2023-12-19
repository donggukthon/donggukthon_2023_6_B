from django.db import models
from django.contrib.auth.models import User

class trashCans(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    picture = models.ImageField(upload_to='picture/')
    information = models.TextField()
    complaincount = models.IntegerField(default=0)

class ComplainCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trashCans = models.ForeignKey(trashCans, on_delete=models.CASCADE, related_name='complain_counts')

    def save(self, *args, **kwargs):
        # 해당 쓰레기통에 대한 신고가 처음인 경우에만 complaincount를 증가
        if not ComplainCount.objects.filter(user=self.user, trashCans=self.trashCans).exists():
            self.trashCans.complaincount += 1
            self.trashCans.save()

        super().save(*args, **kwargs)
