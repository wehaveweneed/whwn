define([
    'jquery',
    'backbone',
    'views/signin',
    'views/signup'
], function( $, Backbone, SignInView, SignUpView ) {

    var Router = Backbone.Marionette.AppRouter.extend({
        routes: {
          "": "signin",
          "signin": "signin",
          "signup": "signup"
        },
        signin : function() {
          ItemMan.MainRegion.show(new SignInView());
        },
        signup : function() {
          ItemMan.MainRegion.show(new SignUpView());
        }
    });

    return Router;
});
