#!/bin/bash

curl -X POST localhost:8000/students -H "Content-Type: application/json" -d '{"userName": "Ivo", "passWord": "Ivanović"}'