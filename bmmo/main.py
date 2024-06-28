import sys
from bmmo.misc import optimize
from bmmo.file import get_lines


def main(path: str):
    og_lines = get_lines(path)
    optimized_lines = optimize(og_lines)
    optimized_bmap_file = open('optimized_bmap.txt', 'w+')
    for line in optimized_lines:
        optimized_bmap_file.write(line + '\n')
    optimized_bmap_file.close()


if __name__ == '__main__':
    path = sys.argv[1]
    main(path)
