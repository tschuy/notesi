var app = angular.module('myApp', ['naif.base64']);

var BASE_URL = 'http://127.0.0.1:8000/v1'
var BASE_AUTH_URL = 'http://root:root@dh.tschuy.com/v1'

app.factory('Calls', function($http) {
    return {
        httpGet: function(endpoint, callback) {
            $http({
                method: 'GET',
                headers: {
                  'Authorization': 'Basic ' + window.btoa('root' + ':' + 'root'),
                  'Content-Type': 'application/json'
                },
                url: BASE_AUTH_URL + '/' + endpoint
            }).success(callback);
        },
        httpPatch: function(endpoint, data, callback) {
            $http({
                method: 'PATCH',
                headers: {
                  'Authorization': 'Basic ' + window.btoa('root' + ':' + 'root'),
                  'Content-Type': 'application/json'
                },
                url: BASE_AUTH_URL + '/' + endpoint,
                data: data
            }).success(callback);
        },
        httpPost: function(endpoint, data, callback) {
            $http({
                method: 'POST',
                headers: {
                  'Authorization': 'Basic ' + window.btoa('root' + ':' + 'root'),
                  'Content-Type': 'application/json'
                },
                url: BASE_AUTH_URL + '/' + endpoint,
                data: data
            }).success(callback);
        }
    }
});

app.controller('choiceCtrl', function(Calls, $scope, $http) {
    var currCourse, currLecture, currNote;

    Calls.httpGet('courses/', function(result) {
        $scope.receivedCourses = result;
    });

    Calls.httpGet('universities/', function(result) {
        $scope.receivedUniversities = result;
    });

    Calls.httpGet('courses/', function(result) {
        result = result.map(function(c) {
            c.name = c.department + " " + c.course_code + " | " + c.professor;
            return c;
        });
        $scope.receivedCourses = result;
        console.log(result);
    });

    $scope.submitClass = function(form) {
        var data = $scope.newCourseForm;
        data['university'] = BASE_URL + '/universities/' + data['university'] + '/';
        dateStr = data['time'].toString();
        data['time'] = dateStr.substring(dateStr.indexOf(':') - 2, dateStr.lastIndexOf(':') + 3);
        Calls.httpPost('courses/', data, function(result) {
            $scope.successfulUni = true;
            window.location = "/uploadNotes.html";
        });
    }

    $scope.submitNote = function(form) {
        var data = $scope.newNoteForm;
        var courseId = data['course'];
        data['course'] = BASE_URL + '/courses/' + data['course'] + '/';
        data['date'] = data['date'].toISOString().substring(0,10);
        console.log(data.course);
        data.image = data.file.base64;
        delete data.file;

        Calls.httpGet('lectures/?date=' + data['date'] + '&course=' + courseId, function(lec) {
            if (lec.length !== 0) {
                data.lecture = BASE_URL + '/lectures/' + lec[0].id + '/';
                Calls.httpPost('notes/', data, function(newNote) {
                    console.log('made!')
                });
            } else {
                Calls.httpPost('lectures/', {date: data.date, course: data.course}, function(newLec) {
                  data.lecture = BASE_URL + '/lectures/' + newLec.id + '/';
                  Calls.httpPost('notes/', data, function(newNote) {
                      console.log('made new lec too!')
                  });
                });
            }
        });
    }

    $scope.courseClick = function(course) {
        Calls.httpGet('lectures/?course=' + course.id, function(result) {
          currCourse = course;
          $scope.receivedLectures = result;
        });
    };

    $scope.lectureClick = function(lecture) {
      Calls.httpGet('notes/?lecture=' + lecture.id, function(result) {
          currLecture = lecture;
          $scope.receivedNotes = result;
      });
    };

    $scope.noteClick = function(note) {
      currNote = note;
      document.getElementById('note-img').src = note.image.replace('127.0.0.1:8000', 'dh.tschuy.com');
      $scope.hasNote = true;
    };

    $scope.vote = function(voteDelta) {
      currNote.vote_count = currNote.vote_count + voteDelta;
      delete currNote.image;
      Calls.httpPatch('notes/' + currNote.id + '/', currNote, function(result) {
        console.log(result);
      })
    };
});
