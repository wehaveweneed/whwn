define(['marionette'], function ( Marionette ) {
    
    var ItemMan = new Marionette.Application();
    ItemMan.on('start', function(options) {
      Backbone.history.start({
        pushState: true,
        hashChange: false
      });
    });
    ItemMan.on('initialize:before', function(options) {
      options.apiRoot = '/api/v1';
    });
    ItemMan.on('initialize:after', function(options) {
      ItemMan.addRegions({
        mainApp: "#app"
      });
    });

    return ItemMan;
});
