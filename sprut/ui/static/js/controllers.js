/**
 * Created by bova on 24.06.14.
 */

var sprutControllers = angular.module('sprutControllers', []);

sprutControllers.controller('SprutServerListCtrl', ['$resource', '$scope', 'SpServer', function ($resource, $scope, SpServer) {
    $scope.orderProp = 'id';

    $scope.page_number = 1;

    $scope.showTable = function(page) {
        var q = {order_by: [{field: 'id', direction: 'desc'}]};
        $scope.servers = SpServer.query({page: page, q: q});
    }
    $scope.delete = function(id) {
        SpServer.delete({id: id});
        $scope.showTable($scope.page_number);
    }

    $scope.servers = SpServer.query({page: 1});

}]);


sprutControllers.controller('SprutInstanceListCtrl', ['$resource', '$scope', '$location', 'SpInstance', '$interval',
    function($resource, $scope, $location, SpInstance, $interval) {
        $scope.showTable = function() {
            var page = 1;
            var q = {order_by: [{field: 'id', direction: 'desc'}]};
            $scope.instances = SpInstance.query({page: page, q: q});
        }

        $scope.delete = function(id) {
            SpInstance.delete({id: id});
            $scope.showTable($scope.page_number);
        }

        var q = {order_by: [{field: 'id', direction: 'desc'}]};
        $scope.instances = SpInstance.query({page: 1, q: q});
        repeat = $interval($scope.showTable, 140000);//140sec

        $scope.stop = function(instance_id) {
            SpInstance.update({id: instance_id, command: 'SHUTDOWN IMMEDIATE'});
            $scope.showTable($scope.page_number);
        }

        $scope.start = function(instance_id) {
            SpInstance.update({id: instance_id, command: 'STARTUP'});
            $scope.showTable($scope.page_number);
        }

}]);