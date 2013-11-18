define([
  'jquery',
  'marionette',
  'text!templates/signup.html'
], function($, Marionette, SignUpTpl) {
  var SignUp = Marionette.ItemView.extend({
      tagName: "div",
      id: "signup-form-container",
      template: function() {
        return _.template(SignUpTpl);
      },
      serializeData: function() {
        return { "tmp": "tmp" };
      }
  });

  return SignUp;
});
