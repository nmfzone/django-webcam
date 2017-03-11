const { mix } = require('laravel-mix')
const path = require('path')
const root = path.resolve(__dirname)


/*
 |--------------------------------------------------------------------------
 | Extended Mix Configuration
 |--------------------------------------------------------------------------
 |
 | Here we define our custom Configuration.
 |
 */

mix.setPublicPath('./public/static')
    .webpackConfig({
        //
    });
