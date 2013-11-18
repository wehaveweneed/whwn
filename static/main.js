define(['marionette', 'views/signin', 'routers/router'],
function ( Marionette, SignInView, ItemManRouter ) {
    
    var ItemMan = new Marionette.Application();
    ItemMan.on('initialize:before', function(options) {
      ItemMan.router = new ItemManRouter();
      ItemMan.addRegions({
        NavigationRegion: "#navigation",
        MainRegion: "#application",
        FooterRegion: "#footer"
      });
    });
    ItemMan.on('initialize:after', function(options) {
      // Temporarily navigate here for dev purposes
      Backbone.history.start({
        pushState: true
      });
    });

    window.ItemMan = ItemMan;
    return ItemMan;
});
