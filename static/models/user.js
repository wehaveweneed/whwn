define(['jquery', 'backbone'], function($, Backbone) {

  var User = Backbone.Model.extend({
    urlRoot: '/api/v1/user/'
  });

  return User;

});
