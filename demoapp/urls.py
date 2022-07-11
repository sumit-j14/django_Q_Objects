from django.urls import path
from .views import *

urlpatterns = [
    path('get_all', get_all),
    path('get/<int:rn>', get_rollnumber),
    path('get/<int:rn>/<int:an>/', qsearch),
]
