class Solution:
    # ['', 'home', 'user', '', '', 'Documents', '..', 'Pictures']
    def simplifyPath(self, path: str) -> str:
        hold = path.split("/")
        stack = []

        for char in hold:
            if len(stack) != 0 and char == '..':
                stack.pop()
            elif len(char) != 0 and char != "." and char != "..":
                stack.append(char)

        return "/" + "/".join(stack)