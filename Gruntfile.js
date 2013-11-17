module.exports = function(grunt) {

    var fs = require('fs'),
        // Import our requirejs configuration file
        config = require('./static/config'),
        spawn = require('child_process').spawn;

    // Load requirejs and clean grunt tasks
    grunt.loadNpmTasks('grunt-contrib-requirejs');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-contrib-stylus');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-jshint');

    grunt.initConfig({
        pkg: '<json:package.json>',
        jshint: {
            all: [
                'static/!(compiled)**/*.js',
                'static/*.js',
                'Gruntfile.js'
            ]
        },
        clean: {
            folder: "static/compiled/css/"
        },
        requirejs: {
            compile: {
                options: config
            }
        },
        stylus: {
            development: {
                options: {
                    paths: ['static/components/bootstrap/stylus']
                },
                files: {
                    'static/compiled/css/screen.css': 'static/stylus/screen.styl'
                }
            },
            production: {
                options: {
                    paths: ['static/components/bootstrap/stylus'],
                    cleancss: true
                },
                files: {
                    'static/compiled/css/screen.css': 'static/stylus/screen.styl'
                }
            }
        },
        watch: {
            options: {
                livereload: true
            },
            stylus: {
                files: ['static/stylus/**/*.styl'],
                tasks: ['clean', 'stylus:development']
            },
            js: {
                files: ['static/!(compiled)**/*.js', 'static/!(compiled)**/*.html',
                        'static/*.js', 'Gruntfile.js'],
                tasks: ['jshint', 'requirejs'],
                options: {
                    spawn: false,
                }
            }
        }
    });

    // This should mirror the STATIC_URL in the django settings so
    // our optimizer picks it up.
    grunt.config.set('requirejs.compile.options.baseUrl', './static/');

    // Alias requirejs to js
    grunt.registerTask('js', 'requirejs');
};
