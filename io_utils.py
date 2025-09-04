import threading, sys, time
from queue import Queue, Empty
import math

def input_with_timeout(prompt: str, seconds: int) -> tuple[bool, str | None]:
    q: Queue[str] = Queue()

    def reader():
        try:
            sys.stdout.write(f"\n{prompt}")
            sys.stdout.flush()
            val = input()
        except EOFError:
            val = ""
        q.put(val)

    thread = threading.Thread(target=reader, daemon=True)
    thread.start()

    end_time = time.time() + seconds
    last_remaining = None
    # Initial timer print
    sys.stdout.write(f"\r⏳ {seconds:2d} seconds remaining")
    sys.stdout.flush()

    while time.time() < end_time:
        remaining = math.ceil(end_time - time.time())
        if remaining != last_remaining:
            sys.stdout.write(f"\r⏳ {remaining:2d} seconds remaining")
            sys.stdout.flush()
            last_remaining = remaining
        try:
            val = q.get_nowait()
            sys.stdout.write("\n")  
            sys.stdout.flush()
            return True, val
        except Empty:
            time.sleep(0.1)

    sys.stdout.write("\n⏰ Time's up!\n")
    sys.stdout.flush()
    return False, None