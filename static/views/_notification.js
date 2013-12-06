define([
    'jquery',
    'marionette',
    'handlebars',
    'text!templates/_notification.html'
], function($, Marionette, Handlebars, NavbarTpl) {
    var NotificationRegion = Marionette.ItemView.extend({
        tagName: "div",
        id: "navbar-container",
        template: Handlebars.compile(NavbarTpl),
        serializeData: function() {
          return { "current_user": "Lewis Chung" };
        },
        events: {
          "click #signout": "signout"
        },
        signout: function(e) {
          $.ajax({
            type: "POST",
            url: "/api/v1/user/signout/",
            error: function (data) {
              console.log(data);
            },
            success: function (data) {
              ItemMan.vent.trigger("session:destroy");
            }
          });
          return false;
        }
    });

    return NavigationBar;
});
