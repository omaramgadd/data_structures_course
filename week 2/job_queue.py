from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, t_jobs):
    result = []
    ft = [[0] * 2 for _ in range(n_workers)]
    for i in range(n_workers):
        ft[i][1] = i
    for time in t_jobs:
        hi = heapq.heappop(ft)
        result.append(AssignedJob(hi[1], hi[0]))
        hi[0] += time
        heapq.heappush(ft, hi)


    """
    result = []
    next_free_time = [0] * n_workers
    for time in t_jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += time
    """
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    t_jobs = list(map(int, input().split()))
    assert len(t_jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, t_jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
