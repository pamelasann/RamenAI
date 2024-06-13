from . import app
import secure

secure_headers = secure.Secure(server=secure.Server())

@app.after_request
def set_secure_headers(response):
    secure_headers.framework.flask(response)
    return response
