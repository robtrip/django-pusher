from django.conf.urls import patterns, url

urlpatterns = patterns(
    "",
    url(r"^auth", "django_pusher.views.pusher_auth", name="pusher_auth"),
)
