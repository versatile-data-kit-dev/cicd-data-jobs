
def run(job_input):
    props = job_input.get_all_properties()
    props['db'] = "memory.default"
    props['table_source'] = "vdk_heartbeat_source_yzhivkova_1631913832"
    props['table_destination'] = "vdk_heartbeat_destination_yzhivkova_1631913832"
    props['table_load_destination'] = "vdk_heartbeat_load_destination_yzhivkova_1631913832"
    props['job_name'] = "vdk-heartbeat-data-job-yzhivkova-1631913832"
    job_input.set_all_properties(props)
        