Notesi backend
===============

Rough sketch
------------

* user authentication, user accounts
* users belong universities and classes within those universities

* classes belong to universities
    * ex: class(MTH254 Fall 2015, Dr. Who, 3pm) belongs to uni(OSU)

When a user belongs to a class they can upload notes.

Notes are for a specific lecture. Vote notes up and down, vote users up and down


Objects
-------
* Users:
    * list of classes
    * list of universities (stretch feature: filter search)
    * password? maybe oAuth, maybe CAS
    * username
* Universities:
    * Name
    * Acronym
    * list of classes (not in the db)
    * uni bio?
    * Campus (ex: Corvo, Bend)
* Classes:
    * professor
    * time
    * department
    * course code
    * term
    * university
    * list of lectures
* Notes:
    * lecture
    * contributor
    * votes
* Lectures
    * list of notes
    * class

User Stories
============

I'm a student. I want to upload notes for a specific lecture. I open the app/webapp,
tap the Add Notes button, and take a picture of them. After I take the photo, I
tag it with which class and which lecture.

I'm a student. This is my first time using the service. I create an account, and
get asked for my university. After I tell it my uni, I can search for classes by
MTH254 type things. If it doesn't exist, I can create it. If it does exist, I can
tap on it to add it to my list of classes.

I'm a student reading notes. This person's sucks, so I downvote their notes. If
I notice a trend, I can downvote the user.

I'm a student reading notes. This person has consistently great notes, so I vote
them up.

I'm a OneNote user. I want to add the notes I'm reading to OneNote.
