from rest_framework.routers import DefaultRouter as DR

from mainapp.views import(
    CompanyView, JobsView, EventsView, VideoView
)

router = DR()

router.register('company', CompanyView)
router.register('jobs', JobsView)
router.register('events', EventsView)
router.register('video', VideoView)


urlpatterns = []

urlpatterns += router.urls