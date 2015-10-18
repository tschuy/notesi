from rest_framework import viewsets
from proj.notesi.serializers import (
    StudentSerializer, UniversitySerializer, CampusSerializer, CourseSerializer,
    NoteSerializer, LectureSerializer)
from rest_framework.response import Response
from proj.notesi.models import (Student, University, Campus,
                                     Course, Note, Lecture)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-user__date_joined')
    serializer_class = StudentSerializer

    def list(self, request):
        queryset = Student.objects.all().order_by('-user__date_joined')
        serializer = StudentSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    def list(self, request):
        queryset = University.objects.all()
        serializer = UniversitySerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer

    def list(self, request):
        queryset = University.objects.all()
        serializer = UniversitySerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def list(self, request):
        if request.GET.get('student', None):
            queryset = Course.objects.filter(student=request.GET.get('student', None))
        else:
            queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def list(self, request):
        if request.GET.get('lecture', None):
            queryset = Note.objects.filter(lecture=request.GET.get('lecture', None))
        else:
            queryset = Note.objects.all()
        serializer = NoteSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer

    def list(self, request):
        if request.GET.get('course', None):
            queryset = Lecture.objects.filter(course=request.GET.get('course', None))
        else:
            queryset = Lecture.objects.all()
        serializer = LectureSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
