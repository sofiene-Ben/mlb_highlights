web: ./cloud_sql_proxy -instances=$INSTANCE_CONNECTION_NAME=tcp:5432 & uvicorn app.main:app --host=0.0.0.0 --port=$PORT
