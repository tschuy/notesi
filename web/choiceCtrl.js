var app = angular.module('myApp', []);

app.factory('Calls', function($http) {
    return {
        httpRequest: function(param, callback) {
            $http({
                method: 'GET',
                headers: {
                  'Authorization': 'Basic ' + window.btoa('root' + ':' + 'root')
                },
                url: 'http://root:root@dh.tschuy.com/' + param
            }).success(callback);
        }
    }
});

app.controller('choiceCtrl', function(Calls, $scope, $http) {
    Calls.httpRequest('courses/', function(result) {
        $scope.receivedCourses = result;
    });

    $scope.courseClick = function(course) {
        Calls.httpRequest('lectures/?course=' + course.id, function(result) {
          $scope.receivedLectures = result;
        });
    };

    $scope.lectureClick = function(lecture) {
      Calls.httpRequest('notes/?lecture=' + lecture.id, function(result) {
          $scope.receivedNotes = result;
      });
    }
});
