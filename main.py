from Texts import Text
import Indexing
import Searching


path_1 = '/Users/picsartacademy/Downloads/1.txt'
path_2 = '/Users/picsartacademy/Downloads/2.txt'
text_instance2 = Text(path_2)
text_instance1 = Text(path_1)

print(Text.txt1)
print(Text.txt2)

indexing = Indexing.Index()
word = "efkjwb"
searching = Searching.Search()
searching.search(word)



