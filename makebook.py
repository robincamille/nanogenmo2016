#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script outputs an .md file of the generated novel.
# Each novel is saved in drafts/.
# To keep track of yourself, the script prints to screen the
# name of the library you're "visiting." 

# Required docs:
# - List of NYC public libraries, nyc_public_libraries.tsv
# - List of Project GITenberg texts, GITenberg_repos_list_2.tsv

from random import randint
from random import shuffle
import excerpt, time

outfile = open('drafts/' + str(time.time()) + '.md','w')

outfile.write("# If on a winter's night a library cardholder\n\n")
outfile.write("## Robin Camille Davis\n\n")
outfile.write("*Generated for NaNoGenMo 2016*\n\n\n\n\n")

outfile.write("\nLong ago, you read a book. It was an extraordinary book. \
You haven't thought about it in years, \
though, until this afternoon, when \
you remembered the book in a moment of drowsiness. *That book!* What \
was it called? Alas! You have forgotten the title.\n\nBut you feel sure \
that you could recognize it by sight, or at least in reading the \
first few pages. \
And surely one of the public libraries of New York City will have \
this book in their collections. You must find it; you must \
read it. It's only 4:00. You have time. \
You pocket your MetroCard and \
leave your apartment, heading to the nearest library branch.\n")

#picklibrary 
libfilename = open('nyc_public_libraries.tsv','r')
liblistraw = libfilename.read()
libfilename.close()
liblistraw = liblistraw.split('\r')
liblist = [l.split('\t') for l in liblistraw]
liblist = liblist[1:-1]
shuffle(liblist)

#for i in liblist[:5]:
for i in liblist[:-1]:
    outfile.write('\n___\n')
    outfile.write('\nYou arrive at %s and find yourself on the steps of %s.\n' % (i[1][1:-1], i[2]))
    print i[2]
    success = False
    while not success: #ignore 404 errors
        try:
            s = excerpt.readbook()
            success = True
        except:
            pass
    outfile.write(s[0])
    outfile.write(s[1])
    outfile.write(s[2])

endings = ["'Yes!' you shout, remembering too late that you are in a library. You are holding the book you've been searching for all evening. You hurry to the circulation desk to check it out, the last patron of the night.\n\nYou rush home, looking forward to enjoying the book once more over tea. ", \
"You smile to yourself. Yes, this book, this is the book. You walk to the checkout desk at 4:59pm, just before the library closes. On the train back to your apartment, you open to page 1.", \
"You can't believe it. You found it! You hug the book to your chest and hurry to the circulation desk to check it out before they close up for the night.\n\nAs soon as you're on the subway platform, you begin reading.", \
"'Library's closing,' the security guard announces. Your heart sinks. This was the last library on your list, and this isn't the book. You'll come back tomorrow morning to walk through the stacks more carefully.\n\nIt's out there: you just have to find it. ", \
"This isn't the book, either... Maybe the book you think you remember doesn't exist. Maybe you dreamed it. As the librarians close up for the night, you walk slowly toward the door. \n\nThe memory of the book is already starting to fade.", \
"It's 5:00, and the library is closing.\n\nYou don't think this is the book, but it still piqued your interest. You want to keep reading. You check it out and head home to read it."]

end = endings[randint(0,len(endings)-1)] # choose 1 of 6 possible endings

i = liblist[-1]
outfile.write('\n___\n')
outfile.write('\nThis is the last library branch on your list: %s at %s.\n' % (i[2], i[1][1:-2]))
print i[2]
success = False
while not success: #ignore 404 errors
    try:
        s = excerpt.readbook()
        success = True
    except:
        pass

outfile.write(s[0])
outfile.write(s[1])
outfile.write('\n\n')
outfile.write(end)
outfile.write('\n\n## The End')

outfile.write('\n\n# Appendix A\n## Books you read, in order\n\n')
for b in excerpt.appendixa():
    b = '- *' + b + '*\n'
    outfile.write(b)

outfile.write('\n\n# Appendix B\n## Libraries you visited, in order\n\n')
for i in liblist:
    l = '- ' + i[2] + ' at ' + i[1][1:-2] + ' (' + i[0] + ')\n'
    outfile.write(l)

outfile.write('\n\n___\n\n[Code repository on GitHub](https://github.com/robincamille/nanogenmo2016)\n\
*Code and outputs: CC-BY-NC.\nRobin Camille Davis, 2016.*')

outfile.close()
