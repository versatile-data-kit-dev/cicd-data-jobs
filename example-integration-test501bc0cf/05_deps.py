import time

from vacloud.api.job_input import IJobInput

import logging

log = logging.getLogger(__name__)

import json
import os
import pandas as pd
from edaoptics import datajob, quality
from datetime import datetime


import boto3
import numpy as np

def run(job_input: IJobInput):
    log.info('Starting {}'.format(__name__))




    log.info('Finished successfully {}'.format(__name__))
