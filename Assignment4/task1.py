with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("Reading file content:")
    if len(lines) >= 2:
        line1 = lines[0].strip()
        line2 = lines[1].strip()
        print(f"Line 1: {line1}")
        print(f"Line 2: {line2}")
