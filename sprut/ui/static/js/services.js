/**
 * Created by bova on 24.06.14.
 */

var sprutServices = angular.module('sprutServices', ['ngResource']);

sprutServices.factory('SpServer', ['$resource',
    function($resource){
        return $resource('api/sp_server/:id', {id:'@id'}, {
            'query': {
                    method: 'GET',
                    responseType: 'json',
                    isArray: true,
                    transformResponse: function(data, headersGetter) {
                        return data.objects;
            }},
            'update': {method: 'PATCH'}
        });
    }]);

sprutServices.factory('SpInstance', ['$resource',
    function($resource){
        return $resource('api/sp_ora_instance/:id', {id:'@id'}, {
            'query': {
                method: 'GET',
                responseType: 'json',
                isArray: true,
                transformResponse: function(data, headersGetter) {
                    return data.objects;
                }},
            'update': {method: 'PATCH'}
        });
    }]);