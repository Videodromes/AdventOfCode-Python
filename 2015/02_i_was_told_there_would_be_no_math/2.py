with open(
    "2015/02_i_was_told_there_would_be_no_math/input.txt", "r", encoding="utf-8"
) as input:
    data = input.read().splitlines()


# Part 1
def solution():
    total_paper = 0
    total_ribbon = 0

    for i in data:
        parts = i.split("x")
        l, w, h = int(parts[0]), int(parts[1]), int(parts[2])
        area1, area2, area3 = l * w, w * h, h * l
        slack = min(area1, area2, area3)

        total_paper += 2 * (area1 + area2 + area3) + slack
        total_ribbon += ribbon(l, w, h)

    print(f"Part 1: {total_paper}\nPart 2: {total_ribbon}")


# Part 2
def ribbon(length, width, height):
    p1 = 2 * (length + width)
    p2 = 2 * (length + height)
    p3 = 2 * (width + height)

    ribbon = min(p1, p2, p3)
    bow = length * width * height

    return ribbon + bow


solution()
