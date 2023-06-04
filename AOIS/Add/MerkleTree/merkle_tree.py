import hashlib

from typing import List

OUTPUT: str = "merkle.txt"

class Node:
    def __init__(self, value: str) -> None:
        self.left, self.right = None, None
        self.value = value
        self.hash_value = hashlib.sha256(value.encode("utf=8")).hexdigest()


class MerkleTree:
    @classmethod
    def build(cls, values: List[str]) -> None:
        nodes = [Node(value) for value in values]

        with open(OUTPUT, "w+") as f:
            while len(nodes) != 1:
                temp = []
                for i in range(0, len(nodes), 2):
                    node_1 = nodes[i]
                    if i + 1 < len(nodes):
                        node_2 = nodes[i+1]
                    else:
                        temp.append(nodes[i])
                        break

                    f.write(f"Left  child | Value: {node_1.value} Hash: {node_1.hash_value}\n")
                    f.write(f"Right child | Value: {node_2.value} Hash: {node_2.hash_value}\n")

                    sumNode = node_1.hash_value + node_2.hash_value

                    parent = Node(sumNode)

                    parent.left = node_1
                    parent.right = node_2

                    f.write(f"Parent (left: {node_1.value} right: {node_2.value}) | Value: {parent.value} Hash: {parent.hash_value}\n\n")

                    temp.append(parent)
                nodes = temp

            f.write(f"Final Hash Trace: {nodes[0].hash_value}")


if __name__ == "__main__":
    values = ["hello", "world", "test", "example"]
    MerkleTree.build(values)





