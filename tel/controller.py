from view import what_do, find_input, add_input
from func import find, add
from data_base import open_db
import csv


def start():
    what_do_ = what_do()

    if what_do_ == 1:
        find(find_input())
    elif what_do_ == 2:
        add(add_input())
