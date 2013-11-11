module.exports = function(grunt) {

    var fs = require('fs'),
        // Import our requirejs configuration file
        config = require('./static/config'),
        spawn = require('child_process').spawn;

    // Load requirejs and clean grunt tasks
    grunt.loadNpmTasks('grunt-contrib-requirejs');
    grunt.loadNpmTasks('grunt-contrib-clean');
    grunt.loadNpmTasks('grunt-sass');
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
        sass: {
            dev: {
                files: {
                    'static/compiled/css/screen.css': 'static/sass/screen.scss'
                }
            }
        },
        watch: {
            sass: {
                files: ['static/sass/**/*.scss'],
                tasks: ['clean', 'sass:dev']
            },
            js: {
                files: ['static/!(compiled)**/*.js'],
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

    // Default runs jshint, compiles js, compiles css
    // grunt.registerTask('default', 'jshint js sass:dev');

    // CSS task clears old ones and recompiles them
    // grunt.registerTask('css', 'clean compress');

    // Run django-compressor's compilation. `--force` regardless of DEBUG
    // grunt.registerTask('compress',
    //     'Compresses CSS from django_compressor', function () {

    //       var done = this.async(),
    //           sync = spawn('./manage.py', [ 'compress', '--force']);

    //       sync.stdout.setEncoding('utf8');
    //       sync.stderr.setEncoding('utf8');
    //       sync.stdout.on('data', function (data) { grunt.log.write(data); });
    //       sync.stderr.on('data', function (data) { grunt.log.error(data); });

    //       sync.on('exit', function (code) {
    //           if (code !== 0) {
    //               done(false);
    //           } else {
    //               done();
    //           }
    //       });
    //     }
    // );
};
