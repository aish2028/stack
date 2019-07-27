class Stack:
    def __init__(self):
        self.st=[]

    def push(self,ele):
        self.st.append(ele)
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            ele=self.st.pop()
            print(f"element {ele} is removed from the stack")
    def search(self,searchEle):
        if self.is_empty():
            print("stack is empty")
        else:
            for index,ele in enumerate(self.st):
                if ele==searchEle:
                    return index
                return -1
    def show(self):
        if self.is_empty:
            print("stack is empty")
        else:
            print(self.st)
    def is_empty(self):
        return len(self.st)==0

if __name__=="__main__":
    st=Stack()
    opt_dict={1:st.push,2:st.pop,3:st.search,4:st.show,5:exit}
    while True:
        print("1.push 2.pop 3.search 4.display 5.exit")
        try:
            ch=int(input("enter your choice:"))
            if ch==1:
                ele=int(input('enter the elemnt to be pushed:'))
                st.push(ele)
            elif ch==2:
                st.pop()
            elif ch==3:
                ele=input("enter the element to search:")
                res=st.search(ele)if res!= -1
                print(f"element {ele} found in location")
            ref=opt_dict[ch]
            ref()
        except (ValueError,KeyError):
            print("enter only numbers from 1 to 5")