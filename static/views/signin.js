define([
    'jquery',
    'marionette',
    'text!templates/signin.html'
], function($, Marionette, SignInTpl) {
    var Signin = Marionette.ItemView.extend({
        tagName: "div",
        id: "signin-form-container",
        template: function() {
          return _.template(SignInTpl);
        },
        serializeData: function() {
          return { "tmp": "tmp" };
        },
        events: {
          'submit #signin-form': 'signin',
          'click #signout': 'signout'
        },
        signin: function(e) {
          $.ajax({
            type: 'POST',
            url: '/api/v1/user/signin/',
            dataType: "json",
            data: JSON.stringify({
              'username': $('input[name=username]').val(),
              'raw_password': $('input[name=password]').val()
            }),
            success: function(data) {
              ItemMan.vent.trigger('session:create', data);
            },
            error: function(data) {
              console.log(data);
            }
          });
          return false;
        },
        signout : function (e) {
          $.ajax({
            type: "POST",
            url: "/api/v1/user/signout/",
            error: function (data) {
              console.log(data);
            },
            success: function (data) {
              ItemMan.vent.trigger('session:destroy', data);
            }
          });
          return false;
        }
    });

    return Signin;
});
