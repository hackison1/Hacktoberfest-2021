def find_max_child(i, heap, curr_size):
    # If the right node index is found to be greater than current size of the heap that means the right child is not present and the left child is the smallest one. So we return the left node
    if i * 2 + 1 > curr_size:
        return i * 2

    else:
        # If both children exist then we check which one is smaller and return that
        if heap[i * 2] > heap[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1


def shift_down(index, heap, curr_size):
    # This while loop runs until there are children present for the parent node at given index
    # And this is done by checking if left child node is present or not
    while index * 2 < curr_size:
        # Get the minimum child of the parent node
        max_child = find_max_child(index, heap, curr_size)

        # If the parent is greater than the minimum valued child then we swap them
        if heap[index] < heap[max_child]:
            heap[index], heap[max_child] = heap[max_child], heap[index]
        # We then assign the index to index of minimum child
        index = max_child
        print(heap)


def build_heap(lst):
    # We assign the heap variable to this list and current size to its length
    heap = [0] + lst[:]
    curr_size = len(lst)

    # We start adjusting from the middle to the end parent
    i = curr_size // 2

    # Run this loop until we reach the leftmost element
    while i > 0:
        # Call shiftdown method on the parent index
        shift_down(i, heap, curr_size)
        # Keep going to left
        i -= 1

    end = len(heap) - 1
    while end > 0:
        heap[end], heap[0] = heap[0], heap[end]
        shift_down(0, heap, end - 1)
        end -= 1
    return heap


if __name__ == "__main__":
    alist = [12, 2, 4, 5, 2, 3, 7, 1]

    print('Sorted Array:', build_heap(alist))
