from rest_framework import serializers

from mainapp.models import(
    Company, Jobs, Events, Video
)

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            'id', 'video', 'date', 'name',
            'preview', 'description', 'name_company', 
        )

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = (
            'id', 'location', 'date', 'website',
            'registration', 'description', 'name',
            'image', 'name_company'
        )

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = (
            'id', 'position', 'salary',
            'type', 'name_company',
        )

class CompanySerializer(serializers.ModelSerializer):
    video = VideoSerializer(read_only=True, many=True)
    events = EventsSerializer(read_only=True, many=True)
    jobs = JobsSerializer(read_only=True, many=True)

    class Meta:
        model = Company
        fields = (
            'id', 'name_company', 'logo', 
            'description', 'telegram', 'whatsapp',
            'video', 'events', 'jobs', 
        )