from rest_framework.routers import SimpleRouter
from .views import UserViewSet, TaskViewSet, CategoryViewSet


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('tasks', TaskViewSet, basename='tasks')
router.register('category', CategoryViewSet, basename='category')
urlpatterns = router.urls
