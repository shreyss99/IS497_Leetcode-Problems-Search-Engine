from django.db import models


class LeetcodeData(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_premium = models.BooleanField(null=True, blank=True)
    difficulty = models.CharField(max_length=6, null=True, blank=True)
    solution_link = models.CharField(max_length=200, null=True, blank=True)
    acceptance_rate = models.FloatField(null=True, blank=True)
    frequency = models.FloatField(null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    discuss_count = models.IntegerField(null=True, blank=True)
    accepted = models.CharField(max_length=10, null=True, blank=True)
    submissions = models.CharField(max_length=10, null=True, blank=True)
    companies = models.TextField(null=True, blank=True)
    related_topics = models.CharField(max_length=300, null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    dislikes = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    asked_by_faang = models.BooleanField(null=True, blank=True)
    similar_questions = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
