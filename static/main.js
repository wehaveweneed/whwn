define(['marionette', 'views/signin'], function ( Marionette, SignInView ) {
    
    var ItemMan = new Marionette.Application();
    ItemMan.on('start', function(options) {
      Backbone.history.start({
        pushState: true,
        hashChange: false
      });
    });
    ItemMan.on('initialize:before', function(options) {
      ItemMan.addRegions({
        NavigationRegion: "#navigation",
        MainRegion: "#application",
        FooterRegion: "#footer"
      });
    });
    ItemMan.on('initialize:after', function(options) {
      ItemMan.MainRegion.show(new SignInView());
    });

    return ItemMan;
});
