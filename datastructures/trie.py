"""
Mike McMahon
"""
from typing import List


class Trie(object):
    class Leaf(object):
        def __init__(self, data, is_key):
            self.data = data
            self.is_key = is_key
            self.children = []

        def __str__(self):
            return "{}{}".format(self.data, "*" if self.is_key else "")

    def __init__(self, keys):
        self.root = Trie.Leaf('', False)
        for key in keys:
            self.add_key(key)

    def add_key(self, key):
        self._add(key, self.root.children)

    def has_suffix(self, suffix):
        leaf = self._find(suffix, self.root.children)

        if not leaf:
            return False

        # This is only a suffix if the returned leaf has children and itself is not a key
        if not leaf.is_key and leaf.children:
            return True

        return False

    def includes_key(self, key):
        leaf = self._find(key, self.root.children)

        if not leaf:
            return False

        return leaf.is_key

    def _find(self, key, children: List[Leaf]):
        if not key:
            raise KeyError

        match = False
        if len(key) == 1:
            match = True

        suffix = key[0]
        for leaf in children:
            if leaf.data == suffix and not match:
                return self._find(key[1:], leaf.children)
            elif leaf.data == suffix and match:
                return leaf
        return None

    def _add(self, key, children: List[Leaf]):
        if not key:
            return

        is_key = False
        if len(key) == 1:
            is_key = True

        suffix = key[0]
        for leaf in children:
            if leaf.data == suffix:
                self._add(key[1:], leaf.children)
                break
        else:
            children.append(Trie.Leaf(suffix, is_key))
            self._add(key[1:], children[-1].children)

        return

    @staticmethod
    def _has_children(leaf):
        return bool(leaf.children)


def main():
    keys = ['ba', 'bag', 'a', 'abc', 'abcd', 'abd']
    trie = Trie(keys)
    print(trie.includes_key('ba'))  # True
    print(trie.includes_key('b'))  # False
    print(trie.includes_key('dog'))  # False
    print(trie.has_suffix('b'))  # True
    print(trie.has_suffix('ab'))  # True
    print(trie.has_suffix('abd'))   # False
    print(trie)

if __name__ == "__main__":
    main()