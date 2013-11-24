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
      Backbone.history.start({
        pushState: true,
        root: "/i/"
      });
    });

    ItemMan.on('initialize:after', function(options) {
      var username = $('meta[name=user]').attr('content');
      if (username.length !== 0) {
        // Grab user details mang.
        ItemMan.currentUser = new User({id: username});
        ItemMan.currentUser.fetch();
      }
    });

    ItemMan.vent.on('session:create', function(data) {
      // This is how we tell if a user is logged in. Django has
      // matching logic on the index.html template.
      $('meta[name=user]').attr('content', data.username);
      ItemMan.currentUser = new User(data);
    });

    ItemMan.vent.on('session:destroy', function(data) {
      $('meta[name=user]').attr('content', '');
      ItemMan.currentUser = null;
    });

    window.ItemMan = ItemMan;
    return ItemMan;
});
