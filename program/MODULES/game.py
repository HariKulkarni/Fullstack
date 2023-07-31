import random

class SnakeGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = [(width//2, height//2)]
        self.direction = (0, 0)
        self.food = self.generate_food()

    def generate_food(self):
        while True:
            x, y = random.randint(0, self.width-1), random.randint(0, self.height-1)
            if (x, y) not in self.snake:
                return x, y

    def move_snake(self):
        head_x, head_y = self.snake[-1]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        if new_head == self.food:
            self.food = self.generate_food()
        else:
            self.snake.pop(0)

        self.snake.append(new_head)

    def change_direction(self, dx, dy):
        self.direction = (dx, dy)

    def is_game_over(self):
        head_x, head_y = self.snake[-1]
        return head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height or \
               (head_x, head_y) in self.snake[:-1]

    def display(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.food:
                    print("F", end="")
                elif (x, y) in self.snake:
                    print("S", end="")
                else:
                    print(".", end="")
            print()

if __name__ == "__main__":
    game = SnakeGame(width=10, height=10)

    while not game.is_game_over():
        game.display()
        direction = input("Enter direction (w/a/s/d): ")
        if direction == "w":
            game.change_direction(0, -1)
        elif direction == "a":
            game.change_direction(-1, 0)
        elif direction == "s":
            game.change_direction(0, 1)
        elif direction == "d":
            game.change_direction(1, 0)

        game.move_snake()

    print("Game Over!")
