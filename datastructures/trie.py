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

    def delete(self, key):
        """
        If the key is present as a unique key as in it does not have any children nor are any of its nodes comprised of
         we should delete all of the nodes up to the root
        If the key is a prefix of another long key in the trie, umark the leaf node
        if the key is present in the trie and contains no children but contains nodes that are keys we should delete all
         nodes up to the first encountered key
        :param key:
        :return:
        """

        if not key:
            raise KeyError

        self._delete(key, self.root.children, None)

    def _delete(self, key, children: List[Leaf], parents: (List[Leaf], None), key_idx=0, parent_key=False):
        if not parents:
            parents = list()

        if key_idx >= len(key):
            return

        key_end = True if len(key) == key_idx + 1 else False
        suffix = key[key_idx]
        tmp_idx = key_idx
        for leaf in children:
            if leaf.data == suffix:
                # We're at the tail of the key and we have children
                if leaf.is_key:
                    parent_key = True

                if key_end and leaf.children:
                    # We've encountered another key along the way
                    if parent_key:
                        leaf.is_key = False
                    else:
                        # delete all nodes recursively up to the top of the first node that has multiple children
                        stop = False
                        while parents and not stop:
                            p = parents.pop()
                            # we have children, so walk back up the tree until we hit the first branch
                            # Locate our branch and kill its children
                            for i in range(len(p.children)):
                                if p.children[i].data == key[tmp_idx]:
                                    p.children.pop(i)  # children[i].children = []
                                    stop = True  # Need to stop processing a removal at a branch
                                    break
                            tmp_idx -= 1

                # We have reached the end of the key and there are no children
                elif key_end and not leaf.children:
                    stop = False
                    while parents and not stop:
                        p = parents.pop()
                        # we have children, so walk back up the tree until we hit the first branch
                        # Locate our branch and kill its children
                        for i in range(len(p.children)):
                            if p.children[i].data == key[tmp_idx]:
                                p.children.pop(i) # children[i].children = []
                                stop = True  # Need to stop processing a removal at a branch
                                break
                        tmp_idx -= 1

                # Not at the key end so we need to keep traversing the tree down
                parents.append(leaf)
                self._delete(key, leaf.children, parents, key_idx + 1, key_end)

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

    trie.delete('abd')  # Should only remove the d
    trie.delete('a')    # should unmark a as a key
    trie.delete('ba')   # should remove the ba trie
    trie.delete('bag')  # should only remove the g

    print(trie)

if __name__ == "__main__":
    main()
