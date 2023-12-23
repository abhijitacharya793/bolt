from enum import Enum


class ScanTypes(Enum):
    recon = 1
    fuzzing = 2
    injection = 3
    vulnerability = 4
    all = 5
    manual = 6
    testing = 7
