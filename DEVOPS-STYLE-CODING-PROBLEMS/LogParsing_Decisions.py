logs = [
    "build SUCCESS",
    "unit-tests SUCCESS",
    "integration-tests FAILURE",
    "deploy SKIPPED"
]





def analyze_ci_logs(logs):
    freq={}
    for job in logs:
        jobs,job_status=job.split()
        freq[job_status]=freq.get(job_status,0)+1
        if job_status=="FAILURE":
            return freq,"FAIL"
    return freq,"PASS"
print(analyze_ci_logs(logs))