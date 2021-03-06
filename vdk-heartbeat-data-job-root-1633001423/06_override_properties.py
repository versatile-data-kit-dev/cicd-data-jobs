
def run(job_input):
    props = job_input.get_all_properties()
    props['db'] = "memory.default"
    props['table_source'] = "vdk_heartbeat_source_root_1633001423"
    props['table_destination'] = "vdk_heartbeat_destination_root_1633001423"
    props['table_load_destination'] = "vdk_heartbeat_load_destination_root_1633001423"
    props['job_name'] = "vdk-heartbeat-data-job-root-1633001423"
    props['execute_template'] = "True"
    job_input.set_all_properties(props)
        