/**
 *
 * Require.js allows us to configure shortcut alias
 */
var config = {
    baseUrl: "/static",
    paths: {
        "jquery"        : "components/jquery/jquery",
        "underscore"    : "components/underscore/underscore",
        "text"          : "components/requirejs-text/text",
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
            deps: ['underscore', 'jquery'],
            exports: 'Backbone'
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
};

if (typeof exports === 'object') {
    module.exports = config;
} else if (typeof define === 'function' && define.amd) {
    // If this file is being loaded in the browser, load the config
    define([], function() {
        requirejs.config(config);
    });
}

