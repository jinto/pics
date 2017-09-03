Docker build and run
--------------------

create postgres docker named 'postgres1'

```
sudo docker build -t pics .
HOSTIP=`ip -4 addr show scope global dev eth0 | grep inet | awk "{print \$2}" | cut -d / -f 1`
sudo docker run -d -p 8000:8000 -it --link=postgres1 --add-host=docker:${HOSTIP} --name pics_instance -v /volume2/DISKZZZ/zz_django:/src -v /volume2/DISKZZZ/zz_folder01:/src/media/folder01 -v /volume2/DISKZZZ/zz_dropbox_pics:/src/media/folder02 pics
```

if you want to see console log change '-d' to '--rm'

Docker stop
-----------
```
sudo docker stop pics_instance

docker stop pics_instance
docker rm pics_instance
```


migrate
-------
To run migrate

```
sudo docker exec -it pics_instance /bin/bash
./manage migrate
```

scan files
----------
```
sudo docker exec -it pics_instance ./manage.py scan
```

postgresql
----------
ref : https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04
# confirm 
```
sudo docker exec -it postgres1 /bin/bash
psql -U postgres 
createuser -U postgres --interactive
createdb -U postgres pics
```
