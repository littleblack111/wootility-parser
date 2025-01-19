keys: dict[str, str] = {
    "Esc": "",
    "F1": "",
    "F2": "",
    "F3": "",
    "F4": "",
    "F5": "",
    "F6": "",
    "F7": "",
    "F8": "",
    "F9": "",
    "F10": "",
    "F11": "",
    "F12": "",
    "ScrLk": "",
    "Pause": "",
    "PrtSc": "",
    "A1": "",
    "A2": "",
    "A3": "",
    "Mode": "",
    "Tilde": "",
    "1": "",
    "2": "",
    "3": "",
    "4": "",
    "5": "",
    "6": "",
    "7": "",
    "8": "",
    "9": "",
    "0": "",
    "Minus": "",
    "Equal": "",
    "Backspace": "",
    "Ins": "",
    "Home": "",
    "PgUp": "",
    "Num": "",
    "NumSlash": "",
    "NumAsterisk": "",
    "NumMinus": "",
    "Tab": "",
    "Q": "",
    "W": "",
    "E": "",
    "R": "",
    "T": "",
    "Y": "",
    "U": "",
    "I": "",
    "O": "",
    "P": "",
    "LeftBracket": "",
    "RightBracket": "",
    "Backslash": "",
    "Del": "",
    "End": "",
    "PgDn": "",
    "Num7": "",
    "Num8": "",
    "Num9": "",
    "NumPlus": "",
    "Caps": "",
    "A": "",
    "S": "",
    "D": "",
    "F": "",
    "G": "",
    "H": "",
    "J": "",
    "K": "",
    "L": "",
    "Semicolon": "",
    "Quote": "",
    "Enter": "",
    "Num4": "",
    "Num5": "",
    "Num6": "",
    "LShift": "",
    "Z": "",
    "X": "",
    "C": "",
    "V": "",
    "B": "",
    "N": "",
    "M": "",
    "Comma": "",
    "Period": "",
    "Slash": "",
    "RShift": "",
    "Up": "",
    "Num1": "",
    "Num2": "",
    "Num3": "",
    "NumEnter": "",
    "LCtrl": "",
    "LSuper": "",
    "LAlt": "",
    "Space": "",
    "RAlt": "",
    "RSuper": "",
    "Menu": "",
    "RCtrl": "",
    "Left": "",
    "Down": "",
    "Right": "",
    "Num0": "",
    "NumPeriod": "",
}

keysInternal: dict[str, dict[int, int]] = {
    "Esc": {0: 0},
    "F1": {0: 2},
    "F2": {0: 3},
    "F3": {0: 4},
    "F4": {0: 5},
    "F5": {0: 6},
    "F6": {0: 7},
    "F7": {0: 8},
    "F8": {0: 9},
    "F9": {0: 10},
    "F10": {0: 11},
    "F11": {0: 12},
    "F12": {0: 13},
    "PrtSc": {0: 14},
    "Pause": {0: 15},
    "ScrLk": {0: 16},
    "A1": {0: 17},
    "A2": {0: 18},
    "A3": {0: 19},
    "Mode": {0: 20},
    "Tilde": {1: 0},
    "1": {1: 1},
    "2": {1: 2},
    "3": {1: 3},
    "4": {1: 4},
    "5": {1: 5},
    "6": {1: 6},
    "7": {1: 7},
    "8": {1: 8},
    "9": {1: 9},
    "0": {1: 10},
    "Minus": {1: 11},
    "Equal": {1: 12},
    "Backspace": {1: 13},
    "Ins": {1: 14},
    "Home": {1: 15},
    "PgUp": {1: 16},
    "Num": {1: 17},
    "NumSlash": {1: 18},
    "NumAsterisk": {1: 19},
    "NumMinus": {1: 20},
    "Tab": {2: 0},
    "Q": {2: 1},
    "W": {2: 2},
    "E": {2: 3},
    "R": {2: 4},
    "T": {2: 5},
    "Y": {2: 6},
    "U": {2: 7},
    "I": {2: 8},
    "O": {2: 9},
    "P": {2: 10},
    "LeftBracket": {2: 11},
    "RightBracket": {2: 12},
    "Backslash": {2: 13},
    "Del": {2: 14},
    "End": {2: 15},
    "PgDn": {2: 16},
    "Num7": {2: 17},
    "Num8": {2: 18},
    "Num9": {2: 19},
    "NumPlus": {2: 20},
    "Caps": {3: 0},
    "A": {3: 1},
    "S": {3: 2},
    "D": {3: 3},
    "F": {3: 4},
    "G": {3: 5},
    "H": {3: 6},
    "J": {3: 7},
    "K": {3: 8},
    "L": {3: 9},
    "Semicolon": {3: 10},
    "Quote": {3: 11},
    "Enter": {3: 13},
    "Num4": {3: 17},
    "Num5": {3: 18},
    "Num6": {4: 19},
    "LShift": {4: 0},
    "Z": {4: 2},
    "X": {4: 3},
    "C": {4: 4},
    "V": {4: 5},
    "B": {4: 6},
    "N": {4: 7},
    "M": {4: 8},
    "Comma": {4: 9},
    "Period": {4: 10},
    "Slash": {4: 11},
    "RShift": {4: 13},
    "Up": {4: 15},
    "Num1": {4: 17},
    "Num2": {4: 18},
    "Num3": {4: 19},
    "NumEnter": {4: 20},
    "LCtrl": {5: 0},
    "LSuper": {5: 1},
    "LAlt": {5: 2},
    "Space": {5: 6},
    "RCtrl": {5: 13},
    "RAlt": {5: 10},
    "RSuper": {5: 11},
    "Fn": {5: 12},
    "Left": {5: 14},
    "Down": {5: 15},
    "Right": {5: 16},
    "Num0": {5: 18},
    "NumPeriod": {5: 19},
}
