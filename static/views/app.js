define([
    'jquery',
    'underscore',
    'backbone',
    'text!templates/placeholder.html'
], function( $, _, Backbone, placeholderTemplate ) {

    var AppView = Backbone.View.extend({

        el: '#app',
        template: _.template( placeholderTemplate ), 
        initialize: function() {
            this.render();
        },
        render: function() {
            this.$el.html("PLACEHOLDER");
        }

    });

    return AppView;
});
