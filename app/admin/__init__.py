''' Init admin '''
from flask import Blueprint

admin = Blueprint('admin', __name__)

import logging
from datetime import datetime as dt
from flask import current_app as app
from flask import request
from . import users, hosts, groups, auth
from ..resources import errors

@admin.after_request
def after_request(response):
    """ Logging after every request. """
    access_logger = logging.getLogger("app.access")
    ip = request.environ.get("X-Forwarded-For", request.remote_addr)
    access_logger.info(
        "%s [%s] %s %s %s %s %s %s %s",
        ip,
        dt.utcnow().strftime("%d/%b/%Y:%H:%M:%S.%f")[:-3],
        request.method,
        request.path,
        request.scheme,
        response.status,
        response.content_length,
        request.referrer,
        request.user_agent,
    )
    return response
