class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        components = path.split("/")
        stack = []

        for component in components:
            if component == "..":
                if stack:
                    stack.pop()
            elif component and component != ".":
                stack.append(component)
        
        # print(stack)

        
        if not stack:
            return '/'

            
        return "/" + "/".join(stack)

        