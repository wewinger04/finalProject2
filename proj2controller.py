from PyQt5.QtWidgets import *
from guiDungeonWindow import Ui_mainwindow_project2

class Controller(QMainWindow, Ui_mainwindow_project2):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton_entrance.clicked.connect(lambda: self.entrance())

        self.pushButton_room.clicked.connect(lambda: self.room())

        self.pushButton_contents.clicked.connect(lambda: self.contents())

        self.pushButton_exits.clicked.connect(lambda: self.exits())

        self.pushButton_doors.clicked.connect(lambda: self.doors())

        self.pushButton_Passages.clicked.connect(lambda: self.passages())

        self.pushButton_traps.clicked.connect(lambda: self.traps())

        self.pushButton_hazards.clicked.connect(lambda: self.hazards())

        self.pushButton_obstacles.clicked.connect(lambda: self.obstacles())

import random
result = ""

def roll(num_dice, dice_size):
    global roll_total
    roll_total = 0
    i = 0
    while i < num_dice:
        roll_total += random.randint(1, dice_size)
        i += 1


def entrance(self):
    global result
    result = ""
    roll(1, 10)
    if roll_total == 1:
        result = "20 x 20 square room with passage on each wall"
    if roll_total == 2:
        result = "30 x 30 square room with 2 passages and 2 doors"
    if roll_total == 3:
        result = "40 x 40 square room with 3 doors"
    if roll_total == 4:
        result = "80 x 20 rectangular room with pillars and 2 doors and 2 passages"
    if roll_total == 5:
        result = "20 x 40 rectangular room with passage on each wall"
    if roll_total == 6:
        result = "40 diameter circle with passages at each cardinal direction"
    if roll_total == 7:
        result = "40 diameter circle with well in center and passage at each cardinal direction"
    if roll_total == 8:
        result = "20 x 20 square with 1 passage, 2 doors, and 1 secret door"
    if roll_total == 9:
        result = "10 wide passage, T intersection"
    if roll_total == 10:
        result = "10 wide passage, 4 way intersection"
    self.textBrowser_results.setText(result)

def room(self):
    global result
    result = ""
    roll(1, 20)
    if roll_total < 3:
        result = "20 x 20 square"
    elif roll_total < 5:
        result = "30 x 30 square"
    elif roll_total < 7:
        result = "40 x 40 square"
    elif roll_total < 10:
        result = "20 x 30 rectangle"
    elif roll_total < 13:
        result = "30 x 40 rectangle"
    elif roll_total < 15:
        result = "40 x 50 rectangle"
    elif roll_total == 15:
        result = "50 x 80 rectangle"
    elif roll_total == 16:
        result = "30 diameter circle"
    elif roll_total == 17:
        result = "50 diameter circle"
    elif roll_total == 18:
        result = "40 x 40 octagon"
    elif roll_total == 19:
        result = "60 x 60 octagon"
    else:
        result = "40 x 60 trapezoid"
    self.textBrowser_results.setText(result)

def contents(self):
    global result
    result = ""
    roll(1, 100)
    if roll_total < 9:
        result = "Dominant monster"
    elif roll_total < 16:
        result = "Dominant monster with treasure"
    elif roll_total < 28:
        result = "Monster (pet or ally)"
    elif roll_total < 34:
        result = "Monster (pet or ally) guarding treasure"
    elif roll_total < 43:
        result = "Monster (random creature)"
    elif roll_total < 51:
        result = "Monster (random creature) with treasure"
    elif roll_total < 59:
        result = "Hazard with incidental treasure"
    elif roll_total < 64:
        result = "Obstacle"
    elif roll_total < 74:
        result = "Trap"
    elif roll_total < 77:
        result = "Trap protecting treasure"
    elif roll_total < 81:
        result = "Strangeness"
    elif roll_total < 89:
        result = "Empty"
    elif roll_total < 95:
        result = "Empty with a hazard"
    else:
        result = "Empty with treasure"
    self.textBrowser_results.setText(result)

def exits(self):
    global result
    result = ""
    roll(1, 20)
    if roll_total < 4:
        total_exits = 0
    elif roll_total < 9:
        total_exits = 1
    elif roll_total < 12:
        total_exits = 2
    elif roll_total < 14:
        total_exits = 2
    elif roll_total < 16:
        total_exits = 3
    elif roll_total <= 18:
        total_exits = 4
    elif roll_total == 19:
        total_exits = 5
    else:
        total_exits = 6
    result = "Total Exits: {}".format(total_exits)
    n = 1
    while n <= total_exits:
        roll(1, 20)
        if roll_total < 8:
            roll(1, 20)
            if roll_total < 11:
                result = result + "\nDoor on wall opposite entrance"
            else:
                result = result + "\nCorridor on wall opposite entrance"
        elif roll_total < 13:
            roll(1, 20)
            if roll_total < 11:
                result = result + "\nDoor on wall left of entrance"
            else:
                result = result + "\nCorridor on wall left of entrance"
        elif roll_total < 18:
            roll(1, 20)
            if roll_total < 11:
                result = result + "\nDoor on wall right of entrance"
            else:
                result = result + "\nCorridor on wall right of entrance"
        else:
            roll(1, 20)
            if roll_total < 11:
                result = result + "\nDoor on same wall as entrance"
            else:
                result = result + "\nCorridor on same wall as entrance"
        n += 1
    self.textBrowser_results.setText(result)

def doors(self):
    global result
    result = ""
    roll(1, 20)
    if roll_total < 11:
        result = "Wooden door"
    elif roll_total < 13:
        result = "Barred or locked wooden door"
    elif roll_total == 13:
        result = "Stone door"
    elif roll_total == 14:
        result = "Barred or locked stone door"
    elif roll_total == 15:
        result = "Iron door"
    elif roll_total == 16:
        result = "Barred or locked iron door"
    elif roll_total == 17:
        result = "Portcullis"
    elif roll_total == 18:
        result = "Barred or locked portcullis"
    elif roll_total == 19:
        result = "Secret door"
    elif roll_total == 20:
        result = "Barred or locked secret door"
    result = result + "\nThat opens to\n"
    roll(1, 20)
    if roll_total < 3:
        result = result + "T - intersection with 10 foot long passages"
    elif roll_total < 9:
        result = result + "20 foot long straight passage"
    elif roll_total < 19:
        result = result + "A room"
    elif roll_total == 19:
        stairs(self)
    else:
        result = result + "False door with a trap"
    self.textBrowser_results.setText(result)

def stairs(self):
    global result
    roll(1, 20)
    if roll_total < 5:
        result = result + "Stairs down 1 level to a room"
    elif roll_total < 9:
        result = result + "Stairs down 1 level to 20 foot passage"
    elif roll_total == 9:
        result = result + "Stairs down 2 levels to a room"
    elif roll_total == 10:
        result = result + "Stairs down 2 levels to 20 foot passage"
    elif roll_total == 11:
        result = result + "Stairs down 3 levels to a room"
    elif roll_total == 12:
        result = result + "Stairs down 3 levels to 20 foot passage"
    elif roll_total == 13:
        result = result + "Stairs up 1 level to a room"
    elif roll_total == 14:
        result = result + "Stairs up 1 level to 20 foot passage"
    elif roll_total == 15:
        result = result + "Stairs up to a dead end"
    elif roll_total == 16:
        result = result + "Stairs down to a dead end"
    elif roll_total == 17:
        result = result + "Chimney up 1 level to 20 foot passage"
    elif roll_total == 18:
        result = result + "Chimney up 2 levels to 20 foot passage"
    elif roll_total == 19:
        result = result + "Shaft down 1 level to a room"
    else:
        result = result + "Shaft up 1 level and down 1 level to rooms"

def passages(self):
    global result
    result = ""
    roll(1, 20)
    if roll_total < 3:
        pass_width = 5
    elif roll_total < 13:
        pass_width = 10
    elif roll_total < 15:
        pass_width = 20
    elif roll_total < 17:
        pass_width = 30
    else:
        pass_width = 40
    result = "The passage is {} feet wide,\n".format(pass_width)
    if roll_total == 17:
        result = result + "and There is a row of pillars down the middle. The passage goes\n"
    if roll_total == 18:
        result = result + "and There is a double row of pillars. The passage goes\n"
    if roll_total == 19:
        result = result + "and The ceiling is twice the normal height. The passage goes\n"
    if roll_total == 20:
        result = result + "and The ceiling is twice the normal height, with a gallery halfway up that gives access to 1 level above. The passage goes\n"
    roll(1, 20)
    if roll_total < 3:
        result = result + "30 feet straight, no doors or side passages\n"
    elif roll_total == 3:
        result = result + "Straight 20 feet, door to the right, then straight 10 more feet\n"
    elif roll_total == 4:
        result = result + "Straight 20 feef, door to the left, then straight 10 more feet\n"
    elif roll_total == 5:
        result = result + "Straight 20 feet, ends in a door\n"
    elif roll_total < 8:
        result = result + "Straight 20 feet, branch passage to the right, then straight 10 more feet\n"
    elif roll_total < 10:
        result = result + "Straight 20 feet, branch passage to the left, the. straight 10 more feet\n"
    elif roll_total == 10:
        result = result + "Straight 20 feet to\n"
        roll(1, 10)
        if roll_total == 1:
            result = result + "a secret door\n"
        else:
            result = result + "a dead end\n"
    elif roll_total < 13:
        result = result + "Straight 20 feet, then left turn, then straight 10 more feet\n"
    elif roll_total < 15:
        result = result + "Straight 20 feet, then right turn, then straight 10 more feet\n"
    elif roll_total < 20:
        result = result + "To a room\n"
    else:
        result = result + "To\n"
        stairs(self)
    self.textBrowser_results.setText(result)

def traps(self):
    global result
    result = ""
    roll(1, 6)
    result = "The trap is triggered when\n"
    if roll_total == 1:
        result = result + "stepped on (floor or stairs)\n"
    if roll_total == 2:
        result = result + "moved through (door or hallway)\n"
    if roll_total == 3:
        result = result + "touched (door handle or statue)\n"
    if roll_total == 4:
        result = result + "opened (door or chest)\n"
    if roll_total == 5:
        result = result + "looked at (painting or symbol)\n"
    if roll_total == 6:
        result = result + "moved (statue or stone block)\n"
    roll(1, 100)
    if roll_total < 5:
        result = result + "Magic missile shoots from an object"
    elif roll_total < 8:
        result = result + "Collapsing staircase makes a ramp that deposits characters into a pit"
    elif roll_total < 11:
        result = result + "Ceiling block falls or ceiling collapses"
    elif roll_total < 13:
        result = result + "Ceiling lowers and room locks"
    elif roll_total < 15:
        result = result + "Chute opens in the floor"
    elif roll_total < 17:
        result = result + "Alarm signals nearby monsters"
    elif roll_total < 20:
        result = result + "Touching an object triggers disintegrate spell"
    elif roll_total < 24:
        result = result + "Door or other object is coated in contact poison"
    elif roll_total < 28:
        result = result + "Fire shoots from wall, floor, or object"
    elif roll_total < 31:
        result = result + "Touching an object triggers a flesh to stone spell"
    elif roll_total < 34:
        result = result + "Floor collapses or is an illusion"
    elif roll_total < 37:
        result = result + "Vent releases\n"
        roll(1, 6)
        if roll_total == 1:
            result = result + "blinding gas"
        if roll_total == 2:
            result = result + "acidic gas"
        if roll_total == 3:
            result = result + "obscuring gas"
        if roll_total == 4:
            result = result + "paralyzing gas"
        if roll_total == 5:
            result = result + "poison gas"
        if roll_total == 6:
            result = result + "knockout gas"
    elif roll_total < 40:
        result = result + "Electric floor tiles"
    elif roll_total < 44:
        result = result + "Glyph of warding"
    elif roll_total < 47:
        result = result + "Huge, wheeled statue rolls down corridor"
    elif roll_total < 50:
        result = result + "Lightning bolt from wall or object"
    elif roll_total < 53:
        result = result + "Room locks and fills with\n"
        roll(1, 6)
        if roll_total == 6:
            result = result + "acid"
        else:
            result = result + "water"
    elif roll_total < 57:
        result = result + "Darts fire from opened chest"
    elif roll_total < 60:
        result = result + "Weapon, armor, or rug animates and attacks when touched"
    elif roll_total < 63:
        result = result + "Bladed pendulum swings across room or hall"
    elif roll_total < 68:
        roll(1, 8)
        if roll_total < 2:
            result = result + "Hidden pit opens beneath the characters with gelatinous cube at the bottom"
        elif roll_total < 3:
            result = result + "Hidden pit opens beneath the characters with black pudding at the bottom"
        else:
            result = result + "Hidden pit opens beneath the characters"
    elif roll_total < 74:
        result = result + "Locking pit fills with water"
    elif roll_total < 78:
        result = result + "Scything blade emerges from wall or object"
    elif roll_total < 82:
        result = result + "Spears, possibly poisoned, spring out"
    elif roll_total < 85:
        result = result + "Brittle stairs collapse over spikes"
    elif roll_total < 89:
        result = result + "Thunderwave knocks characters into a pit or spikes"
    elif roll_total < 92:
        result = result + "Steel or stone jaws restrain a character"
    elif roll_total < 95:
        result = result + "Stone block smashes across hallway"
    elif roll_total < 98:
        result = result + "Symbol spell"
    else:
        result = result + "Walls slide together"
    roll(1, 6)
    if roll_total < 3:
        severity = "a setback'"
    elif roll_total < 6:
        severity = "dangerous"
    else:
        severity = "deadly"
    result = result + "\nIt is {}.".format(severity)
    self.textBrowser_results.setText(result)

def obstacles(self):
    global result
    result = ""
    roll(1, 20)
    if roll_total < 2:
        roll(1, 10)
        anti_life = roll_total * 10
        result = "Anti-life aura with {} foot radius prevents living creatures from healing within the aura".format(anti_life)
    elif roll_total < 3:
        result = "Battering winds cause half movement speed and ranged disadvantage"
    elif roll_total < 4:
        result = "Blade barrier blocks passage"
    elif roll_total < 9:
        result = "Cave-in"
    elif roll_total < 13:
        roll(1, 4)
        chasm_wide = roll_total * 10
        roll(2, 6)
        chasm_deep = roll_total * 10
        result = "Chasm {} feet wide and {} feet deep, possibly connected to other dungeon levels".format(chasm_wide, chasm_deep)
    elif roll_total < 15:
        roll(2, 10)
        water_deep = roll_total
        result = "Water fills {} feet of the area; create sloped passages, raised floors, or stairs to contain".format(water_deep)
    elif roll_total < 16:
        roll(1, 100)
        if roll_total < 51:
            result = "A stone bridge with lava flowing beneath"
        else:
            result = "Lava flows through the area"
    elif roll_total < 17:
        roll(1, 4)
        if roll_total < 4:
            result = "Overgrown mushrooms block progress, must be hacked down"
        else:
            roll(1, 10)
            if roll_total < 4:
                fungi = "Brown mold"
            elif roll_total < 6:
                fungi = "Shriekers"
            elif roll_total < 8:
                fungi = "Violet fungus"
            else:
                fungi = "Yellow mold"
            result = "Overgrown mushrooms block path and must be hacked through. {} is hidden in the area".format(fungi)
    elif roll_total < 18:
        result = "Poisonous gas doing 1d6 per minute of exposure"
    elif roll_total < 19:
        result = "Reverse gravity effect"
    elif roll_total < 20:
        result = "Wall of fire blocks passage"
    else:
        result = "Wall of force blocks passage"
    self.textBrowser_results.setText(result)

def hazards(self):
    global result
    result = ""
    roll(1, 20)
    if roll_total < 4:
        result = "Brown mold"
    elif roll_total < 9:
        result = "Green slime"
    elif roll_total < 11:
        result = "Shrieker"
    elif roll_total < 16:
        result = "Spider webs"
    elif roll_total < 18:
        result = "Violet fungus"
    else:
        result = "Yellow mold"
    self.textBrowser_results.setText(result)
