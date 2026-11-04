from abc import ABC, abstractmethod


class Animal(ABC):
    """Common interface and shared behavior for all animals."""

    def __init__(self, name: str) -> None:
        self.name = name

    @property
    @abstractmethod
    def species(self) -> str:
        """Each animal must provide its species."""
        ...

    @abstractmethod
    def make_sound(self) -> str:
        """Each animal must provide its own sound."""
        ...

    @abstractmethod
    def move(self) -> str:
        """Each animal must describe how it moves."""
        ...

    def eat(self, food: str) -> None:
        """Shared behavior: all animals can eat."""
        print(f"{self.name} the {self.species} eats {food}.")

    def sleep(self) -> None:
        """Shared behavior: all animals can sleep."""
        print(f"{self.name} the {self.species} is sleeping.")

    def introduce(self) -> None:
        """Uses the abstract property and methods through a common interface."""
        print(f"I'm {self.name}, a {self.species}.")
        print(f"I say: {self.make_sound()}")
        print(f"I move by: {self.move()}")


class Lion(Animal):
    @property
    def species(self) -> str:
        return "lion"

    def make_sound(self) -> str:
        return "Roar!"

    def move(self) -> str:
        return "walking and running"


class Duck(Animal):
    @property
    def species(self) -> str:
        return "duck"

    def make_sound(self) -> str:
        return "Quack!"

    def move(self) -> str:
        return "walking and swimming"


def care_for_animal(animal: Animal) -> None:
    """Works with any Animal subclass without knowing its exact type."""
    animal.introduce()
    animal.eat("food")
    animal.sleep()


def main() -> None:
    animals: list[Animal] = [
        Lion("Leo"),
        Duck("Daisy"),
    ]

    for animal in animals:
        care_for_animal(animal)
        print()


if __name__ == "__main__":
    main()