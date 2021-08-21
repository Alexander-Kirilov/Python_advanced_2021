def fill_the_box(hi, le, wi, *args):
    h = int(hi)
    l = int(le)
    w = int(wi)

    total_cubes = h * l * w

    for num in args:
        if num == "Finish":
            break
        total_cubes -= int(num)

    if total_cubes >= 0:
        return f"There is free space in the box. You could put {total_cubes} more cubes"
    else:
        return f"No more free space! You have {abs(total_cubes)} more cubes."


print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
