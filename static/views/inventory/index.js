define([
    'jquery',
    'marionette'
], function($, Marionette) {
    var Inventory = Marionette.ItemView.extend({
        tagName: "div",
        id: "inventory",
        template: function() {
          return _.template("This is a placeholder for inventory stuff.");
          //return _.template(SignInTpl);
        },
        serializeData: function() {
          return { "tmp": "tmp" };
        },
        events: {
        },
        onRender: function () {
          /* Temporary classes for distinguishing this view visually */
          this.$el.css("height", "100%");
          this.$el.css("background", "beige");
        }
    });

    return Inventory;
});
