from __future__ import annotations
from typing import Dict, List


class Person:

    def __init__(
            self,
            name: str,
            age: int,
    ) -> None:
        self.name = name
        self.age = age
        Person.people[f"{self.name}"] = self

    people: Dict[str, Person] = {}


def create_person_list(people_data: List[dict]) -> List[Person]:

    [Person(person["name"], person["age"]) for person in people_data]

    for human in people_data:
        person = Person.people[human["name"]]
        spouse_name = human.get("wife") or human.get("husband")
        if spouse_name:
            setattr(person,
                    "wife" if "wife" in human else "husband",
                    Person.people.get(spouse_name))

    return list(Person.people.values())
