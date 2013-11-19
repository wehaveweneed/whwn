define(['marionette', 'views/signin', 'models/user', 'routers/router'],
function ( Marionette, SignInView, User, ItemManRouter ) {
    
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

    ItemMan.vent.on('user:create', function(data) {
      $('meta[name=user]').attr('content', data.username);
      $('meta[name=key]').attr('content', data.key);
      ItemMan.current_user = new User(data);
    });

    window.ItemMan = ItemMan;
    return ItemMan;
});
