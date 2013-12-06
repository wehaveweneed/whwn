define([
    'jquery',
    'backbone',
    'views/_navbar',
], function( $, Backbone, NavigationBarView ) {

    var InventoryRouter = Backbone.Marionette.AppRouter.extend({
        routes: {
          "inventory": "index",
        },
        initialize: function() {
          ItemMan.NavigationRegion.show(new NavigationBarView());
          this.navigate("inventory", {trigger: true, replace: true});
        },
        index: function() {
          console.log("Strange View.");
          ItemMan.MainRegion.close();
        },
    });

    return InventoryRouter;
});
