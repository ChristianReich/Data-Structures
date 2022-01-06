"""
-------------------------------------------------------
Utilities
-------------------------------------------------------
Author:  Christian Reichenbach
ID:      190608390
Email:   reic8390@mylaurier.ca
__updated__ = "2021-02-10"
-------------------------------------------------------
"""
from List_array import List
from Priority_Queue_array import Priority_Queue
from Queue_array import Queue
from Stack_array import Stack


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    LENGTH = len(source)
    i = 0
    while i < LENGTH:
        stack.push(source.pop())
        i += 1
    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    LENGTH = len(stack._values)
    i = 0
    while i < LENGTH:
        value = stack.pop()
        target.insert(0, value)
        i += 1
    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    stack = Stack()
    result = stack.is_empty()
    if result:
        stack.push(source[0])
    else:
        stack.push(source[0])
        stack.pop()
        stack.peek()
    return


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    LENGTH = len(source)
    i = 0
    while i < LENGTH:
        queue.insert(source.pop(0))
        i += 1
    return


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    LENGTH = len(queue._values)
    i = 0
    while i < LENGTH:
        value = queue.remove()
        target.append(value)
        i += 1
    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    LENGTH = len(source)
    i = 0
    while i < LENGTH:
        pq.insert(source.pop(0))
        i += 1
    return


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    LENGTH = len(pq._values)
    i = 0
    while i < LENGTH:
        value = pq.remove()
        target.append(value)
        i += 1
    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()
    array_to_queue(q, a)
    val = 12

    empty_result = q.is_empty()
    q.insert(val)
    value = q.remove()
    value2 = q.peek()
    LENGTH = q.__len__()
    print("""Is_Empty: {}
    Remove: {}
    Peek: {}
    Length: {}""".format(empty_result, value, value2, LENGTH))
    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    array_to_queue(pq, a)
    val = 12
    empty_result = pq.is_empty()
    pq.insert(val)
    value = pq.remove()
    value2 = pq.peek()
    print("""Is_Empty: {}
    Remove: {}
    Peek: {}""".format(empty_result, value, value2))
    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    LENGTH = len(source)
    for i in range(LENGTH):
        val = source.pop(0)
        llist.append(val)
    return


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not llist.is_empty():
        target.append(llist.pop(0))
    return


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()
    array_to_list(lst, source)
    empty = lst.is_empty()
    lst.insert(0, 0)
    lst.remove(lst._values[0])
    count = lst.count(lst._values[0])
    lst.append(66)
    lst.index(lst._values[0])
    lst.find(lst._values[0])
    max = lst.max()
    min = lst.min()
    print("""Is_empty: {}
Count: {}
Max: {}Min: {}""".format(empty, count, max, min))

    return
