class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        # Uses the Pythagorean theorem: sqrt(w^2 + h^2)
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        # Create lines of '*' and join them with newlines
        line = "*" * self.width + "\n"
        return line * self.height

    def get_amount_inside(self, shape):
        # Calculate how many times the passed shape fits horizontally and vertically
        horizontal_fit = self.width // shape.width
        vertical_fit = self.height // shape.height
        return horizontal_fit * vertical_fit

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side: int):
        # Initialize both width and height with the side length
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"

shape1 = Rectangle(20, 30)
print(shape1.get_area())
