import logging
import time

log = logging.getLogger(__name__)

def run(job_input):
    """
    Function named `run` is required in order for a python script to be recognized as a Data Job Python step and executed.

    VDK provides to every python step an object - job_input - that has methods for:

    * executing queries to OLAP Database.
    * ingesting data into Data Lake
    * processing Data Lake data into a dimensional model Data Warehouse.
    See IJobInput documentation
    """

    log.info(f"Job {__name__} started successfully")

    time.sleep(120) # Sleep for 2m minutes

    log.info(f"Job {__name__} finished successfully")
