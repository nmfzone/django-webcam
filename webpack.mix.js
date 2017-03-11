const { mix } = require('laravel-mix')
require('./webpack.config')


/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel application. By default, we are compiling the Sass
 | file for the application as well as bundling up all the JS files.
 |
 */

mix.sass('assets/sass/app.scss', 'css')
   .js('assets/js/app.js', 'js');
