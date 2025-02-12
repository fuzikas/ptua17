def filtering():
    filtered_numbers = [i for i in range(1, 1000) if "9" in str(i)]
    return filtered_numbers

print(filtering())