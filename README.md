# Orea Microservice

### Docker Set up
To run build and run the detached servers

* `docker-compose up -d`

To run up into App server

* `docker exec -it lab-test-ms_django_1 /bin/bash`

To run server locally

* `pip install -r requirements/local.txt`
* `python manage.py runserver 0:8000`



# TODO
* Relax uniqueness on lab request sample_id field
* Implement @Percy's suggestion of tracking uniqueness using facility_id and id combination
