/**
 * Created by bova on 26.06.14.
 */

var sprutDirectives = angular.module('sprutDirectives', []);

sprutDirectives.directive('instancePanel', function() {
    return {
//        scope: true,//Use parent scope
        scope: { // isolated scope
            x: '=',
            instances: '=',
            stopInstance: '&',
            startInstance: '&'
        },
        link: function(scope, elem, attrs) {
            var x = attrs.x;
        },
        templateUrl: 'static/partials/instance/panel.html'
    };
});