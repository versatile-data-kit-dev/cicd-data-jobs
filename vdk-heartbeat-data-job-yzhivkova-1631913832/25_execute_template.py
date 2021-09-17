# Copyright 2021 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0
import uuid


def run(job_input):
    ts = uuid.uuid4().hex
    db = job_input.get_property("db")
    target_table = f"vdk_heartbeat_dim_users_{ts}"
    source_table = f"vdk_heartbeat_vw_dim_users_{ts}"
    try:
        run_template_test(job_input, db, target_table, source_table)
    finally:
        job_input.execute_query(f"DROP TABLE IF EXISTS {db}.{target_table}")
        job_input.execute_query(f"DROP TABLE IF EXISTS {db}.{source_table}")


def run_template_test(job_input, db, target_table, source_table):
    # prepare source data
    job_input.execute_query(
        f"""
        CREATE TABLE IF NOT EXISTS {db}.{source_table}
        (
            id string,
            name string,
            username string,
            email string
        )
        """
    )
    job_input.execute_query(
        f"""
        INSERT INTO {db}.{source_table} VALUES
            ('id', 'A. Userov',  'auserov', 'auserov@example.com')
        """
    )

    # prepare target table
    job_input.execute_query(
        f"""
        DROP TABLE IF EXISTS {db}.{target_table}
        """
    )
    job_input.execute_query(
        f"""
        CREATE TABLE {db}.{target_table} (
            LIKE {db}.{source_table}
        )
        """
    )

    # execute template which will copy data from source to target
    template_args = {
        "target_schema": db,
        "target_table": target_table,
        "source_schema": db,
        "source_view": source_table,
    }
    job_input.execute_template(
        template_name="scd1", template_args=template_args
    )

    # check if target was correctly populated (only 1 entry from source should be inserted there)
    result = job_input.execute_query(f"SELECT COUNT (1) FROM {db}.{target_table}")

    if result and result[0][0] != 1:
        raise Exception("scd1 template did not work correctly.")
