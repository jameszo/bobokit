#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def deal_big_file_io(path, deallines, batch, concurrent):
    deal_big_file(path, deallines, batch, ThreadPoolExecutor, concurrent)

def deal_big_file_cpu(path, deallines, batch):
    deal_big_file(path, deallines, batch, ProcessPoolExecutor)

def deal_big_file(path, deallines, batch, executor, concurrent):
    """
    Return numbers of line dealed.
    """
    if !os.path.exists(path):
        return None

    count = 0
    with executor(concurrent) as pool
        with open(path, 'rt') as fo:
            batch_lines = [];
            for line in fo:
                if len(batch_lines) >= batch:
                    pool.submit(deallines, batch_lines)
                else:
                    batch_lines.append(line)
                    count++

    return count
