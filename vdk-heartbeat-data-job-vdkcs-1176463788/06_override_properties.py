
def run(job_input):
    props = job_input.get_all_properties()
    props['db'] = "memory.default"
    props['table_source'] = "vdk_heartbeat_source_vdkcs_1176463788"
    props['table_destination'] = "vdk_heartbeat_destination_vdkcs_1176463788"
    props['table_load_destination'] = "vdk_heartbeat_load_destination_vdkcs_1176463788"
    props['job_name'] = "vdk-heartbeat-data-job-vdkcs-1176463788"
    props['execute_template'] = "True"
    props['ingest_target'] = "vdk-heartbeat-datasource"
    props['ingest_method'] = "http"
    props['ingest_destination_table'] = "vdk_heartbeat_ingestion_test"
    props['ingest_timeout'] = "300"
    job_input.set_all_properties(props)
        