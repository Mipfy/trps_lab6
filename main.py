import os


def SLOC(path):
    total_line_number = 0
    empty_lines = 0
    comment_line_number = 0
    file_number = 0

    for root, _, files in os.walk(path):

        for file in files:

            if file.endswith(".txt"):
                file_number += 1

                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:

                    lines = f.readlines()
                    total_line_number += len(lines)

                    for line in lines:

                        if line == "\n":
                            empty_lines += 1
                            continue

                        if r"'''" in line or r'"""' in line or r'#' in line:
                            comment_line_number += 1

    if empty_lines / total_line_number * 100 > 25:
        empty_lines = total_line_number * 0.25

    comment_statistics = comment_line_number / total_line_number
    return total_line_number, empty_lines, comment_line_number, comment_statistics, file_number


sloc = SLOC("./test/")
print( f'Physical SLOC: \ntotal lines {sloc[0]}, \nempty lines {sloc[1]}, \ncomment lines {sloc[2]}, \ncommentability metric {sloc[3]}, \nfiles number {sloc[4]}')
