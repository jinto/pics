Docker build and run
--------------------
```
sudo docker build . -t pics_django
sudo docker run -d -p 8000:8000 -it --name pics_django_instance -v /source_folder:/src -v /folder_source:/src/folder01  pics_django
```


migrate
-------
To run migrate

```
sudo docker exec -it pics_django_instance /bin/bash
./manage migrate
```
