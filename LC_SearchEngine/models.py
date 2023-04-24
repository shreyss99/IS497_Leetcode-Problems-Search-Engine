from django.db import models


class LeetcodeData(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_premium = models.BooleanField()
    difficulty = models.CharField(max_length=6)
    solution_link = models.CharField(max_length=100)
    acceptance_rate = models.FloatField()
    frequency = models.FloatField()
    url = models.CharField(max_length=100)
    discuss_count = models.IntegerField()
    accepted = models.IntegerField()
    submissions = models.CharField(max_length=4)
    companies = models.TextField()
    related_topics = models.CharField(max_length=1000)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    rating = models.IntegerField()
    asked_by_faang = models.BooleanField()
    similar_questions = models.TextField()

    def __str__(self):
        return self.title