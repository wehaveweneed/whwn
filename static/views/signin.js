define([
  'jquery',
  'marionette',
  'text!templates/signin.html'
], function($, Marionette, LoginTpl) {
  var Signin = Marionette.ItemView.extend({
      tagName: "div",
      id: "signin-form-container",
      template: function() {
        return _.template(LoginTpl);
      },
      serializeData: function() {
        return { "tmp": "tmp" };
      }
  });

  return Signin;
});
