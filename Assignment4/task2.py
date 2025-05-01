text_1 = input("Enter text to write to the file: ")
open('output.txt', 'w').write(text_1)
print("Data successfully written to output.txt.")

text_2 = input("\nEnter addition text to append: ")
open('output.txt', 'a').write('\n' + text_2)
print("Data successfully appended")

with open('output.txt', 'r') as file:
    content = file.read()
    print("\nFinal Content of Output.txt:")
    print(content)