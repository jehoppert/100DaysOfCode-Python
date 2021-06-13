age: int
name: str
height: float
is_human: bool

# type hints params and output


def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


print(police_check("tell"))
