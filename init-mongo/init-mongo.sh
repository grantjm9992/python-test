#!/bin/bash

mongoimport --host localhost --db intelistyle_db --collection garments --file /docker-entrypoint-initdb.d/garments.jl
