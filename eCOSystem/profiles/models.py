from djongo import models

class Follower(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField()

class Following(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField()

class Follow(models.Model):
    user_name = models.EmailField()
    follower = models.ArrayModelField(
        model_container = Follower,
    )
    following = models.ArrayModelField(
        model_container = Following,
    )

    def __str__(self):
        return self.user_name
