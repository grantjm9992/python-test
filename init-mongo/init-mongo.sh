#!/bin/bash

mongoimport --host mongo --db intelistyle_db --collection garments --file /docker-entrypoint-initdb.d/garments.jl
