"""
I am writing a script that decides whether a CI pipeline should PASS or FAIL based on the result gotten from the CI
"""

"""
jobs = [
    ("build", "SUCCESS"),
    ("unit-tests", "SUCCESS"),
    ("integration-tests", "SKIPPED"),
    ("deploy", "SUCCESS")
]
"""

jobs = [
    ("build", "SUCCESS"),
    ("unit-tests", "SUCCESS"),
    ("integration-tests", "SKIPPED"),
    ("deploy", "SUCCESS")
]


def pipeline_fail_or_pass(jobs):
    for stage,result in jobs:
        if result=="FAILURE" or result=="SKIPPED":
            return "FAILED"
    return "PASSED"
print(pipeline_fail_or_pass(jobs))