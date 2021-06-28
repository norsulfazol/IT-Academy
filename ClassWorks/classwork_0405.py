#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randrange


def is_sorted(collection):
    return collection == sorted(collection)


def get_random_indexes(collection_lenght):
    rand_idx1, rand_idx2 = randrange(collection_lenght), randrange(collection_lenght)
    while rand_idx1 == rand_idx2:
        rand_idx2 = randrange(collection_lenght)
    return rand_idx1, rand_idx2


def try_sort(collection, idx1, idx2):
    collection[idx1], collection[idx2] = collection[idx2], collection[idx1]


if __name__ == '__main__':
    coll = [3, 1, 2, 8]
    coll_lenght = len(coll)
    counter = 0
    while not is_sorted(coll):
        try_sort(coll, *get_random_indexes(coll_lenght))
        print(coll)
        counter += 1
    print(counter)
