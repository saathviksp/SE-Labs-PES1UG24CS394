import pygame
import random

TILE = 40
COLS, ROWS = 20, 15
WALL, FLOOR, CHEST, KEY, TRAP = 0, 1, 2, 3, 4
SPEED = 3
MM = 6  # mini-map pixels per tile

def reachable(grid, start):
    """Tiles the player can walk to from `start` (row, col) without crossing walls or traps."""
    seen = {start}
    stack = [start]
    while stack:
        r, c = stack.pop()
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in seen
                    and grid[nr][nc] not in (WALL, TRAP)):
                seen.add((nr, nc))
                stack.append((nr, nc))
    return seen

def place_traps(grid, rooms, per_room=2):
    """Put up to `per_room` traps in every room except the start room.
    A trap is only kept if the key and chest stay reachable without
    stepping on any trap, so a level can never be impossible to finish."""
    if len(rooms) < 2:
        return
    start = (rooms[0].y, rooms[0].x)
    targets = [(r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] in (KEY, CHEST)]
    guard_row = rooms[-1].centery - 1  # row the guard patrols in the chest room
    for room in rooms[1:]:
        cells = [(r, c) for r in range(room.y, room.bottom)
                 for c in range(room.x, room.right)
                 if grid[r][c] == FLOOR and not (room is rooms[-1] and r == guard_row)]
        random.shuffle(cells)
        placed = 0
        for r, c in cells:
            if placed == per_room:
                break
            grid[r][c] = TRAP
            seen = reachable(grid, start)
            if all(t in seen for t in targets):
                placed += 1
            else:
                grid[r][c] = FLOOR

def generate_world():
    grid = [[WALL]*COLS for _ in range(ROWS)]
    rooms = []
    for _ in range(8):
        w = random.randint(3,6)
        h = random.randint(3,5)
        x = random.randint(1, COLS-w-1)
        y = random.randint(1, ROWS-h-1)
        room = pygame.Rect(x, y, w, h)
        overlap = any(room.inflate(2,2).colliderect(r) for r in rooms)
        if not overlap:
            rooms.append(room)
            for ry in range(y, y+h):
                for rx in range(x, x+w):
                    grid[ry][rx] = FLOOR
    for i in range(len(rooms)-1):
        ax, ay = rooms[i].centerx, rooms[i].centery
        bx, by = rooms[i+1].centerx, rooms[i+1].centery
        cx = ax
        while cx != bx:
            grid[ay][cx] = FLOOR
            cx += 1 if bx > cx else -1
        cy = ay
        while cy != by:
            grid[cy][bx] = FLOOR
            cy += 1 if by > cy else -1
    if len(rooms) >= 2:
        cr, ck = rooms[-1], rooms[-2]
        grid[cr.centery][cr.centerx] = CHEST
        grid[ck.centery][ck.centerx] = KEY
    place_traps(grid, rooms)
    start = rooms[0] if rooms else None
    return grid, start, rooms

COLORS = {
    WALL: (60,50,70),
    FLOOR: (200,190,170),
    CHEST: (200,160,30),
    KEY: (220,220,60),
    TRAP: (150,50,40),
}

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 28, 28)
        self.color = (60,120,220)
        self.has_key = False

    def move(self, keys, grid, rows, cols):
        dx=dy=0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: dx=-SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: dx=SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]: dy=-SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: dy=SPEED
        self._try_move(dx,0,grid,rows,cols)
        self._try_move(0,dy,grid,rows,cols)

    def _try_move(self, dx, dy, grid, rows, cols):
        new = self.rect.move(dx,dy)
        for px,py in [(new.left,new.top),(new.right-1,new.top),(new.left,new.bottom-1),(new.right-1,new.bottom-1)]:
            c,r=px//TILE,py//TILE
            if not(0<=r<rows and 0<=c<cols) or grid[r][c]==WALL:
                return
        self.rect=new

    def respawn(self, x, y):
        self.rect.topleft = (x, y)

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)
        if self.has_key:
            pygame.draw.circle(screen, (220,220,60), (self.rect.right-6, self.rect.top+6), 5)

class Guard:
    """Patrols back and forth along one row between two x pixel positions."""
    def __init__(self, left_col, right_col, row, speed=2):
        self.left = left_col * TILE + 6
        self.right = right_col * TILE + 6
        self.rect = pygame.Rect(self.left, row * TILE + 6, 28, 28)
        self.speed = speed
        self.direction = 1

    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.x >= self.right:
            self.rect.x = self.right
            self.direction = -1
        elif self.rect.x <= self.left:
            self.rect.x = self.left
            self.direction = 1

    def draw(self, screen):
        pygame.draw.rect(screen, (180,30,60), self.rect, border_radius=6)
        pygame.draw.circle(screen, (255,255,255), (self.rect.x+9, self.rect.y+11), 4)
        pygame.draw.circle(screen, (255,255,255), (self.rect.x+19, self.rect.y+11), 4)

def make_guard(rooms):
    if len(rooms) < 2:
        return None
    chest_room = rooms[-1]
    return Guard(chest_room.x, chest_room.right - 1, chest_room.centery - 1)

WIDTH = COLS * TILE
HEIGHT = ROWS * TILE + 50
FPS = 60

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Treasure Hunt")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", 24)
        self.big_font = pygame.font.SysFont("monospace", 40, bold=True)
        self.reset()

    def reset(self):
        self.grid, start, rooms = generate_world()
        if start:
            sx = start.x * TILE + 6
            sy = start.y * TILE + 6
        else:
            sx, sy = TILE+6, TILE+6
        self.start_pos = (sx, sy)
        self.player = Player(sx, sy)
        self.guard = make_guard(rooms)
        self.won = False
        self.status = "Find the KEY, then the CHEST!"

    def send_to_start(self, message):
        self.player.respawn(*self.start_pos)
        self.status = message

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r: self.reset()
        return True

    def update(self):
        if self.won: return
        keys = pygame.key.get_pressed()
        self.player.move(keys, self.grid, ROWS, COLS)
        if self.guard:
            self.guard.update()
            if self.player.rect.colliderect(self.guard.rect):
                self.send_to_start("Guard caught you! Back to start.")
                return
        pr = self.player.rect.centery // TILE
        pc = self.player.rect.centerx // TILE
        if 0<=pr<ROWS and 0<=pc<COLS:
            cell = self.grid[pr][pc]
            if cell == KEY:
                self.player.has_key = True
                self.grid[pr][pc] = FLOOR
                self.status = "Got the key! Find the CHEST!"
            elif cell == CHEST and self.player.has_key:
                self.won = True
                self.status = "Treasure found!"
            elif cell == TRAP:
                self.send_to_start("TRAP! Sent back to start.")

    def draw_minimap(self):
        ox, oy = WIDTH - COLS*MM - 8, 8
        pygame.draw.rect(self.screen, (255,255,255), (ox-2, oy-2, COLS*MM+4, ROWS*MM+4))
        for r in range(ROWS):
            for c in range(COLS):
                pygame.draw.rect(self.screen, COLORS[self.grid[r][c]], (ox+c*MM, oy+r*MM, MM, MM))
        if self.guard:
            gx = ox + self.guard.rect.centerx * MM // TILE
            gy = oy + self.guard.rect.centery * MM // TILE
            pygame.draw.circle(self.screen, (255,60,90), (gx, gy), 2)
        px = ox + self.player.rect.centerx * MM // TILE
        py = oy + self.player.rect.centery * MM // TILE
        pygame.draw.circle(self.screen, (60,170,255), (px, py), 3)

    def draw_inventory(self):
        slot = pygame.Rect(WIDTH-50, ROWS*TILE+7, 36, 36)
        pygame.draw.rect(self.screen, (40,40,60), slot, border_radius=4)
        pygame.draw.rect(self.screen, (150,150,170), slot, 2, border_radius=4)
        if self.player.has_key:
            cx, cy = slot.center
            gold = (220,220,60)
            pygame.draw.circle(self.screen, gold, (cx-8, cy), 7, 3)
            pygame.draw.line(self.screen, gold, (cx-1, cy), (cx+11, cy), 3)
            pygame.draw.line(self.screen, gold, (cx+7, cy), (cx+7, cy+6), 3)
            pygame.draw.line(self.screen, gold, (cx+11, cy), (cx+11, cy+5), 3)

    def draw(self):
        self.screen.fill((30,25,40))
        for r in range(ROWS):
            for c in range(COLS):
                cell = self.grid[r][c]
                rect = pygame.Rect(c*TILE, r*TILE, TILE, TILE)
                pygame.draw.rect(self.screen, COLORS[cell], rect)
                if cell == KEY:
                    pygame.draw.circle(self.screen, (255,240,60),(c*TILE+TILE//2, r*TILE+TILE//2),10)
                elif cell == CHEST:
                    pygame.draw.rect(self.screen,(180,120,20),rect.inflate(-12,-12),border_radius=4)
                elif cell == TRAP:
                    for i in range(3):
                        bx = rect.x + 6 + i*10
                        pygame.draw.polygon(self.screen, (230,230,230),
                            [(bx, rect.bottom-8), (bx+5, rect.y+10), (bx+10, rect.bottom-8)])
        if self.guard:
            self.guard.draw(self.screen)
        self.player.draw(self.screen)
        self.draw_minimap()
        hud = pygame.Rect(0,ROWS*TILE,WIDTH,50)
        pygame.draw.rect(self.screen,(20,20,35),hud)
        st = self.font.render(self.status+" | R=Restart", True, (200,200,200))
        self.screen.blit(st,(8,ROWS*TILE+13))
        self.draw_inventory()
        if self.won:
            ov=pygame.Surface((WIDTH,ROWS*TILE),pygame.SRCALPHA)
            ov.fill((0,0,0,140))
            self.screen.blit(ov,(0,0))
            msg=self.big_font.render("TREASURE FOUND!", True,(220,180,30))
            sub=self.font.render("Press R to Play Again",True,(180,180,180))
            self.screen.blit(msg,(WIDTH//2-msg.get_width()//2,ROWS*TILE//2-30))
            self.screen.blit(sub,(WIDTH//2-sub.get_width()//2,ROWS*TILE//2+20))
        pygame.display.flip()

    def run(self):
        running=True
        while running:
            running=self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

if __name__ == "__main__":
    engine = GameEngine()
    engine.run()