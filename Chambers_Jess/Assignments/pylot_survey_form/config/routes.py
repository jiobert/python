
from system.core.router import routes


routes['default_controller'] = 'Surveys'

routes['POST']['/process'] = 'Surveys#process'
