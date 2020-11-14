from flask_assets import Bundle, Environment

from plane_stats import app

style_bundle = Bundle(
    'styles/main.css',
    output='gen/style.min.css'
)

js_bundle = Bundle(
    'js/app.js',
    'js/vendor/foundation.js',
    'js/vendor/jquery.js',
    output='gen/main.min.js'
)

assets = Environment(app)

assets.register('main_styles', style_bundle)
assets.register('main_js', js_bundle)
style_bundle.build()
js_bundle.build()