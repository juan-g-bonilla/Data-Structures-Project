class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def is_user_in_group(self, user):
        """
        Return True if user is in the group (or any sub-group), False otherwise.

        Args:
        user(str): user name/id
        """
        if user in self.users:
            return True

        for g in self.groups:
            if g.is_user_in_group(user):
                return True

        return False

if __name__ == "__main__":

    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    parent.add_user("parent_user")
    child.add_user("child_user")
    sub_child.add_user("sub_child_user")

    child.add_group(sub_child)
    parent.add_group(child)

    assert(parent.is_user_in_group("parent_user"))
    assert(parent.is_user_in_group("child_user"))
    assert(parent.is_user_in_group("sub_child_user"))
    assert(not parent.is_user_in_group("intruder"))
    assert(not parent.is_user_in_group(""))
    assert(not parent.is_user_in_group(None))