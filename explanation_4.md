Takes O(n) time, where n is the total number of users and groups, now matter how deep, contained in the given group.

self.users is checked before self.groups to avoid as much recursion as possible
