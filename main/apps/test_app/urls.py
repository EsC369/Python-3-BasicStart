from django.conf.urls import indlude, url  # adding include package
from . import views           # . = looks at the same directory im in, and look for a file called views and import it into this file.
urlpatterns = [
    url(r'^$', views.index)   # Looks for an empty root url and redirect to the views folder and pulls the index/html file within views
    url(r'^info$', views.info) # When typing  /info, will go into views folder and render the info file/html
] 