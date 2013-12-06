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
          "signout": "signout",
          "": "index",
        },
        initialize: function(options) {
          if (ItemMan.getRegion("NavigationRegion") !== undefined) {
            ItemMan.NavigationRegion.close();
          }
          this.navigate("signin", { trigger: true });
        },
        index: function() {
          ItemMan.MainRegion.show(new SignInView());
        },
        signin : function() {
          ItemMan.MainRegion.show(new SignInView());
          if (typeof ItemMan.currentUser === undefined || ItemMan.currentUser === null) {
          }
        },
        signup : function() {
          ItemMan.MainRegion.show(new SignUpView());
        }
    });

    return Router;
});
