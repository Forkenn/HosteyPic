docker exec -i hosteypic_postgres sh -c "PGPASSWORD=my_secret_password psql --username admin db_hosteypic" < ./archives/dump_<year>_<month>_<day>.sql