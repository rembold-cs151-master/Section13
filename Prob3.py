from pgl import GWindow, GRect, GLabel, GCompound

SQUARE_SIZE = 60
GWINDOW_WIDTH = 4 * SQUARE_SIZE
GWINDOW_HEIGHT = 4 * SQUARE_SIZE
SQUARE_FILL_COLOR = "LightGray"
PUZZLE_FONT = "18px 'Sans-Serif'"

def create_piece(num):
    compound = GCompound()
    square = GRect(SQUARE_SIZE, SQUARE_SIZE)
    square.set_filled(True)
    square.set_fill_color(SQUARE_FILL_COLOR)
    value = GLabel(str(num))
    value.set_font(PUZZLE_FONT)
    value.move(
        SQUARE_SIZE / 2 - value.get_width() / 2,
        SQUARE_SIZE / 2 + value.get_ascent() / 2,
    )
    compound.add(square)
    compound.add(value)
    return compound

def click_action(e):
    mx, my = e.get_x(), e.get_y()
    current = gw.get_element_at(mx, my)
    if current is not None: #we clicked on a piece
        # Search all 4 directions
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            cx = mx + x * SQUARE_SIZE
            cy = my + y * SQUARE_SIZE
            if ((0 < cx < GWINDOW_WIDTH) and 
                (0 < cy < GWINDOW_HEIGHT)):
                elem = gw.get_element_at(cx, cy)
                if elem is None: # the empty space!
                    current.move(x * SQUARE_SIZE, 
                                 y * SQUARE_SIZE)
                    return #stops the search early if we found it

gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
for i in range(15):
    p = create_piece(i + 1)
    p.move(SQUARE_SIZE * (i % 4), 
           SQUARE_SIZE * (i // 4))
    gw.add(p)
gw.add_event_listener("mousedown", click_action)
