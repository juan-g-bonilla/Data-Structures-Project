Takes O(n) time, where n is the total number of users and groups, now matter how deep, contained in the given group.

self.users is checked before self.groups to avoid as much recursion as possible

Space complexity of is_user_in_group() is O(1) since no variables are created for the method.