angular
	.module('app',['ngRoute'])
	.factory('systFactory', systFactory);

	function systFactory(){

		getLectures: function(){

			$http({
				method:"GET",
				url: "http://dh.tschuy.com/lectures/?course=1"
			}).then(function success(){
				
			})
		}
	}