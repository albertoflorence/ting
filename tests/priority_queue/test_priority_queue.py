import pytest
from ting_file_management.priority_queue import PriorityQueue

priority = {"nome_do_arquivo": "priority.txt", "qtd_linhas": 1}
priority_2 = {"nome_do_arquivo": "priority_2.txt", "qtd_linhas": 1}
low_priority = {"nome_do_arquivo": "low_priority.txt", "qtd_linhas": 10}
low_priority_2 = {"nome_do_arquivo": "low_priority_2.txt", "qtd_linhas": 6}


def test_basic_priority_queueing():
    queue = PriorityQueue()

    queue.enqueue(low_priority)
    queue.enqueue(priority)
    queue.enqueue(low_priority_2)
    queue.enqueue(priority_2)

    assert len(queue) == 4
    assert queue.dequeue() == priority
    assert queue.search(0) == priority_2
    assert queue.search(1) == low_priority
    assert queue.search(2) == low_priority_2

    with pytest.raises(IndexError):
        queue.search(3)
