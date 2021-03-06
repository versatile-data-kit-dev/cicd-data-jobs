# Copyright 2021 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0
import logging
import time
# from vacloud.api.job_input import IJobInput

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
    log.info(f"Starting job step {__name__}")
    print("Mzhivkov test job")
    print(f"Provided arguments: {job_input.get_arguments()}")
    time.sleep(1)
    
