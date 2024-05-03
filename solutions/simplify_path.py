# -*- coding: utf-8 -*-

################################################
#
# Leetcode 71. Simplify Path
# URL: https://leetcode.com/problems/simplify-path/description/
# Difficulty: Medium
#
################################################


class Solution:
    def simplify_path(self, path):
        dir_or_files = []
        path = path.split("/")
        for elem in path:
            if dir_or_files and elem == "..":
                dir_or_files.pop()
            elif elem not in [".", "", ".."]:
                dir_or_files.append(elem)

        return "/" + "/".join(dir_or_files)