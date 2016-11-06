# putting it all together...

from random import randint
from random import shuffle
##import urllib2
##from nltk import sent_tokenize as tok

#import picklibrary
import excerpt, time

outfile = open('drafts/' + str(time.time()) + '.md','w')

outfile.write("# If on an winter's night a library cardholder\n")

outfile.write("\nLong ago, you read a book. It was a wonderful book: transporting, \
enlightening, beautiful. Just this afternoon, \
you remembered this book in a moment of drowsiness. That book! What \
was it called? You have forgotten the title. What a pity. \n\n\
But surely one of the public libraries of New York City will have \
this book in their collections. It's only 4:00; you have time. \
You pocket your MetroCard and \
leave your apartment, heading to the first library branch on \
your list.\n")

#picklibrary 
libfilename = open('nyc_public_libraries.tsv','r')
liblistraw = libfilename.read()
libfilename.close()
liblistraw = liblistraw.split('\r')
liblist = [l.split('\t') for l in liblistraw]
liblist = liblist[1:-1]
shuffle(liblist)

for i in liblist[:-1]:
    outfile.write('\n_______________________________________________\n')
    outfile.write('\nYou arrive at %s and find yourself on the steps of %s.' % (i[1][1:-1], i[2]))
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

    time.sleep(3) #politeness

endings = ["'Yes!' you shout, remembering too late that you are in a library. You are holding the book you've been searching for all night long. You hurry to the circulation desk to check it out, the last patron of the night. You hurry home, looking forward to devouring the book once more over tea. ", \
"You smile to yourself. Yes, this book, this is the book. You walk to the checkout desk at 4:59pm, just before the library closes. On the train back to your apartment, you open to page 1. It's going to be a very good night. ", \
"You can't believe it. You found it! You hug the book to your chest and hurry to the circulation desk to check it out before they close up for the night. As soon as you're on the subway platform, you begin reading. ", \
"'Library's closing,' the security guard announces. Your heart sinks. This was the last library on your list, and this isn't the book. You'll come back tomorrow morning to walk through the stacks more carefully. It's out there: you just have to find it. ", \
"This isn't the book, either... Maybe the book you think you remember doesn't exist. Maybe you dreamed it. As the librarians close up for the night, you walk slowly toward the door. The memory of the book is already starting to fade.", \
"It's 5:00, and the library is closing. You don't think this is the book, but it still piqued your interest. You want to keep reading. You check it out and head home."]

end = endings[randint(0,len(endings)-1)]

i = liblist[-1]
outfile.write('\n_______________________________________________\n')
outfile.write('\nThis is the last library branch on your list: %s at %s.' % (i[2], i[1][1:-1]))
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
outfile.write('\n\nThe End')

time.sleep(3) #politeness

outfile.close()
