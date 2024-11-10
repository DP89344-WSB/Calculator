class SimpleListOperations:
    def __init__(self):
        self.numbers = []

    def add_number(self, number: int):
        """Dodaje liczbę do listy."""
        self.numbers.append(number)

    def remove_number(self, number: int):
        """Usuwa liczbę z listy, jeśli istnieje."""
        if number in self.numbers:
            self.numbers.remove(number)

    def is_empty(self) -> bool:
        """Sprawdza, czy lista jest pusta."""
        return len(self.numbers) == 0

    def average(self) -> float:
        """Oblicza średnią z liczb w liście."""
        if not self.numbers:
            raise ValueError("Lista jest pusta, nie można obliczyć średniej.")
        return sum(self.numbers) / len(self.numbers)

    def find_max(self) -> int:
        """Zwraca największą liczbę w liście."""
        if not self.numbers:
            raise ValueError("Lista jest pusta, nie można znaleźć maksymalnej liczby.")
        return max(self.numbers)
