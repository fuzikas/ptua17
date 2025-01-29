
at_count = 0
email = input("Enter your email address ")
for symbol in email:
    if symbol == "@":
        at_count += 1

print(at_count)
# symbol_index = int(email.index("@"))

# for next_symbol in email[symbol_index:len(email)]:
#     if next_symbol == ".":
#         print("taskas yra")
#         break
# if next_symbol != ".":
#     print("Don't forget to use . after your domain name")