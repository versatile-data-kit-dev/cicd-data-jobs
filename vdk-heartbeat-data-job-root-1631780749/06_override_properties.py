
def run(job_input):
    props = job_input.get_all_properties()
    props['db'] = "memory.default"
    props['table_source'] = "vdk_heartbeat_source_root_1631780749"
    props['table_destination'] = "vdk_heartbeat_destination_root_1631780749"
    props['table_load_destination'] = "vdk_heartbeat_load_destination_root_1631780749"
    props['job_name'] = "vdk-heartbeat-data-job-root-1631780749"
    job_input.set_all_properties(props)
        