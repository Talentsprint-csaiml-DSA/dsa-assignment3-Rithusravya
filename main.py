import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define comparison operators for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_map):
    # Create a priority queue (min-heap)
    priority_queue = [Node(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(priority_queue)

    # Build the Huffman tree
    while len(priority_queue) > 1:
        # Pop the two nodes with the lowest frequencies
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        
        # Create a new internal node with the sum of frequencies
        internal_node = Node(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right

        # Push the new internal node back into the priority queue
        heapq.heappush(priority_queue, internal_node)

    # Return the root of the Huffman tree
    return priority_queue[0]

def generate_huffman_codes(node, current_code="", code_map=defaultdict(str)):
    if node is None:
        return code_map

    # If this is a leaf node, store the code
    if node.char is not None:
        code_map[node.char] = current_code

    # Recursively generate the codes for the left and right children
    generate_huffman_codes(node.left, current_code + "0", code_map)
    generate_huffman_codes(node.right, current_code + "1", code_map)

    return code_map

def Huffman_coding(input_string):
    # Step 1: Count the frequency of each character
    freq_map = Counter(input_string)

    # Step 2: Build the Huffman tree
    root = build_huffman_tree(freq_map)

    # Step 3: Generate the Huffman codes
    huffman_codes = generate_huffman_codes(root)

    # Step 4: Encode the input string using the Huffman codes
    encoded_string = ''.join(huffman_codes[char] for char in input_string)

    return encoded_string

# Example usage
if __name__ == "__main__":
    input_string = "this is an example for huffman encoding"
    encoded_string = Huffman_coding(input_string)
    print(f"Encoded string: {encoded_string}")
