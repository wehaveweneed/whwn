define(['marionette',
        'views/signin',
        'views/inventory/index',
        'models/user',
        'routers/main',
        'routers/inventory'],
function(Marionette, SignInView, InventoryView, User, ItemManRouter, InventoryRouter) {
    
    var ItemMan = new Marionette.Application();
    ItemMan.on('initialize:before', function(options) {
      ItemMan.router = new ItemManRouter();
      ItemMan.addRegions({
        NavigationRegion: "#navigation",
        NotificationRegion: "#notifications",
        MainRegion: "#application",
        FooterRegion: "#footer"
      });
    });

    ItemMan.on('initialize:after', function(options) {
      Backbone.history.start({
        pushState: true
      });
    });

    ItemMan.on('initialize:after', function(options) {
      // On first initialize if user is already logged in
      // we want to fetch and populate the current_user model
      // and enable the navigation bar.
      var username = $('meta[name=user]').attr('content');
      if (username.length !== 0) {
        // Grab user details mang.
        ItemMan.currentUser = new User({id: username});
        ItemMan.currentUser.fetch();

        // Show inventory since signed in
        ItemMan.router = new InventoryRouter();
        ItemMan.MainRegion.show(new InventoryView());
      }
    });

    ItemMan.vent.on('session:create', function(data) {
      // When a user logs in his sesion is created. We get the
      // current user data and show the navigation bar.
      $('meta[name=user]').attr('content', data.username);
      ItemMan.currentUser = new User(data);

      // Load the inventory view
      ItemMan.router = new InventoryRouter();
      ItemMan.MainRegion.show(new InventoryView());
    });

    ItemMan.vent.on('session:destroy', function(data) {
      // When a user logs out of his session, we disable the
      // navigation bar and bring him to the signin screen.
      $('meta[name=user]').attr('content', '');
      ItemMan.currentUser = null;

      // Load the standard (not signed in view)
      ItemMan.router = new ItemManRouter({ goto: "signin" });
    });

    window.ItemMan = ItemMan;
    return ItemMan;
});
