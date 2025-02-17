import os

from deephyper_benchmark import *

DIR = os.path.dirname(os.path.abspath(__file__))


class FNOBenchmark(Benchmark):
    version = "0.0.1"

    requires = {
        "py-pip-requirements": {
            "type": "pip",
            "name": "-r " + os.path.join(DIR, "requirements.txt"),
        },
    }
