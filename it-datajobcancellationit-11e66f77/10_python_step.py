import logging

import time

from vdk.api.job_input  import IJobInput

log = logging.getLogger(__name__)


def run(job_input: IJobInput):
    """
    Function named `run` is required in order for a python script to be recognized as a Data Job Python step and executed.

    VDK provides to every python step an object - job_input - that has methods for:

    * executing queries to OLAP Database.
    * ingesting data into Data Lake
    * processing Data Lake data into a dimensional model Data Warehouse.
    See IJobInput documentation
    """
    seconds = 120
    log.info(f"Starting tes job and sleepin for {seconds} seconds.")
    time.sleep(seconds)
    log.info(f"Exiting data job after sleeping for {seconds} seconds.")
