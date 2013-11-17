define(['marionette', 'views/login'], function ( Marionette, LoginView ) {
    
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
      var loginView = new LoginView();
      ItemMan.MainRegion.show(loginView);
    });

    return ItemMan;
});
