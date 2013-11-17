define([
    'jquery',
    'backbone'
], function( $, Backbone ) {

    var Router = Backbone.Marionette.AppRouter.extend({
        routes: {
          "login": "login"
        },
        login : function() {
          
        }
    });

    return Router;
});
