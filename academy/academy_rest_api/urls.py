from rest_framework import routers
from django.urls import path

from academy.academy_rest_api.views.exercises import ExerciseViewSet
from academy.academy_rest_api.views.exercises import ExerciseViewSet2

router = routers.SimpleRouter()
router.register(r'exercises', ExerciseViewSet)

urlpatterns = router.urls + [
    path('test/', ExerciseViewSet2.as_view(), name='hello-view'),
]
