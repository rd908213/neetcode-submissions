class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elem in tokens:
            if elem.isdigit(): # Check if its a number
                stack.append(int(elem))
            elif elem[1:].isdigit(): # Account for negative numbers
                stack.append(int(elem[1:]) * -1)
            else:
                print("___________")
                print(stack)
                x = stack.pop()
                y = stack.pop()
                print(f"{y}{elem}{x}")
                match elem:
                    case "+":
                        stack.append(y + x)
                    case "-":
                        stack.append(y - x)
                    case "*":
                        stack.append(y * x)
                    case "/":
                        stack.append(int(y / x))
        return stack[0]
