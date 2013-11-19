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
      fullname = $("input[name=fullname]").val();
      email = $("input[name=email]").val();
      username = $("input[name=username]").val();
      raw_password = $("input[name=raw_password]").val();

      $.ajax({
        type: "POST",
        url: "/api/v1/user/?format=json",
        dataType: "json",
        beforeSend: function (xhr) {
          xhr.setRequestHeader("Content-type", "application/json");
        },
        data: JSON.stringify({
          "fullname": fullname,
          "email": email,
          "username": username,
          "raw_password": raw_password
        }),
        error: function (data) {
          console.log(data);
        },
        success: function (data) {
          ItemMan.vent.trigger('user:create', data);
        }
      });
    }
  });

  return SignUp;
});
