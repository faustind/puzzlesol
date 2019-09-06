# In Obedience of the Truth

from collections import deque

def create_img(w, h):
    """Create img h*w filled with 0."""
    h, w = int(h), int(w)
    # using one more row and col for easy indexing
    img = [['O'] * (w+1) for _ in range(h+1)]
    return img

def clear_img(img):
    w, h = len(img[0]), len(img)
    return [['O'] * (w) for _ in range(h)]

def color_pixel(img, col, row, c):
    col, row = int(col), int(row)
    img[row][col] = c

def vseg(img, col, y1, y2, c):
    col, y1, y2 = map(int, (col, y1, y2))
    if y2 < y1:
        y1, y2 = y2, y1 # y2 is now bigger
    for i in range(y1, y2+1):
        img[i][col] = c

def hseg(img, first_col, last_col, row, c):
    first_col, last_col, row = map(int, (first_col, last_col, row))
    if last_col < first_col:
        first_col, last_col = last_col, first_col
    for col in range(first_col, last_col+1):
        img[row][col] = c

def color_rec(img, col1, row1, col2, row2, c):
    col1, row1, col2, row2 = map(int, (col1, row1, col2, row2))
    if row2 < row1 :
        row1, row2 = row2, row1
    for row in range(row1, row2+1):
        hseg(img, col1, col2, row, c)

def fill_reg(img, col, row, c):
    col, row = int(col), int(row)
    H, W = len(img)-1, len(img[0])-1
    base_color = img[row][col]
    # q hold pixel with an adjacent side to one pixel in the region
    q = deque()
    visited = set()
    q.append((row, col))
    while q:
        ri, ci = q.popleft()
        if 1 <= ri <= H and 1 <= ci <= W and img[ri][ci] == base_color:
            if (ri, ci) not in visited:
                visited.add((ri, ci))
                # same color as x
                img[ri][ci] = c
                # append its adjacent pixel to q
                q.extend([(ri-1, ci), (ri+1, ci),
                         (ri, ci-1), (ri, ci+1)])

def print_img(img, name):
    print(name)
    for row in img[1:]:
        print(''.join(str(i) for i in row[1:]))

commands = {
    'I': create_img,
    'C': clear_img,
    'L': color_pixel,
    'V': vseg,
    'H': hseg,
    'K': color_rec,
    'F': fill_reg,
    'S': print_img,
}

while True:
    command = input().split()
    if command[0] == 'X':
        break

    if command[0] not in commands:
        continue

    if command[0] == 'I':
        img = create_img(*command[1:])
        continue
    if command[0] == 'C':
        img = clear_img(img)
        continue

    # perfom action
    commands[command[0]](img, *command[1:])
