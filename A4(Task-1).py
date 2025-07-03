try:
    file1 = open('sample.txt', 'r')
    print("Reading file content:")
    reading_file = file1.readlines()
    line_no = 1
    for line in reading_file:
        print("Line", line_no, ":", line.strip())
        line_no += 1

    file1.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")