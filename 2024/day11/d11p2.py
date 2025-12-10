class LL:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def print_ll(node):
    while True:
        print(node.data, end=", ")
        if node.next is None:
            break
        node = node.next
    print()

stones = [int(x) for x in input().split()]

length = len(stones)
prev = None
for s in reversed(stones):
    new = LL(s, prev)
    prev = new
start = prev

blinks = 75

for b in range(blinks):
    print(b)
    prev_node = None
    curr_node = start
    while curr_node is not None:
        if curr_node.data == 0:
            curr_node.data = 1
            prev_node = curr_node
            curr_node = curr_node.next
            continue
        num_len = len(str(curr_node.data))
        if num_len%2 == 0:
            split_len = num_len//2
            second_half = LL(curr_node.data % (10**split_len), curr_node.next)
            first_half = LL(curr_node.data // (10**split_len), second_half)
            if prev_node is None:
                start = first_half
            else:
                prev_node.next = first_half
            length += 1
            prev_node = second_half
            curr_node = second_half.next
        else:
            curr_node.data *= 2024
            prev_node = curr_node
            curr_node = curr_node.next
    
print(length)