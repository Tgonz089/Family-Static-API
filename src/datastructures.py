
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22],
                "id": self._generateId()
            },
            {
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3],
                "id": self._generateId()
            },
            {
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1],
                "id": self._generateId()
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self) -> int:
        return randint(0, 99999999)

    def add_member(self, member: dict) -> None:
        self._members.append(member)

    def delete_member(self, id):
        status = False
        for i, item in enumerate(self._members, start=0):
            if item["id"] == id:
                self._members.pop(i)
                status = True

        return status
    def get_member(self, id):
        for i in self._members:
            if i["id"] == int(id):
                return i

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
