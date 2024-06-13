from . import app
import secure
import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

secure_headers = secure.Secure(server=secure.Server())

app = Flask(__name__, instance_relative_config=True)
app.secret_key = os.urandom(24)
""" app.config.from_object("defaults")
app.config.from_envvar("RAMEN_CONFIG", silent=True) """



@app.after_request
def set_secure_headers(response):
    secure_headers.framework.flask(response)
    return response


from authlib.integrations.flask_client import OAuth

oauth = OAuth(app)

google = oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    # access_token_url='https://accounts.google.com/o/oauth2/token',
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    # authorize_url='https://accounts.google.com/o/oauth2/auth',
    client_kwargs={"scope": "openid profile email"},
    # userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo'
)
