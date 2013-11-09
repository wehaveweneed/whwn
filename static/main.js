define([
    'backbone',
    'views/app',
    'routers/router'
], function ( Backbone, AppView, Router ) {
    // Initialize routing and start Backbone.history()
    return function () {
        new Router();
        Backbone.history.start();

        new AppView();
    };
});
