import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

# Initialize curses
curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

key = KEY_RIGHT  # initial direction
score = 0

snake = [[4,10], [4,9], [4,8]]
food = [10,20]
win.addch(food[0], food[1], '*')

while key != 27:  # 27 = ESC
    win.border(0)
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')
    win.addstr(0, 27, ' SNAKE ')
    win.timeout(150 - (len(snake)//5 + len(snake)//10)%120)

    prev_key = key
    event = win.getch()
    key = key if event == -1 else event

    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:
        key = prev_key

    # Calculate next head position
    y = snake[0][0]
    x = snake[0][1]
    if key == KEY_RIGHT:
        x += 1
    if key == KEY_LEFT:
        x -= 1
    if key == KEY_UP:
        y -= 1
    if key == KEY_DOWN:
        y += 1
    snake.insert(0, [y, x])

    # Check for collision with border or self
    if y == 0 or y == 19 or x == 0 or x == 59 or snake[0] in snake[1:]:
        break

    # If snake eats food
    if snake[0] == food:
        score += 1
        food = []
        while food == []:
            food = [randint(1,18), randint(1,58)]
            if food in snake:
                food = []
        win.addch(food[0], food[1], '*')
    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(snake[0][0], snake[0][1], '#')

curses.endwin()
print(f"Final score = {score}")
