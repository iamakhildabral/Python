class stack(list):

       def __init__(self):
              self.stack = list() # Stack Creation

       def push(self,object):
              self.append(object)

       def top(self):
              return len(self.stack)


if __name__ == "__main__":
       s = stack()
       s.push(32)
       s.push("akhil")
       print(s.pop())
       print(s.top())
