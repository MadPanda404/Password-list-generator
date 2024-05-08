import os
import threading

words = ["apple", "banana","strawberry"]

filename = "password_list.txt"
numbers = 1000
length_of_numbers = len(str(numbers))

def generate_passwords(word):
    with open(filename, "a") as f:
        for i in range(0, numbers + 1):
            prefix_padded = str(i).rjust(length_of_numbers, '0')
            f.write(f"{word + prefix_padded}\n")
        for i in range(0, numbers + 1):
            prefix_padded = str(i).rjust(length_of_numbers, '0')
            f.write(f"{prefix_padded + word}\n")

if os.path.exists(filename):
    if input("Remove old password list? (y/n): ").upper() == "Y":
        os.remove(filename)
        print("Removed old password list.")
else:
    print("The existing password list does not exist.")

threads = []
for index, word in enumerate(words):
    thread = threading.Thread(target=generate_passwords, args=(word,))
    threads.append(thread)
    thread.start()

for index, thread in enumerate(threads):
    thread.join()
    print(f"{round((index + 1) / len(threads) * 100)}%...")

print("100%")
print("Done")
