#get random para of gutenberg text 

import urllib2
from nltk import sent_tokenize as tok
from random import randint

# get list of all books in GITenberg
pgfilename = open('GITenberg_repos_list_2.tsv','r')
pglistraw = pgfilename.read()
pgfilename.close()

pglistraw = pglistraw.split('\n')

pglistlong = [l.split('\t') for l in pglistraw]
pglist = []
for b in pglistlong:
    if len(b) == 7:
        pglist.append(b)

usedbooks = []
foundit = ["You browse the shelves and find yourself attracted to a \
book entitled *%s*. Is this the one you've been looking for?", "You approach \
a kindly librarian and ask him about a the book you're seeking. 'I think it \
had a red cover,' you add.\n\nHis eyes light up. 'Ah! You must mean *%s*.' \
He leads you to the book and plucks it from the shelf.", "\
As soon as you enter, you see a familiar-looking book on display in an \
exhibit. You snatch it up and read the title: *%s*.", "As you walk through \
the stacks, you bump into a tall woman. 'Excuse me,' you murmur. 'I was \
just looking for a book.'\n\nShe smiles politely and shelves the book \
she was holding. It looks familiar... *%s*, it's called.", "While browsing \
the stacks, something heavy suddenly falls onto your head. 'Ouch!' you \
shout. But no one is nearby. You rub your cranium and look at the \
book that fell on you. '*%s*,' you mutter. Perhaps this was a sign.", "You \
walk every aisle, but nothing looks promising. Suddenly, a young man rushes \
past you, and a book falls out of his bag. 'Hey!' you call after him, \
but he has already left. You pick up the book and read the title: *%s*. \
It has a red cover and a familiar weight in your hand.", "\
You approach a librarian who is wearing smart tortoiseshell glasses. 'Can I help you?' \
she asks.\n\n'I hope,' you reply. 'I'm looking for a book, but can't \
remember the title. I think it had a red cover...'\n\nShe waits for more \
information, and when you offer none, she makes a small sound in her \
throat.\n\n'Well, this one is a classic, and several other patrons have \
sought it out recently,' she says politely, leading you to a shelf with \
a familiar-looking red book on it. 'Lovely title, isn't it?' she adds. \
'*%s*.'"]

leave = ["\n\nYou close the book, disappointed. This isn't the book you were thinking of. It must be in a different library. You set off for the next branch on your list.", \
"\n\nThis is not the book. You snap it shut, beginning to feel despondent. But it might be in a different library. You leave in a hurry for the next branch on your list. ", \
"\n\nNo, this can't be it. You shelve the book and leave quickly. It's getting dark outside, and there isn't much time left. You head to the next nearest library branch. ", \
"\n\nThis doesn't sound familiar at all. Frowning, you leave the book on a reshelving cart and stride out into the evening air, ready to try another library branch. ", \
"\n\nYou stop reading. This isn't your book, this is some other strange text. You leave it on the shelf and go outside. Time to try the next library branch. ", \
"\n\nNo, this isn't the book you had in mind, although it does intrigue you. You consider checking it out, but you don't have much time before the next branch closes. You go outside and point your feet toward the next branch on your list."]

def randombook():
    book = pglist[randint(1,32867)]
    return book

def pickbook():
    mybook = randombook()
    while mybook[0] in usedbooks:
        mybook = randombook()
    usedbooks.append(mybook[0])
    #found = 
    return int(mybook[0])



def readbook():
    bk = pglist[pickbook()] #pick #2000 from list
    number = bk[1]
    codetitle = bk[2]
    title = bk[3]

    intro = ['\n\n']
    intro.append(foundit[randint(0,len(foundit)-1)] % title)
    intro.append('\n\nYou flip to a random page and begin to read...\n\n')

    urll = 'https://raw.githubusercontent.com/GITenberg/' + codetitle + \
           '/master/' + number + '.txt'

    req = urllib2.Request(urll)
    response = urllib2.urlopen(req)
    the_page = response.read()

    ex = the_page[10000:11000]

    # stitch together line breaks
    ex = ex.split('\n')
    ex = ' '.join(ex)
    ex = ex.split('\r')
    ex = ' '.join(ex)

    # split into sentences
    exs = tok(ex)

    # start with second sentence, end with second-to-last
    blurb = '> ... ' + (' '.join(exs[1:-1])) + ' ...'

    outtro = (leave[randint(0,len(leave)-1)])

    return ' '.join(intro), blurb, outtro
