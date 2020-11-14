from flask_assets import Bundle, Environment

from plane_stats import app

style_bundle = Bundle(
    'styles/main.css',
    output='gen/style.min.css'
)

assets = Environment(app)

assets.register('main_styles', style_bundle)
style_bundle.build()