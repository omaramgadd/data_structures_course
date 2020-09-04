from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        ft = self.finish_time
        at = request.arrived_at
        ttp = request.time_to_process
        while ft:
            if ft[0] <= at:
                ft.pop(0)
            else:
                break
        if len(ft) == self.size:
            return Response(True, -1)
        if len(ft) == 0:
            ft.append(at + ttp)
            return Response(False, at)
        ft.append(ttp + ft[-1])
        return Response(False, ft[-2])


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
