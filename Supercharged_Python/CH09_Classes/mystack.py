class Stack(list):
    
    def push(self, v):
        self.append(v)
    
    def peek(self):
        return self[-1]

    def __iter__(self):
        self.current = 0
        return self
        
    def __next__(self):
        if self.current < len(self):
            self.current += 1
            return self[self.current - 1]
        else:
            raise StopIteration

st = Stack()
st.push(10)
st.push(20)
st.push(30)
st.push(40)
print('Size of stack is:', len(st))
print('First element is:', st[0])
print('The top of the stack is:', st.peek())
print(st.pop())
print(st.pop())
print(st.pop())
print('Size of stack is:', len(st))