from dotenv import load_dotenv
import os
import subprocess

# .env 파일 로드
load_dotenv()

os.environ['POSTGRES_DB']="infra_datahub"
os.environ['POSTGRES_SCHEMA']="datahub_meta"
# dbt 명령 실행
dbt_command = ["dbt", "debug", "--target","snowflake_dev"]
dbt_command = ["dbt", "debug", "--target","postgres_dev"]
dbt_command = ["dbt", "run", "--target","postgres_dev"]
# dbt_command = ["dbt", "debug"]
print(f"dbt_command:{dbt_command}")
subprocess.run(dbt_command, check=True, env=os.environ)
