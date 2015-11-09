ChatApp.controller('PostMessageController', ['$rootScope','$scope','$http','Upload',
    function($rootScope,$scope, $http,Upload) {
        $scope.file = []
        $scope.message = {'text':''};
        $scope.send_message = function(isValid,message) {
            $scope.submitted = true;
            if (isValid) {
                if ($scope.file.length){ $scope.upload($scope.file,message)}
                else{
                    $http.post('/api/messages/create/',message)
                        .success(function(data, status, headers, config) {
                            $scope.message.text ='';
                            $rootScope.get_messages();
                        })
                        .error(function(data, status, headers, config) {
                            console.log('Error');
                            console.log(data);
                        });
                    console.log('test')
                }
            }
            else{
                console.log('Form not valid')
            }
        }
        $scope.upload = function (file,message) {
            console.log(message)
                Upload.upload({
                    url: '/api/messages/create/',
                    fields: message,
                    file: file,
                    fileFormDataName: 'file'
                }).then(function (resp) {
            console.log('Success ');
            $scope.message.text ='';
            var x = document.getElementsByName("file");
            for (var i = 0; i < x.length; i++) {
                x[i].value = null;
            }
            $rootScope.get_messages();
        }, function (resp) {
            console.log('Error status: ' + resp.status);
        });
    };
}]);



ChatApp.controller('ListMessagesController', ['$rootScope','$scope','$http','$interval',
    function($rootScope,$scope, $http, $interval) {
        $scope.messages = [];
        $rootScope.get_messages = function() {$http.get('/api/messages/list/',{})
            .success(function(data, status, headers, config) {
                $scope.messages = angular.copy(data);
                console.log($scope.messages)
            })
            .error(function(data, status, headers, config) {
               console.log('Error');
               console.log(data)
            })};
        $rootScope.get_messages()
        $interval($scope.get_messages,3000)
}]);




