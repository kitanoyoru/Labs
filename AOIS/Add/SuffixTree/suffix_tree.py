from typing import Any, Dict


class Node:
    def __init__(self) -> None:
        self.suffix_link = -1


class Edge:
    def __init__(
        self,
        first_char_index: int,
        last_char_index: int,
        source_node_index: int,
        dest_node_index: int,
    ) -> None:
        self.first_char_index = first_char_index
        self.last_char_index = last_char_index
        self.source_node_index = source_node_index
        self.dest_node_index = dest_node_index

    @property
    def length(self) -> int:
        return self.last_char_index - self.first_char_index


class Suffix:
    def __init__(
        self, source_node_index: int, first_char_index: int, last_char_index: int
    ) -> None:
        self.source_node_index = source_node_index
        self.first_char_index = first_char_index
        self.last_char_index = last_char_index

    @property
    def length(self) -> int:
        return self.last_char_index - self.first_char_index

    def explicit(self) -> bool:
        return self.first_char_index > self.last_char_index

    def implicit(self) -> bool:
        return self.last_char_index >= self.first_char_index


class SuffixTree:
    def __init__(self, s: str, case_insensitive: bool = False):
        self.string = s

        self.case_insensitive = case_insensitive
        self.N = len(s) - 1

        self.nodes = [Node()]
        self.edges: Dict[Any, Edge] = {}
        self.active = Suffix(0, 0, -1)

        if self.case_insensitive:
            self.string = self.string.lower()
        for i in range(len(s)):
            self._add_prefix(i)

    def find_substring(self, substring):
        if not substring:
            return -1
        if self.case_insensitive:
            substring = substring.lower()
        curr_node = 0
        i = 0
        while i < len(substring):
            edge = self.edges.get((curr_node, substring[i]))
            if not edge:
                return -1
            ln = min(edge.length + 1, len(substring) - i)
            if (
                substring[i : i + ln]
                != self.string[edge.first_char_index : edge.first_char_index + ln]
            ):
                return -1
            i += edge.length + 1
            curr_node = edge.dest_node_index
        return edge.first_char_index - len(substring) + ln

    def has_substring(self, substring):
        return self.find_substring(substring) != -1

    def _add_prefix(self, last_char_index):
        last_parent_node = -1
        while True:
            parent_node = self.active.source_node_index
            if self.active.explicit():
                if (
                    self.active.source_node_index,
                    self.string[last_char_index],
                ) in self.edges:
                    break
            else:
                e = self.edges[
                    self.active.source_node_index,
                    self.string[self.active.first_char_index],
                ]
                if (
                    self.string[e.first_char_index + self.active.length + 1]
                    == self.string[last_char_index]
                ):
                    break
                parent_node = self._split_edge(e, self.active)

            self.nodes.append(Node())
            e = Edge(last_char_index, self.N, parent_node, len(self.nodes) - 1)
            self._insert_edge(e)

            if last_parent_node > 0:
                self.nodes[last_parent_node].suffix_link = parent_node
            last_parent_node = parent_node

            if self.active.source_node_index == 0:
                self.active.first_char_index += 1
            else:
                self.active.source_node_index = self.nodes[
                    self.active.source_node_index
                ].suffix_link
            self._canonize_suffix(self.active)
        if last_parent_node > 0:
            self.nodes[last_parent_node].suffix_link = parent_node
        self.active.last_char_index += 1
        self._canonize_suffix(self.active)

    def _insert_edge(self, edge):
        self.edges[(edge.source_node_index, self.string[edge.first_char_index])] = edge

    def _remove_edge(self, edge):
        self.edges.pop((edge.source_node_index, self.string[edge.first_char_index]))

    def _split_edge(self, edge, suffix):
        self.nodes.append(Node())
        e = Edge(
            edge.first_char_index,
            edge.first_char_index + suffix.length,
            suffix.source_node_index,
            len(self.nodes) - 1,
        )
        self._remove_edge(edge)
        self._insert_edge(e)
        self.nodes[
            e.dest_node_index
        ].suffix_link = suffix.source_node_index  ### need to add node for each edge
        edge.first_char_index += suffix.length + 1
        edge.source_node_index = e.dest_node_index
        self._insert_edge(edge)
        return e.dest_node_index

    def _canonize_suffix(self, suffix):
        if not suffix.explicit():
            e = self.edges[
                suffix.source_node_index, self.string[suffix.first_char_index]
            ]
            if e.length <= suffix.length:
                suffix.first_char_index += e.length + 1
                suffix.source_node_index = e.dest_node_index
                self._canonize_suffix(suffix)
