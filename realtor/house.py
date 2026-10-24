from math import isfinite


class House:
    def __init__(self, area, price, bedrooms=1, floors=1):
        if not isfinite(area) or area <= 0:
            raise ValueError("Area must be a finite positive number")
        if not isfinite(price) or price < 0:
            raise ValueError("Price must be a finite non-negative number")
        if not isinstance(bedrooms, int) or bedrooms < 0:
            raise ValueError("Number of bedrooms must be a non-negative integer")
        if not isinstance(floors, int) or floors <= 0:
            raise ValueError("Number of floors must be a positive integer")
        self._area = area
        self._price = price
        self._bedrooms = bedrooms
        self._floors = floors

    def final_price(self, discount):
        if not isfinite(discount) or not 0 <= discount <= 100:
            raise ValueError("Discount must be between 0 and 100 percent")
        return self._price * (1 - discount / 100)

    def __str__(self):
        return (
            f"House area: {self._area}, bedrooms: {self._bedrooms}, "
            f"floors: {self._floors}, price: {self._price}"
        )


class SmallHouse(House):
    def __init__(self, price, bedrooms=1, floors=1):
        super().__init__(42, price, bedrooms, floors)
