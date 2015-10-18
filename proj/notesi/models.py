from django.contrib.auth.models import User, UserManager
from django.db import models

class Student(User):
    user = models.OneToOneField(User)
    univerities = models.ManyToManyField('University')
    courses = models.ManyToManyField('Course')

    objects = UserManager()

    def __unicode__(self):
        return self.username


class University(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    acronym = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name


class Campus(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey('University')

    def __unicode__(self):
        return self.name

class Course(models.Model):
    TERMS = ( # TODO find better way to do this
        ('FALL', 'Fall'),
        ('WINTER', 'Winter'),
        ('SUMMER', 'Summer'),
        ('SPRING', 'Spring'),
    )

    professor = models.CharField(max_length=100) # this should be a foreign key
    time = models.TimeField()
    department = models.CharField(max_length=10) # this should be a foreign key
    course_code = models.CharField(max_length=10)
    term = models.CharField(max_length=10, choices=TERMS)
    university = models.ForeignKey('University')

    def __unicode__(self):
        return "{} {}".format(self.department, self.course_code)


class Note(models.Model):
    student = models.ForeignKey('Student')
    vote_count = models.IntegerField()
    lecture = models.ForeignKey('Lecture')
    #image_url = models.URLField()
    image = models.ImageField()

    def __unicode__(self):
        return "{} by {}".format(self.lecture, self.student)


class Lecture(models.Model):
    date = models.DateField()
    course = models.ForeignKey('Course')
    def __unicode__(self):
        return "{} on {}".format(self.course, self.date)
