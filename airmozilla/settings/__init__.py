from .base import *
try:
    from .local import *
except ImportError, exc:
    exc.args = tuple([
        '%s (did you rename airmozilla/settings/local.py-dist?)' % (
            exc.args[0],
        )
    ])
    raise exc
