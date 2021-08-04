class Ternary_Search_Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.equal = None
        self.right = None
        self.is_end_of_string = False
    def insert(self,level,key):
        #print("after equal?")
        if key[level]<self.data:
            if self.left!=None:
                self.left.insert(level,key)
            else:
                self.left = Ternary_Search_Tree(key[level])
                self.left.insert(level,key)
        elif key[level]>self.data:
            if self.right!=None:
                self.right.insert(level,key)
            else:
                self.right = Ternary_Search_Tree(key[level])
                self.right.insert(level,key)
        else:
            if level!=len(key)-1:
        #        print("equal?")
                if self.equal!=None:
                    self.equal.insert(level+1,key)
                else:
                    self.equal = Ternary_Search_Tree(key[level+1])
                    self.equal.insert(level+1,key)
            else:
                self.is_end_of_string = True
    def traverse(self,buffer,depth):
            #print("after traverse",buffer,depth)
            if self.left!=None:
                self.left.traverse(buffer,depth)
            #print("after self.left",buffer,depth)
            buffer[depth] = self.data
            for i in range(depth+1,10):
                buffer[i]=""
            if self.is_end_of_string==True:
                print("".join(buffer))
            if self.equal!=None:
                self.equal.traverse(buffer,depth+1)
            #print("after self.equal",buffer,depth)
            if self.right!=None:
                self.right.traverse(buffer,depth)
            #print("after self.right",buffer,depth)

    def search(self,level,key):
        if key[level]<self.data:
            if self.left.data!=key[level]:
                return "No such word exists"
            else:
                return self.left.search(level,key)
        elif key[level]>self.data:
            if self.right.data!=key[level]:
                return "No such word exists"
            else:
                return self.right.search(level,key)
        else:
            if level==len(key)-1:
                return self.is_end_of_string
            #print(self.data)
            if self.equal==None or self.equal.data!=key[level+1]:
                return "No such word exists"
            return self.equal.search(level+1,key)

word = ["cat","cats","bug","up","upa","us","arunim","arun"]
t = Ternary_Search_Tree(word[0][0])
for i in word:
    #print(word.index(i))
    t.insert(0,i)
#printing all the words in Ternary Tree
t.traverse([""]*(10),0)
#Searching for a word in the Tree
print(t.search(0,"cats"))
print(t.search(0,"catf"))
