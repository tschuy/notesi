angular
	.module('app',['ngRoute'])
	.controller('systCtrl', systCtrl);

	function systCtrl(){
		submitTime: function() {
			
		},

		getLectures: function(){

			$http({
				method:"GET",
				url: "http://dh.tschuy.com/lectures/?course=1"
			}).then(function success(){
				print 
			})
		}
	}
