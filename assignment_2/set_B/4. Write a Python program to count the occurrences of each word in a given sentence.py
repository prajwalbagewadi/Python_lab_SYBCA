"""
4. Write a Python program to count the occurrences of each word in a given sentence.
"""

"""
input sentence:He took his hat and his leave
"""
#input string array
sentence=input("Enter a Sentence:")
#print(sentence)

def word_counter(sentence):
    #split string array seperator Space
    collector=sentence.split(" ")
    for word in collector:
        print("word=",word,end="\n")
        
    #occurance of each word
    # create a new dictionary to store all unique words with there count
    new_dict={}
    count=0
    # add the words from sentence into the dict as keys and count as val
    for word in collector:
        new_dict[word]=count
        
    #print the dict created
    print("new_dict=",new_dict,end="\n")
        
    #extract keys using keys() method
    key=new_dict.keys()
    #store it in obj convert the obj to list
    keys=list(key)
    print("dict_keys=",keys,end="\n")

    #compare word from sentence with key val to increament
    for word in collector:
        for key in keys:
            # if word exists in keys list increament
            if word==key:
                new_dict[word]+=1
        
    #print the dict created
    print("word_count=",new_dict,end="\n")
        
#function call        
word_counter(sentence)
