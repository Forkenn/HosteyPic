#!/bin/bash

/usr/sbin/rsyslogd
/usr/sbin/opendkim -x /etc/opendkim/opendkim.conf
/usr/sbin/postfix start-fg

sleep 3

touch /var/log/mail.log; tail -f /var/log/mail.log