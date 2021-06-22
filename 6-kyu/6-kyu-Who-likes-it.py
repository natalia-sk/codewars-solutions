def likes(names):
    likes_number = len(names)

    if not likes_number:
        return 'no one likes this'

    if likes_number == 1:
        result = f'{names[0]} likes this'
    else:
        if likes_number == 2:
            result = f'{names[0]} and {names[1]} like this'
        elif likes_number == 3:
            result = f'{names[0]}, {names[1]} and {names[2]} like this'
        else:
            others = likes_number - 2
            result = f'{names[0]}, {names[1]} and {others} others like this'
    return result
