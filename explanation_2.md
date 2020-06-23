The find_files() functions is called recursively each time it encounters a subdirectory.
Time complexity is O(n) where n is the files and subfolders that are, no matter how deeply, contained in the root file

Space complexity is O(n), since in the worst case every file under the folder has the desired suffix and all of them have to be stored before being returned.