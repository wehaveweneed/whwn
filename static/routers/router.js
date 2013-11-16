define([
    'jquery',
    'backbone'
], function( $, Backbone ) {

    var Router = Backbone.Router.extend({
        routes: {
          '': 'home'
        },
        home: function() {
          
        }
    });

    return Router;
});
