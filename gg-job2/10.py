from vdk.api.job_input import IJobInput
import logging

log = logging.getLogger(__name__)

def run(job_input: IJobInput):
    log.info("TEST")
