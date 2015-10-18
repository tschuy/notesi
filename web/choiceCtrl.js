var app = angular.module('myApp', []);

app.factory('Calls', function($http) {
    return {
        httpGet: function(endpoint, callback) {
            $http({
                method: 'GET',
                headers: {
                  'Authorization': 'Basic ' + window.btoa('root' + ':' + 'root')
                },
                url: 'http://root:root@dh.tschuy.com/v1/' + endpoint
            }).success(callback);
        },
        httpPatch: function(endpoint, data, callback) {
            $http({
                method: 'PATCH',
                headers: {
                  'Authorization': 'Basic ' + window.btoa('root' + ':' + 'root')
                },
                url: 'http://root:root@dh.tschuy.com/v1/' + endpoint,
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
    };

    $scope.vote = function(voteDelta) {
      currNote.vote_count = currNote.vote_count + voteDelta;
      delete currNote.image;
      Calls.httpPatch('notes/' + currNote.id + '/', currNote, function(result) {
        console.log(result);
      })
    };
});
