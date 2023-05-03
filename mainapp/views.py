from rest_framework.viewsets import ModelViewSet

from mainapp.models import(
    Company, Jobs, Events, Video
)

from mainapp.serrielizer import(
    CompanySerializer, JobsSerializer, 
    EventsSerializer, VideoSerializer
)

class CompanyView(ModelViewSet):
    queryset = Company.objects.all()                   
    serializer_class = CompanySerializer

class JobsView(ModelViewSet):
    queryset = Jobs.objects.all()                   
    serializer_class = JobsSerializer

class EventsView(ModelViewSet):
    queryset = Events.objects.all()                   
    serializer_class = EventsSerializer

class VideoView(ModelViewSet):
    queryset = Video.objects.all()                   
    serializer_class = VideoSerializer

