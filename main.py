# python3

def parallel_processing(n, m, data):
    output = []
    jobs_done = 0
    time = 0
    job_finish_time = [0] * n
    while jobs_done < m:
        for i in range(n):
            if job_finish_time[i] <= time:
                output.append((i, time))
                job_finish_time[i] = time + data[jobs_done]
                jobs_done += 1
                if jobs_done == m:
                    break
        time += 1

    return output

def main():
    # n - thread count 
    # m - job count
    text1 = input()
    n = int(text1.split()[0])
    m = int(text1.split()[1])

    data = list(map(int, input().split()))
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    result = parallel_processing(n,m,data)
    for i in range(m):
        print(result[i][0], result[i][1])


if __name__ == "__main__":
    main()
