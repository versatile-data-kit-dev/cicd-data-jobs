
def run(job_input):
    props = job_input.get_all_properties()
    props['db'] = "taurus_testing_sandbox"
    props['table_source'] = "vdk_heartbeat_source_gageorgiev_1631798765"
    props['table_destination'] = "vdk_heartbeat_destination_gageorgiev_1631798765"
    props['table_load_destination'] = "vdk_heartbeat_load_destination_gageorgiev_1631798765"
    props['job_name'] = "data-job-gageorgiev-1631798765"
    job_input.set_all_properties(props)
        