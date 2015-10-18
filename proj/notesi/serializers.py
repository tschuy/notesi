from rest_framework import serializers
from proj.notesi.models import (Student, University, Campus,
                                Course, Note, Lecture)


class UniversitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = University
        fields = ('name', 'bio', 'acronym', 'id')


class CampusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campus
        fields = ('name', 'university', 'id')



class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'username', 'email', 'courses', 'id')


class LectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lecture
        fields = ('course','date', 'id')


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('professor', 'time', 'department', 'course_code', 'term',
                  'university', 'id')


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('student', 'vote_count', 'lecture', 'image', 'id')
