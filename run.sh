#！/bin/bash
cd /root/fuyangserver/fuyang/ENV35/bin/
source activate
cd /root/fuyangserver/fuyang/fuyangserver/
uwsgi --socket fuyangserver.sock --module fuyangserver.wsgi --buffer-size 65535  --chmod-socket=666
