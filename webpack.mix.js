const { mix } = require('laravel-mix')
require('./webpack.config')


/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your application.
 |
 */

mix.sass('assets/sass/app.scss', 'css')
   .js('assets/js/app.js', 'js');
