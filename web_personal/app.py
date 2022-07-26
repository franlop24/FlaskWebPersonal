############## Imports Flask & Python ##########
from flask import Flask
from flask_login import LoginManager

############## Imports Apps Blueprints ##########
from home.views import home_blueprint
from auth.views import auth_blueprint
from error_pages.handlers import error_pages
from projects.views import project_blueprint
from auth.models import get_user_by_id

##########  Creacion de App Flask ##########
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['ENV'] = 'development'

######### Configuracion de Flask Login ##########
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)

################# Registro de Apps ##################
app.register_blueprint(home_blueprint)
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(error_pages)
app.register_blueprint(project_blueprint, url_prefix='/project')

if __name__ == '__main__':
    app.run(debug=True)