from position import *


spmatrix = {}


def spmatrix_create(zero: float = 0) -> spmatrix:
    spmatrix.update({'zero': zero})
    return spmatrix


def spmatrix_is(mat: spmatrix) -> bool: #errado provavelmente
    return type(mat) is dict


def spmatrix_zero_get(mat: spmatrix) -> float:
    return mat['zero']


def spamtrix_zero_set(mat: spmatrix, zero:float):
    mat.update({'zero': zero})


def spmatrix_value_get(mat: spmatrix, pos: position) -> float:
    return mat[position]


def spmatrix_value_set(mat: spmatrix, pos: position, val: float):
    mat.update[pos: val]