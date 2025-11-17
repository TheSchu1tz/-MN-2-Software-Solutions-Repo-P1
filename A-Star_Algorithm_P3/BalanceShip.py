from collections import defaultdict

def main():
    filepath = input("Please provide the file to solve for: ")
    file = ReadFile(filepath)
    manifest = ParseFile(file)

    

# returns array of strings read from filename
def ReadFile(filename):
    file = open(filename, mode = 'r', encoding = 'utf-8-sig')
    lines = file.readlines()
    file.close()
    return lines

# creates data representation of manifest
def ParseFile(lines):
    manifest = []
    for line in lines:
        # get plain text [01, 01], {00000}, NAN
        parts = line.split(", ")
        # get int representation of the coordinate [1,1]
        x, y = parts[0].strip("[]").split(",")
        coord = [int(x), int(y)]
        # get the id "{00000}"
        id = parts[1] 
        # get the item "NAN"
        item = parts[2].strip("\n")

        entry = [coord, id, item]
        manifest.append(entry)
    return manifest

if __name__ == "__main__":
    main()