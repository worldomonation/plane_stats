from flask import Flask

# Has to be in this order, with the routes imported at bottom due to
# circular import.
app = Flask(__name__)

from plane_stats import routes
from plane_stats import assets