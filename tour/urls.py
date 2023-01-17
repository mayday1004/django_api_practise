from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register("", views.TourViewSet, basename="tours")


urlpatterns = router.urls
