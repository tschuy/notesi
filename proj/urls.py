from django.conf.urls import url, include
from rest_framework import routers
from proj.notesi import views
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'universities', views.UniversityViewSet)
router.register(r'campuses', views.CampusViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'notes', views.NoteViewSet)
router.register(r'lectures', views.LectureViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
