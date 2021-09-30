
def run(job_input):
    props = job_input.get_all_properties()
    props['db'] = "memory.default"
    props['table_source'] = "vdk_heartbeat_source_root_1632996757"
    props['table_destination'] = "vdk_heartbeat_destination_root_1632996757"
    props['table_load_destination'] = "vdk_heartbeat_load_destination_root_1632996757"
    props['job_name'] = "vdk-heartbeat-data-job-root-1632996757"
    props['execute_template'] = "True"
    job_input.set_all_properties(props)
        