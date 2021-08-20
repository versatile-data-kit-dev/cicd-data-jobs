
def run(job_input):
    props = job_input.get_all_properties()
    props['db'] = "taurus_testing_sandbox"
    props['table_source'] = "vdk_heartbeat_source_mzhivkov_1629471407"
    props['table_destination'] = "vdk_heartbeat_destination_mzhivkov_1629471407"
    props['table_load_destination'] = "vdk_heartbeat_load_destination_mzhivkov_1629471407"
    props['job_name'] = "vdk-heartbeat-data-job-mzhivkov-1629471407"
    job_input.set_all_properties(props)
        