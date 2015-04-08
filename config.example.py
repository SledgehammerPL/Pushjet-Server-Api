# Must be a mysql database!
database_uri = 'mysql://root@localhost/pushjet_api'

# Are we debugging the server?
# Do not turn this on when in production!
debug = True

# Limit requests?
limiter = False

# Google Cloud Messaging configuration (required for android!)
google_api_key = ''

# Message Queueing, this should be the relay
zeromq_relay_uri = 'ipc:///tmp/pushjet-relay.ipc'
