from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
class Bookmark(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    date = models.DateField(default=timezone.now)
    url = models.TextField(max_length=500)
    class Meta:
        verbose_name = _("Bookmark")
        verbose_name_plural = _("Bookmarks")

    def __str__(self):
        return self.titlefrom


