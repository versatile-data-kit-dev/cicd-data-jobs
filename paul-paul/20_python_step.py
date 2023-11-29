# Copyright 2021-2023 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0
import logging

from vdk.api.job_input import IJobInput
import torch


log = logging.getLogger(__name__)


def run(job_input: IJobInput):
    # Create a tensor
    x = torch.rand(5, 3)
    print("starting")
    print("A random tensor:")
    print(x)

    # Check if CUDA (GPU support) is available and print the tensor on GPU if available
    if torch.cuda.is_available():
        print("CUDA is available. Moving tensor to GPU.")
        x = x.to('cuda')
        print(x)
    else:
        print("CUDA not available. Tensor is on CPU.")

    print("PyTorch is working correctly!")
