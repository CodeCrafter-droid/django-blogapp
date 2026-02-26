from rest_framework.routers import DefaultRouter
from .views import BlogAPI

router =  DefaultRouter()
router.register(r'blog',BlogAPI)

urlpatterns = router.urls
