class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        method_add = self.items.append(item)
        return self.items

    def pop(self):
        method_pop = self.items.pop()
        return self.items[-1]

    def peek(self):
        method_peek = self.items[-1]
        return method_peek

    def size(self):
        return len(self.items)


class StackBrackets:
    def __init__(self, stack: str):
        self.stack = stack
        self.goodstack = True

    def check(self):
        stacklist = []

        for i in self.stack:
            if i in "({[":
                stacklist.append(i)

            elif i in "]})":
                if not stacklist:
                    self.goodstack = False
                    break

                open_bracket = stacklist.pop()
                if open_bracket == "(" and i == ")":
                    continue

                if open_bracket == "{" and i == "}":
                    continue

                if open_bracket == "[" and i == "]":
                    continue

                self.goodstack = False
                break

        if self.goodstack and len(stacklist) == 0:
            return "good stack"
        else:
            return "bad stack"


firststack = StackBrackets("[([])((([[[]]])))]{()}{{[()]}}")
print(firststack.check())
