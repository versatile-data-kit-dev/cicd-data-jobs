import logging

import time

from taurus.api.job_input import IJobInput

log = logging.getLogger(__name__)


def run(job_input: IJobInput):
    log.info(f"Get current properties ")
    props = job_input.get_all_properties()
    props['now'] = time.time()
    log.info(f"Save new properties ")
    job_input.set_all_properties(props)
    log.info(f"Updated property now to {props['now']}")