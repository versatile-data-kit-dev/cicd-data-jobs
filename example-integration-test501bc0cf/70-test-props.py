import time

from vacloud.api.job_input import IJobInput

import logging

log = logging.getLogger(__name__)


def run(job_input: IJobInput):
    log.info('Starting {}'.format(__name__))

    props = dict(ts=time.time())
    job_input.get_all_properties()
    job_input.set_all_properties(props)
    # Though there is caching still let's try get
    persisted_props = job_input.get_all_properties()
    if persisted_props != props:
        raise Exception("persisted properties are different from original properties. "
                        "There might be an issue with Properties Service ...")
    log.info('Finished successfully {}'.format(__name__))
