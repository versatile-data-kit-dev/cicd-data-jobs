
def run(job_input):
    props = job_input.get_all_properties()
    props['db'] = "taurus_testing_sandbox"
    props['table_source'] = "vdk_heartbeat_source_root_1628495102"
    props['table_destination'] = "vdk_heartbeat_destination_root_1628495102"
    props['table_load_destination'] = "vdk_heartbeat_load_destination_root_1628495102"
    props['job_name'] = "vdk-control-cli-release-test-job-1628495101"
    job_input.set_all_properties(props)
        