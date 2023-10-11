
def run(job_input):
    props = job_input.get_all_properties()
    props['db'] = "taurus_testing_sandbox"
    props['table_source'] = "vdk_heartbeat_source_vdkcli_1032724790"
    props['table_destination'] = "vdk_heartbeat_destination_vdkcli_1032724790"
    props['table_load_destination'] = "vdk_heartbeat_load_destination_vdkcli_1032724790"
    props['job_name'] = "vdk-control-cli-release-test-job-1696998252"
    props['execute_template'] = "True"
    props['ingest_target'] = "vdk-heartbeat-datasource"
    props['ingest_method'] = "http"
    props['ingest_destination_table'] = "vdk_heartbeat_ingestion_test"
    props['ingest_timeout'] = "300"
    job_input.set_all_properties(props)
        