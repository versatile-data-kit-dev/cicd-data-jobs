import logging

import time

from vdk.api.job_input  import IJobInput

log = logging.getLogger(__name__)


def run(job_input: IJobInput):
    log.info("Testing we can still write to the ephemeral filesystem.")

    with open("test-file.txt", 'w') as f:
        f.write("Testing sentence.")

    with open("test-file.txt", 'r') as f:
        if str(f.read()) != 'Testing sentence.':
            raise Exception("File write was unsuccessful.")

    log.info("Testing we cannot write to the root filesystem.")

    try:
        with open("/test-file.txt", 'w') as f:
            f.write("Testing sentence.")
    except OSError:
        log.info("Root filesystem is read-only, as it should.")
    else:
        raise Exception("Root filesystem is not read-only")
