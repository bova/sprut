/**
 * Created by bova on 26.06.14.
 */

var sprutDirectives = angular.module('sprutDirectives', []);

sprutDirectives.directive('instancePanel', function() {
    return {
//        scope: true,//Use parent scope
        scope: { // isolated scope
//            x: '=',
            instance: '=',
            stopInstance: '&',
            startInstance: '&'
        },
        link: function(scope, elem, attrs) {
            scope.getStatusColor = function() {
                console.log(scope.instance.id);
                if (scope.instance.status == 'OPEN') {
                    return 'green';
                } else if (scope.instance.status == 'CLOSED') {
                    return 'red';
                } else {
                    return 'grey';
                }
            };
        },
        templateUrl: 'static/partials/instance/panel.html'
    };
});