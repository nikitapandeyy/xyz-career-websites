from sqlalchemy import create_engine, text
import os

db_conn_string = os.environ['DB_CONN_STRING']

engine = create_engine(db_conn_string,
                      connect_args={
                        "ssl":{
                          "ssl_ca":"/etc/ssl/cert.pem"
                        }
                      })



def load_job_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('select * from jobs'))
        jobs = [dict(row.items()) for row in result]
        return jobs



  

  
   

   
   
