
def run(job_input):
    props = job_input.get_all_properties()
    props['db'] = "taurus_testing_sandbox"
    props['table_source'] = "vdk_heartbeat_source_aivanov_1631774997"
    props['table_destination'] = "vdk_heartbeat_destination_aivanov_1631774997"
    props['table_load_destination'] = "vdk_heartbeat_load_destination_aivanov_1631774997"
    props['job_name'] = "vdk-heartbeat-data-job-aivanov-1631774997"
    job_input.set_all_properties(props)
        