module.exports = function(grunt) {

    var fs = require('fs'),
        // Import our requirejs configuration file
        config = require('./static/config'),
        spawn = require('child_process').spawn;

    // Load requirejs and clean grunt tasks
    grunt.loadNpmTasks('grunt-contrib-requirejs');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-contrib-stylus');
    grunt.loadNpmTasks('grunt-contrib-copy');
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
                    paths: ['static/components/bootstrap-stylus/stylus']
                },
                files: {
                    'static/compiled/css/screen.css': 'static/stylus/screen.styl',
                    'static/compiled/css/bootstrap.css': 'static/components/bootstrap-stylus/stylus/bootstrap.styl'
                }
            },
            production: {
                options: {
                    paths: ['static/components/bootstrap/stylus'],
                    cleancss: true
                },
                files: {
                    'static/compiled/css/screen.css': 'static/stylus/screen.styl',
                    'static/compiled/css/bootstrap.css': 'static/components/bootstrap-stylus/stylus/bootstrap.styl'
                }
            }
        },
        copy: {
            "fa-css": {
                src: 'static/components/font-awesome/css/font-awesome.css',
                dest: 'static/compiled/css/font-awesome.css'
            },
            "fa-fonts": {
                options: {
                    basePath: 'static/components/font-awesome/fonts'
                },
                files: [{
                    expand: true,
                    cwd: 'static/components/font-awesome/fonts/',
                    dest: 'static/compiled/fonts/',
                    src:['fontawesome-webfont.woff',
                         'fontawesome-webfont.ttf',
                         'fontawesome-webfont.svg']
                }]
            }
        },
        watch: {
            options: {
                livereload: true
            },
            stylus: {
                files: ['static/stylus/**/*.styl'],
                tasks: ['stylus:development']
            },
            js: {
                files: ['static/!(compiled)**/*.js', 'static/!(compiled)**/*.html',
                        'static/*.js'],
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
    grunt.registerTask('default', ['stylus:development', 'js', 'copy']);
};
