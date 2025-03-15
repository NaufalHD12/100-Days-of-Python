# # read only
# with open("Day24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# # write (but delete the prev content, if there is no file then it automatically creating new file)
# with open("Day24/my_file.txt", mode=) as file:
#     file.write("New Text.")

# append
with open("Day24/my_file.txt", mode="a") as file:
    file.write("\nNew Text.")