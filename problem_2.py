import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    sol = []
    for fil in os.listdir(path):

        if os.path.isfile(path + "/" + fil):
            if fil.endswith(suffix):
                sol.append(path + "/" + fil)
        else:
            sol = sol + find_files(suffix, path + "/" + fil)

    return sol

def test_find_files():

    assert(find_files(".c", "./testdir_p_2") == ['./testdir_p_2/subdir1/a.c', './testdir_p_2/subdir3/subsubdir1/b.c', './testdir_p_2/subdir5/a.c', './testdir_p_2/t1.c'])
    assert(find_files(".gitkeep", "./testdir_p_2") == ['./testdir_p_2/subdir2/.gitkeep', './testdir_p_2/subdir4/.gitkeep'])

if __name__ == "__main__":
    test_find_files()