# DBT Repository

This repository contains configurations and models for managing data transformations using [dbt (Data Build Tool)](https://www.getdbt.com/). dbt enables efficient data transformations in your data warehouse by providing a framework for SQL-based transformations, dependency management, testing, and documentation.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Setup](#setup)
3. [Key Commands](#key-commands)
    - [dbt debug](#dbt-debug)
    - [dbt run](#dbt-run)
    - [dbt test](#dbt-test)
    - [dbt docs](#dbt-docs)
4. [Configuration Files](#configuration-files)
    - [dbt_project.yml](#dbt_projectyml)
    - [profiles.yml](#profilesyml)
5. [Environment Variables](#environment-variables)
6. [Contributing](#contributing)

---

## Getting Started

This repository is designed for use with dbt. To begin, ensure you have dbt installed and properly configured. Follow the [official installation guide](https://docs.getdbt.com/docs/getting-started/installation).

---

## Setup

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd <repo_name>
   ```
2. Install dbt:
    ```bash
    pip install dbt-core 
    pip install dbt-postgres
    pip install dbt-snowflake
    pip install python-dotenv
    ```
3. Set up your profiles in `~/.dbt/profiles.yml.` 
Example:
    ```yaml
    my_project:
        outputs:
            postgres_dev:
            type: postgres
            host: "{{ env_var('POSTGRES_HOST') }}"
            user: "{{ env_var('POSTGRES_USER') }}"
            password: "{{ env_var('POSTGRES_PASSWORD') }}"
            port: "{{ env_var('POSTGRES_PORT') }}"
            dbname: "{{ env_var('POSTGRES_DB') }}"
            schema: public
            snowflake_dev:
            type: snowflake
            account: "{{ env_var('SNOWFLAKE_ACCOUNT') }}"
            user: "{{ env_var('SNOWFLAKE_USER') }}"
            password: "{{ env_var('SNOWFLAKE_PASSWORD') }}"
            role: "{{ env_var('SNOWFLAKE_ROLE') }}"
            database: "{{ env_var('SNOWFLAKE_DATABASE') }}"
            warehouse: "{{ env_var('SNOWFLAKE_WAREHOUSE') }}"
            schema: "{{ env_var('SNOWFLAKE_SCHEMA') }}"
        target: postgres_dev
    ```

---

## Key Commands

### dbt debug
Tests whether dbt can connect to the database and verifies configurations.

**Usage**:
```bash
dbt debug --target <target_name>
```
**Example**:
```bash
dbt debug --target postgres_dev
```

---

### dbt run

Executes all models or a specific set of models in the project.

**Usage**:
```bash
dbt run [--select <model_name_or_path>]
```
**Example**:
Run all models:
```bash
dbt run
```
Run specific models:
```bash
dbt run --select my_model
dbt run --select path/to/models/
```

---

### dbt test

Executes tests defined in the project to ensure data quality.

**Usage**:

```bash
dbt test [--select <model_name_or_path>]
```

**Example**:

```bash
dbt test
```

---

### dbt docs
Generates and serves documentation for your project.

**Usage**:
Generate documentation:
```bash
dbt docs generate
```
Serve documentation:
```bash
dbt docs serve
```

---

## Configuration Files

### dbt_project.yml
Defines project-level configurations, such as model paths, materialization, and environment-specific settings.

**Example**:
```yaml
# dbt_project.yml
name: multi_warehouse_project
version: 1.0.0
profile: multi_warehouse_profile  # profiles.yml의 Profile 이름
model-paths: ["models"]
# Models 설정
models:
multi_warehouse_project:
    postgres:  # PostgreSQL 전용 모델
    +materialized: table # 테이블로 저장
    +enabled: "{{ (target and target.name == 'postgres_dev') | default(false) }}"  # Postgres 타겟에서만 실행
    snowflake:  # Snowflake 전용 모델
    +materialized: table # view로 저장
    +enabled: "{{ (target and target.name == 'snowflake_dev') | default(false) }}"  # Snowflake 타겟에서만 실행
```

### profiles.yml
Specifies database connection details and environment-specific configurations.

**Example**:
```yaml
multi_warehouse_profile:  # Profile 이름
outputs:
    postgres_dev:  # PostgreSQL 환경
    type: postgres
    host: "{{ env_var('POSTGRES_HOST') }}"
    user: "{{ env_var('POSTGRES_USER') }}"
    password: "{{ env_var('POSTGRES_PASSWORD') }}"
    port: "{{ env_var('POSTGRES_PORT') }}"
    dbname: "{{ env_var('POSTGRES_DB') }}"        
    schema: "{{ env_var('POSTGRES_SCHEMA') }}"   
    threads: 1
    snowflake_dev:  # Snowflake 환경
    type: snowflake
    account: "{{ env_var('SNOWFLAKE_ACCOUNT') }}"
    user: "{{ env_var('SNOWFLAKE_USER') }}"
    password: "{{ env_var('SNOWFLAKE_PASSWORD') }}"
    role: "{{ env_var('SNOWFLAKE_ROLE') }}"
    database: "{{ env_var('SNOWFLAKE_DATABASE') }}"
    warehouse: "{{ env_var('SNOWFLAKE_WAREHOUSE') }}"
    schema: "{{ env_var('SNOWFLAKE_SCHEMA') }}"
    threads: 1
target: postgres_dev  # 기본 사용할 환경 (postgres_dev or snowflake_dev)
```

---

### Environment Variables
Sensitive credentials like database hostnames, usernames, and passwords should be stored as environment variables.

**Example**:
    
```bash
export POSTGRES_HOST="localhost"
export POSTGRES_USER="my_user"
export POSTGRES_PASSWORD="my_password"
```

Use `env_var()` to reference these variables in `dbt_project.yml` or `profiles.yml`.

---

### Contributing
1. Fork the repository.
2. Create a new feature branch:
    ```bash
    git checkout -b feature/my-new-feature
    ```

3. Commit your changes:
    ```bash
    git commit -m "Add my new feature"
    ```
4. Push to the branch:
    ```bash
    git push origin feature/my-new-feature
    ```
5. Open a pull request.

---

### License
This project is licensed under the MIT License.

```arduino
This `README.md` provides clear instructions and examples for using and configuring your dbt repository. It includes setup steps, command usage, and configuration file details, making it easy for users and contributors to get started.
```