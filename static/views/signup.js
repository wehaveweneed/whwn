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
    },
    events: {
      "submit form.form": "submit"
    },
    submit: function(e) {
      e.preventDefault();

      $.ajax({
        type: "POST",
        url: "/api/v1/user/signup/",
        dataType: "json",
        data: JSON.stringify({
          "full_name": $("input[name=fullname]").val(),
          "email": $("input[name=email]").val(),
          "username": $("input[name=username]").val(),
          "raw_password": $("input[name=password]").val()
        }),
        error: function (data) {
          console.log(data);
        },
        success: function (data) {
          ItemMan.vent.trigger('session:create', data);
        }
      });
      return false;
    }
  });

  return SignUp;
});
