from collections import namedtuple
# make a basic Link class
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes',
                           'title', 'url'])
links = [
    Link(0, 60398, 1334014208.0, 109,
         "C overtakes Java as the No. 1 programming language in the TIOBE index.",
         "http://pixelstech.net/article/index.php?id=1333969280"),
    Link(1, 60254, 1333962645.0, 891,
         "This explains why technical books are all ridiculously thick and overpriced",
         "http://prog21.dadgum.com/65.html"),
    Link(23, 62945, 1333894106.0, 351,
         "Learn Haskell Fast and Hard",
         "http://yannesposito.com/Scratch/en/blog/Haskell-the-Hard-Way/"),
    Link(2, 6084, 1333996166.0, 81,
         "Announcing Yesod 1.0- a robust, developer friendly, high performance web framework for Haskell",
         "http://www.yesodweb.com/blog/2012/04/announcing-yesod-1-0"),
    Link(3, 30305, 1333968061.0, 270,
         "TIL about the Lisp Curse",
         "http://www.winestockwebdesign.com/Essays/Lisp_Curse.html"),
    Link(4, 59008, 1334016506.0, 19,
         "The Downfall of Imperative Programming. Functional Programming and the Multicore Revolution",
         "http://fpcomplete.com/the-downfall-of-imperative-programming/"),
    Link(5, 8712, 1333993676.0, 26,
         "Open Source - Twitter Stock Market Game - ",
         "http://www.twitstreet.com/"),
    Link(6, 48626, 1333975127.0, 63,
         "First look: Qt 5 makes JavaScript a first-class citizen for app development",
         "http://arstechnica.com/business/news/2012/04/an-in-depth-look-at-qt-5-making-javascript-a-first-class-citizen-for-native-cross-platform-developme.ars"),
    Link(7, 30172, 1334017294.0, 5,
         "Benchmark of Dictionary Structures", "http://lh3lh3.users.sourceforge.net/udb.shtml"),
    Link(8, 678, 1334014446.0, 7,
         "If It's Not on Prod, It Doesn't Count: The Value of Frequent Releases",
         "http://bits.shutterstock.com/?p=165"),
    Link(9, 29168, 1334006443.0, 18,
         "Language proposal: dave",
         "http://davelang.github.com/"),
    Link(17, 48626, 1334020271.0, 1,
         "LispNYC and EmacsNYC meetup Tuesday Night: Large Scale Development with Elisp ",
         "http://www.meetup.com/LispNYC/events/47373722/"),
    Link(101, 62443, 1334018620.0, 4,
         "research!rsc: Zip Files All The Way Down",
         "http://research.swtch.com/zip"),
    Link(12, 10262, 1334018169.0, 5,
         "The Tyranny of the Diff",
         "http://michaelfeathers.typepad.com/michael_feathers_blog/2012/04/the-tyranny-of-the-diff.html"),
    Link(13, 20831, 1333996529.0, 14,
         "Understanding NIO.2 File Channels in Java 7",
         "http://java.dzone.com/articles/understanding-nio2-file")]

# make the function query() return the number of votes for the link whose ID is 15
# def query():
#   for x in links:
#       if x.id == 15:
#            return x.votes

            
# return a list of Links submitted by user 62443, by submission time ascending
def query():
    list_of_links = []
    for l in links:
        if l.submitter_id == 62443:
            list_of_links.append(l)
    list_of_links.sort(key = lambda x: x.submitted_time)
    return list_of_links

print query()
