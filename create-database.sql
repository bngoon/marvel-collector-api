CREATE DATABASE marvelcollectors;

CREATE USER marvel_collector_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE marvelcollector TO marvel_collector_admin;

