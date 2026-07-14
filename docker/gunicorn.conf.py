"""
====================================================
 AgriNova AI v2.0
 Gunicorn Configuration
====================================================
"""

import multiprocessing

# --------------------------------------------------
# Server Socket
# --------------------------------------------------

bind = "0.0.0.0:8000"
backlog = 2048

# --------------------------------------------------
# Worker Configuration
# --------------------------------------------------

workers = max(2, multiprocessing.cpu_count())

worker_class = "gthread"

threads = 4

timeout = 120

graceful_timeout = 30

keepalive = 5

# --------------------------------------------------
# Restart Settings
# --------------------------------------------------

max_requests = 1000

max_requests_jitter = 50

# --------------------------------------------------
# Logging
# --------------------------------------------------

accesslog = "logs/gunicorn_access.log"

errorlog = "logs/gunicorn_error.log"

loglevel = "info"

capture_output = True

enable_stdio_inheritance = True

# --------------------------------------------------
# Process Naming
# --------------------------------------------------

proc_name = "agrinova_ai"

# --------------------------------------------------
# Security
# --------------------------------------------------

limit_request_line = 4094

limit_request_fields = 100

limit_request_field_size = 8190

# --------------------------------------------------
# Temporary Directory
# --------------------------------------------------

worker_tmp_dir = "/dev/shm"

# --------------------------------------------------
# Application Hooks
# --------------------------------------------------

def when_ready(server):
    server.log.info("AgriNova AI v2.0 server is ready.")


def on_starting(server):
    server.log.info("Starting AgriNova AI v2.0...")


def worker_int(worker):
    worker.log.info("Worker received INT or QUIT signal.")


def worker_abort(worker):
    worker.log.info("Worker aborted.")