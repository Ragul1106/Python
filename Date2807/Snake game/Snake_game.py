import curses
import random
import time

def food_generator(height, width):
    while True:
        yield (random.randint(1, height - 2), random.randint(1, width - 2))

class Snake:
    def __init__(self, y, x):
        self.body = [(y, x), (y, x - 1), (y, x - 2)]
        self.direction = curses.KEY_RIGHT

    def move(self):
        head = self.body[0]
        if self.direction == curses.KEY_RIGHT:
            new_head = (head[0], head[1] + 1)
        elif self.direction == curses.KEY_LEFT:
            new_head = (head[0], head[1] - 1)
        elif self.direction == curses.KEY_UP:
            new_head = (head[0] - 1, head[1])
        elif self.direction == curses.KEY_DOWN:
            new_head = (head[0] + 1, head[1])
        self.body.insert(0, new_head)
        return new_head

    def change_direction(self, new_dir):

        opposite = {curses.KEY_RIGHT: curses.KEY_LEFT,
                    curses.KEY_LEFT: curses.KEY_RIGHT,
                    curses.KEY_UP: curses.KEY_DOWN,
                    curses.KEY_DOWN: curses.KEY_UP}
        if new_dir != opposite.get(self.direction, None):
            self.direction = new_dir

    def grow(self):
        pass  

    def shrink(self):
        self.body.pop()  

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(150)

    sh, sw = stdscr.getmaxyx()
    win = curses.newwin(sh, sw, 0, 0)
    win.border()

    snake = Snake(sh//2, sw//4)
    food_gen = food_generator(sh, sw)
    food = next(food_gen)

    score = 0
    while True:
        win.clear()
        win.border()
        win.addstr(0, 2, f'Score: {score} ')
        win.addch(food[0], food[1], '*')

        for y, x in snake.body:
            win.addch(y, x, '#')

        try:
            key = win.getch()
        except:
            key = -1

        if key != -1:
            snake.change_direction(key)

        new_head = snake.move()

        if (new_head[0] in [0, sh-1] or
            new_head[1] in [0, sw-1] or
            new_head in snake.body[1:]):
            msg = "Game Over! Press any key to exit..."
            win.addstr(sh//2, sw//2 - len(msg)//2, msg)
            win.nodelay(False)
            win.getch()
            break

        if new_head == food:
            snake.grow()
            food = next(food_gen)
            score += 1
        else:
            snake.shrink()

        win.refresh()
        time.sleep(0.1)

if __name__ == "__main__":
    curses.wrapper(main)
