#!/bin/sh

CONV="../../datastruct/tree/red-black-tree/src/rbt2dot.py"

$CONV -o img/tournament-tree-1.dot "(((((. 7 .) 7 (. 6 .)) 16:R ((. 15 .) 16:R (. 16:R .))) 16:R (((. 8 .) 8 (. 4 .)) 13 ((. 13 .) 13 (. 3 .)))) 16:R ((((. 5 .) 10 (. 10 .)) 10 ((. 9 .) 9 (. 1 .))) 14 (((. 12 .) 12 (. 2 .)) 14 ((. 11 .) 14 (. 14 .)))))"
