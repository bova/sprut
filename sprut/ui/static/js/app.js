/**
 * Created by bova on 24.06.14.
 */

/* App Module */
var sprutApp = angular.module('sprutApp', [
    'sprutServices',
    'ngResource',
    'ngRoute',
    'sprutControllers'
]);

sprutApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.when('/server', {
                templateUrl: 'static/partials/server.html',
                controller: 'SprutServerListCtrl'
            });
        $routeProvider.when('/instance', {
            templateUrl: 'static/partials/instance.html',
            controller: 'SprutInstanceListCtrl'
        });
        $routeProvider.when('/operation/upload', {
            templateUrl: 'static/partials/upload_update.html',
            controller: 'LZDOperationUploadCtrl'
        }).otherwise({
            redirectTo: '/server'
        });
    }]);