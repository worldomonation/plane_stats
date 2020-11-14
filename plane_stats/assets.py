from flask_assets import Bundle, Environment

# from . import app

bundles = {
    'main_css': Bundle (
        'css/main.css',
        output='gen/main.css'
    )
}

# assets = Environment(app)

# assets.register(bundles)