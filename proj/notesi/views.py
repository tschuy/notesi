from rest_framework import viewsets
from proj.notesi.serializers import (
    StudentSerializer, UniversitySerializer, CampusSerializer, CourseSerializer,
    NoteSerializer, LectureSerializer)
from proj.notesi.models import (Student, University, Campus,
                                     Course, Note, Lecture)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-user__date_joined')
    serializer_class = StudentSerializer


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
