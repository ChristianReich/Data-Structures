"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Christian Reichenbach
ID:      190608390
Email:   reic8390@mylaurier.ca
__updated__ = "2021-03-30"
-------------------------------------------------------
"""
# Imports
# Use any appropriate data structure here.
from Sorted_List_array import Sorted_List
# Define the new_slot slot creation function.
new_slot = Sorted_List

# Constants
SEP = '-' * 40


class Hash_Set:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, slots):
        """
        -------------------------------------------------------
        Initializes an empty Hash_Set of size slots.
        Use: hs = Hash_Set(slots)
        -------------------------------------------------------
        Parameter:
            slots - number of initial slots in Hash Set (int > 0)
        Returns:
            A new Hash_Set object (Hash_Set)
        -------------------------------------------------------
        """
        self._slots = slots
        self._table = []
        self._count = 0

        # Define the empty slots.
        for _ in range(self._slots):
            self._table.append(new_slot())

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the Hash Set.
        Use: n = len(hs)
        -------------------------------------------------------
        Returns:
            the number of values in the Hash Set.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the Hash Set is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Returns:
            True if the Hash Set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot(key)
        -------------------------------------------------------
        Returns:
            slot - list at the position of hash key in self._table
        -------------------------------------------------------
        """
        slot = hash(key) % self._slots
        return self._table[slot]

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Hash Set contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the Hash Set contains key, False otherwise.
        -------------------------------------------------------
        """

        # your code here

    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the Hash Set, allows only one copy of value.
        Calls _rehash if the Hash Set _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data element (?)
        Returns:
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """
        inserted = False
        slot = self._find_slot(value)
        if value not in slot:
            slot.insert(value)
            inserted = True
            self._count += 1
        if inserted and self._count > Hash_Set._LOAD_FACTOR * self._slots:
            self._rehash()
        return inserted

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """

        # your code here

    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the Hash Set, if it exists.
        Use: value = hs.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """

        slot = self._find_slot(key)
        if key in slot:
            value = slot.find(key)
            slot.remove(key)
            self._count -= 1
        else:
            value = None
        return value

    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the Hash Set and reallocates the
        existing data within the Hash Set to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        self._slots = self._slots * 2 + 1
        temp = self._table
        self._table = []
        for _ in range(self._slots):
            self._table.append(new_slot())
        for slot in temp:
            for val in slot:
                s = self._find_slot(val)
                s.insert(val)
        return

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two hash sets are identical.
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
             target - another hash set (Hash_Set)
        Returns:
            identical - True if this hash set contains the same values 
                as other in the same order, otherwise returns False.
        -------------------------------------------------------
        """

        # your code here

    def debug(self):
        """
        USE FOR TESTING ONLY
        ---------------------------------------------------------
        Prints the contents of the Hash Set starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        length = len(self._table)
        print("{} slots\n".format(self._slots))
        for i in range(length):
            print("""----------------------------------------
            slot {}\n""".format(i))
            for val in self._table[i]:
                print("{}\n".format(val))

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slots. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for item in slot:
                yield item