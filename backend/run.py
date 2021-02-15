"""Run app module"""

from api.integration import weather_api
from api.app import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
