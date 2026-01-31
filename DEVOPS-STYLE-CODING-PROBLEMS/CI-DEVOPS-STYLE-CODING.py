"""
PRINT CI JOBS
"""

jobs = [
    ("build", "SUCCESS"),
    ("unit-tests", "SUCCESS"),
    ("integration-tests", "FAILURE"),
    ("deploy", "SKIPPED")
]

"""
EXPECTED RESULT
{
    "SUCCESS": 2,
    "FAILURE": 1,
    "SKIPPED": 1
}
"""


def summarize_ci_jobs(jobs):
    freq={}
    for job,job_status in jobs:
        freq[job_status]=freq.get(job_status,0)+1
    return freq
print(summarize_ci_jobs(jobs))



"""
MY RESULT
{'SUCCESS': 2, 'FAILURE': 1, 'SKIPPED': 1}
"""