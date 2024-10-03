from django.db import models


class MovieOrder(models.Model):
    purchased_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
