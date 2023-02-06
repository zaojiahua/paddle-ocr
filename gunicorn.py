import os


if not os.path.exists('log'):
    os.mkdir('log')

debug = False
loglevel = 'debug'
timeout = 600
bind = '0.0.0.0:8091'
pidfile = 'log/gunicorn.pid'
logfile = 'log/debug.log'
errorlog = 'log/error.log'
accesslog = 'log/access.log'

workers = 1

x_forwarded_for_header = 'X-FORWARDED-FOR'
