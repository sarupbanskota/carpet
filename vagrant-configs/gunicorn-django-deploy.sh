#!/bin/bash
#
# Source: http://senko.net/en/django-nginx-gunicorn/

set -e
LOGFILE=/var/log/gunicorn/hello.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=vagrant
GROUP=vagrant
cd /vagrant/carpet/
#source ../bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec /usr/local/bin/gunicorn_django -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE
