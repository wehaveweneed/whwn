/**
 *
 * Require.js allows us to configure shortcut alias
 */
var config = {
    baseUrl: "/static/js",
    paths: {
        "jquery"        : "components/jquery/jquery",
        "underscore"    : "components/underscore/underscore",
        "text"          : "components/requirejs-text/text",
        "marionette"    : "components/backbone.marionette/lib/backbone.marionette",
        "backbone"      : "components/backbone/backbone",
        "mustache"      : "components/mustache/mustache",
    },

    shim : {
        jquery: {
            exports: '$'
        },
        underscore: {
            exports: '_'
        },
        backbone: {
            deps: ['jquery', 'underscore', 'helpers/cookie_util'],
            exports: 'Backbone',
            init: function (jquery, underscore, cookie) {
                var oldSync = this.Backbone.sync;
                this.Backbone.sync = function(method, model, options) {
                    options.beforeSend = function(xhr) {
                        xhr.setRequestHeader('X-CSRFToken', cookie.find('csrftoken'));
                        xhr.setRequestHeader('Content-type', 'application/json');
                    };
                    return oldSync(method, model, options);
                };
            }
        },
        marionette: {
            deps: ['jquery', 'underscore', 'backbone'],
            exports: 'Marionette'
        },
        mustache: {
            exports: 'Mustache'
        }
    },

    // Application scripts to include in optimization
    modules: [
        { name: 'main'} 
    ],

    // Directory where our optimized files will be compiled to:
    // {{STATIC_URL}}/compiled/js/
    dir: "./static/compiled/js/",

    // This prevents unwanted file in the baseUrl from being copied to
    // the compiled/ folder before optimization.
    fileExclusionRegExp: /(^\.|.*test.*|compiled|css)(?!\.js$)/,

    // We need to change this later in production. This just speeds up the
    // grunt watch task.
    optimize: "none"
};

if (typeof exports === 'object') {
    module.exports = config;
} else if (typeof define === 'function' && define.amd) {
    // If this file is being loaded in the browser, load the config
    define([], function() {
        requirejs.config(config);
    });
}

