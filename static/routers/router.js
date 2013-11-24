define([
    'jquery',
    'backbone',
    'views/signin',
    'views/signup'
], function( $, Backbone, SignInView, SignUpView ) {

    var Router = Backbone.Marionette.AppRouter.extend({
        routes: {
          "signin": "signin",
          "signup": "signup",
          "signout": "signout"
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
