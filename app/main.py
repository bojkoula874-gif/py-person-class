from __future__ import annotations
from typing import Dict, List


class Person:
    people: Dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: List[dict]) -> List[Person]:

    [Person(person["name"], person["age"]) for person in people]
    for pers in people:
        if "wife" in pers and pers["wife"] is not None:
            Person.people[pers["name"]].wife =\
                Person.people[pers["wife"]]
        if "husband" in pers and pers["husband"] is not None:
            Person.people[pers["name"]].husband =\
                Person.people[pers["husband"]]

    return list(Person.people.values())
