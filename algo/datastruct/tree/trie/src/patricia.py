#!/usr/bin/python

import string

# Patricia Trie definition
class Patricia:
    def __init__(self, value = None):
        self.value = value
        self.children = {}

# longest common prefix
# returns (p, s1', s2'), where p is lcp, s1'=s1-p, s2'=s2-p
def lcp(s1, s2):
    j=0
    while j<=len(s1) and j<=len(s2) and s1[0:j]==s2[0:j]:
        j+=1
    j-=1
    return (s1[0:j], s1[j:], s2[j:])

def branch(key1, tree1, key2, tree2):
    if key1 == "":
        #example: insert "an" into "antoher"
        tree1.children[key2] = tree2
        return tree1
    t = Patricia()
    t.children[key1] = tree1
    t.children[key2] = tree2
    return t

def insert(t, key, value = None):
    if t is None:
        t = Patricia()

    node = t
    while(True):
        match = False
        for k, tr in node.children.items():
            if key == k: # just overwrite
                node.value = value
                return t
            (prefix, k1, k2)=lcp(key, k)
            if prefix != "":
                match = True
                if k2 == "": 
                    # example: insert "antoher" into "an", go on traversing
                    node = tr
                    key = k1
                    break
                else: #branch out a new leaf
                    node.children[prefix] = branch(k1, Patricia(value), k2, tr)
                    del node.children[k]
                    return t
        if not match: # add a new leaf
            node.children[key] = Patricia(value)
            break
    return t

def to_string(t, prefix=""):
    str = "(" + prefix
    if t.value is not None:
        str += ":"+t.value
    for k, tr in sorted(t.children.items()):
        str += ", " + to_string(tr, prefix+k)
    str += ")"
    return str

def list_to_patricia(l):
    t = None
    for x in l:
        t = insert(t, x)
    return t

def map_to_patricia(m):
    t = None
    for k, v in m.items():
        t = insert(t, k, v)
    return t

class PatriciaTest:
    def run(self):
        self.test_lcp()
        self.test_insert()

    def test_lcp(self):
        print "test lcp"
        print lcp("om", "ub")
        print lcp("romane", "romanus")
        print lcp("an", "another")

    def test_insert(self):
        print "test insert"
        t = list_to_patricia(["a", "an", "another", "b", "bob", "bool", "home"])
        print to_string(t)
        t = list_to_patricia(["romane", "romanus", "romulus"])
        print to_string(t)
        t = map_to_patricia({"001":'y', "100":'x', "101":'z'})
        print to_string(t)
        t = list_to_patricia(["home", "bool", "bob", "b", "another", "an", "a"]);
        print to_string(t)

if __name__ == "__main__":
    PatriciaTest().run()
    