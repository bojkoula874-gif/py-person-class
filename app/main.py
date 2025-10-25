from __future__ import annotations
from typing import Dict, List, Optional


class Person:

    def __init__(
            self,
            name: str,
            age: int,
            spouse_name: Optional[str] = None,
            spouse_type: Optional[str] = None
    ) -> None:
        self.name = name
        self.age = age
        if spouse_name and spouse_type:
            setattr(self, spouse_type, None)
        Person.people[f"{self.name}"] = self

    people: Dict[str, Person] = {}


def create_person_list(people_data: List[dict]) -> List[Person]:
    for human in people_data:
        if "wife" in human:
            Person(
                human["name"],
                human["age"],
                spouse_name=human["wife"],
                spouse_type="wife"
            )
        elif "husband" in human:
            Person(
                human["name"],
                human["age"],
                spouse_name=human["husband"],
                spouse_type="husband"
            )

    for human in people_data:
        person = Person.people[human["name"]]
        if "wife" in human and human["wife"]:
            person.wife = Person.people[human["wife"]]
        if "husband" in human and human["husband"]:
            person.husband = Person.people[human["husband"]]

    return list(Person.people.values())


