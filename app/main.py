class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    Person.people = {
        person["name"]: Person(person["name"], person["age"])
        for person in people
    }

    for person in people:
        if "wife" in person and person["wife"]:
            setattr(
                Person.people[person["name"]],
                "wife",
                Person.people[person["wife"]]
            )
        if "husband" in person and person["husband"]:
            setattr(
                Person.people[person["name"]],
                "husband",
                Person.people[person["husband"]]
            )

    return [person for person in Person.people.values()]
