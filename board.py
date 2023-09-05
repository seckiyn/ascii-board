from dataclasses import dataclass
import readline

@dataclass
class Character:
    name: str
    char: str
    x: int
    y: int
    @property
    def pos(self):
        return self.x, self.y


class Board:
    def __init__(self, character: Character, width=20, height=20):
        self.width = width
        self.height = height
        self.character = character
        self.char = "*"
        self.block = "#"
        self.board = Board.create_board(width, height, self.char)
    def update_character_position(self):
        x = self.character.x
        y = self.character.y
        char = self.character.char
        self.set_position_with_char(x, y, char)

    def set_position_with_char(self, x, y, char):
        self.board[y][x] = char

    def print_board(self):
        Board.print_board_static(self.board)

    def check_border(self, x, y):
        border = not (0 <= x < self.width and 0 <= y < self.height)
        """
            Is it inside border and next square is a block
        """
        block = not border and self.board[y][x] == self.block
        return border or block

    def move_right(self):
        new_x = self.character.x + 1
        new_y = self.character.y + 0
        if self.check_border(new_x, new_y): return

        old_x, old_y = self.character.pos
        self.set_position_with_char(old_x, old_y, self.char)

        self.character.x = new_x
        self.character.y = new_y
    def move_left(self):
        new_x = self.character.x + -1
        new_y = self.character.y + 0
        if self.check_border(new_x, new_y): return

        old_x, old_y = self.character.pos
        self.set_position_with_char(old_x, old_y, self.char)

        self.character.x = new_x
        self.character.y = new_y
    def move_up(self):
        new_x = self.character.x + 0
        new_y = self.character.y + -1
        if self.check_border(new_x, new_y): return

        old_x, old_y = self.character.pos
        self.set_position_with_char(old_x, old_y, self.char)

        self.character.x = new_x
        self.character.y = new_y
    def move_down(self):
        new_x = self.character.x + 0
        new_y = self.character.y + 1
        if self.check_border(new_x, new_y): return

        old_x, old_y = self.character.pos
        self.set_position_with_char(old_x, old_y, self.char)

        self.character.x = new_x
        self.character.y = new_y
    def draw_line(self, x1, y1, x2, y2):
        dx = abs(x2 - x1)
        sx = 1 if x1 < x2 else -1
        dy = -abs(y2 - y1)
        sy = 1 if y1 < y2 else -1
        error = dx + dy

        while True:
            self.set_position_with_char(x1, y1, self.block)
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * error
            if e2 >= dy:
                if x1 == x2:
                    break
                error = error + dy
                x1 = x1 + sx
            if e2 <= dx:
                if y1 == y2:
                    break
                error = error + dx
                y1 = y1 + sy




    @staticmethod
    def create_board(width, height, char="*"):
        board = list()
        for i in range(width):
            board.append(list([char]*width))
        return board
    @staticmethod
    def print_board_static(board):
        for line in board:
            print("".join(line))



if __name__ == "__main__":
    # board = Board.create_board(10, 10)
    # Board.print_board_static(board)

    character = Character("mustafa", "@", 0, 0)
    b = Board(character, 20, 20)
    b.update_character_position()
    b.set_position_with_char(4, 5, b.block)
    b.draw_line(0, 0, 11, 15)
    b.print_board()
    while True:
        func = input("Func: ")
        getattr(b, func)()
        b.update_character_position()
        b.print_board()
