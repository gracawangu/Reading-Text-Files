# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    
    with open('story.txt') as f:
        text = f.read()
        return text
       
print(read_file_content('story.txt'))
     

def count_words(text):
    text = read_file_content("story.txt")
    for char in '.,?':
        text = text.replace(char, " ")
  
    dict = {}
    for unique_words in text.split():
        
        if unique_words in dict: 
            dict[unique_words] +=1
            
        else:
            dict[unique_words] = 1

    return dict

print(count_words("story.txt"))
 
       

