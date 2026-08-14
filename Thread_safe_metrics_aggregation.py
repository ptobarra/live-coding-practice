"""
Thread-safe shared-metrics aggregation across worker threads.

Original scenario: an ML data-processing pipeline where multiple worker
threads each process a chunk of items and need to update two shared
counters — total items processed and total errors encountered.

Two bugs were identified in the original version and fixed here:

1. Loop-scope bug: `total_errors` was being incremented once per ITEM
   inside the processing loop, instead of once per CHUNK. Since
   `errors_in_chunk` is already a per-chunk total, this inflated the
   error count by a factor of `items_in_chunk` (e.g. 200 items x 2
   errors incorrectly produced 400 instead of 2).

2. Race condition: `total_items_processed += 1` (and the equivalent
   `+=` on `total_errors`) is not atomic - it's a read, a modify, and
   a write as three separate steps. When multiple threads perform this
   sequence concurrently on the same shared variable, updates can be
   silently lost (thread B reads the value before thread A's write is
   visible, then overwrites it). This is fixed by:
     - accumulating each thread's item count in a LOCAL variable
       during the loop (no shared-state contention while looping), and
     - updating both shared counters together inside a single
       `threading.Lock()`-protected critical section, so only one
       thread can read-modify-write the shared state at a time.
"""

import threading

total_items_processed = 0
total_errors = 0

# Guards the two shared counters below. Any code that reads-then-writes
# total_items_processed or total_errors must hold this lock.
metrics_lock = threading.Lock()


def process_data_chunk(items_in_chunk: int, errors_in_chunk: int) -> None:
    """Process a chunk of items and update the shared metrics.

    Args:
        items_in_chunk: number of items in this chunk.
        errors_in_chunk: total number of errors encountered in this chunk.
    """

    global total_items_processed, total_errors

    local_items_processed = 0

    for _ in range(items_in_chunk):
        # ... processing ...
        local_items_processed += 1

    # Single critical section: both shared counters are updated together,
    # while holding the lock, so no other thread can interleave here.
    with metrics_lock:
        total_items_processed += local_items_processed
        total_errors += errors_in_chunk

    # Manual alternative:
    # metrics_lock.acquire()
    # try:
    #     total_items_processed += local_items_processed
    #     total_errors += errors_in_chunk
    # finally:
    #     metrics_lock.release()


def main():
    chunks = [
        # (items_in_chunk, errors_in_chunk)
        (100, 0),
        (200, 2),
        (150, 1),
    ]

    threads = []

    for worker_id, (items, errors) in enumerate(chunks):
        thread = threading.Thread(
            target=process_data_chunk,
            args=(items, errors),
            name=f"worker-{worker_id}",
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Total items processed: {total_items_processed}")
    print(f"Total errors: {total_errors}")


if __name__ == "__main__":
    main()
