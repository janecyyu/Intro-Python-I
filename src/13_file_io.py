"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# fp is 'file pointer'
with open('foo.txt') as fp:
    for line in fp:
        print(line)

# f = open('foo.txt', 'r')
# print(f.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('foo.txt') as fp:
    fp.write("""Line1
                Line2
                Line3""")
# might sometimes see a close
fp.close()

file = open('bar.txt', 'w')

file.write('This is our new text file')
file.write('This is our second new text file')
file.write('This is our third new text file')

file.close()

file = open('bar.txt', 'r')
print(file.read())
