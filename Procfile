web: bin/run_cloud_sql_proxy & wait $(jobs -p) && uvicorn app.main:app --host=0.0.0.0 --port=$PORT
