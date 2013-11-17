define([
  'jquery',
  'marionette',
  'text!templates/login.html'
], function($, Marionette, LoginTpl) {
  var Login = Marionette.ItemView.extend({
      template: function() {
        return _.template(LoginTpl);
      },
      serializeData: function() {
        return { "tmp": "tmp" };
      }
  });

  return Login;
});
