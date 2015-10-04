#!/usr/bin/env python
"""This is my doc string.

Keyword arguments:
A -- apple
"""
# Copyright 2015 Austin Fox
# Program is distributed under the terms of the
# GNU General Public License see ./License for more information.

import os
import sys
import glob
import fnmatch
import pythoncom
import re
import win32com
from win32com.shell import shell, shellcon
import win32com.client


def check_win():
    if sys.platform in ["win32", "cygwin"]:
        print "windows"
        return True
    else:
        return False


# get the target of a shortcut
# http://timgolden.me.uk/python/win32_how_do_i/read-a-shortcut.html
def shortcut_target(filename):
    link = pythoncom.CoCreateInstance(
        shell.CLSID_ShellLink,
        None,
        pythoncom.CLSCTX_INPROC_SERVER,
        shell.IID_IShellLink
    )
    link.QueryInterface(pythoncom.IID_IPersistFile).Load(filename)
    # GetPath returns the name and a WIN32_FIND_DATA structure
    # which we're ignoring. The parameter indicates whether
    # shortname, UNC or the "raw path" are to be
    # returned. Bizarrely, the docs indicate that the
    # flags can be combined.
    name, _ = link.GetPath(shell.SLGP_UNCPRIORITY)
    icon, _ = shortcut.GetIconLocation()
    return name, icon


def find_all_links(depth=0):
    """depth: 0 = only start menu and desktop (faster)
              1 = all files/folders (slow)
    """
    _shell_ = win32com.client.Dispatch("WScript.Shell")
    files = []
    if depth == 0:
        # Path Lo Cals - https://msdn.microsoft.com/en-us/library/windows/desktop/bb762494(v=vs.85).aspx
        places = [shellcon.CSIDL_DESKTOP,
                  shellcon.CSIDL_COMMON_DESKTOPDIRECTORY,
                  shellcon.CSIDL_STARTMENU,
                  shellcon.CSIDL_COMMON_STARTMENU]
        for place in places:
            path = shell.SHGetSpecialFolderPath(None, place)
            # print path
            # files = glob.glob(os.path.join(path, "*.lnk"))
            for root, dirnames, filenames in os.walk(path):
                for filename in fnmatch.filter(filenames, '*.lnk'):
                    # print root
                    files.append(os.path.join(root, filename))

    if depth == 1:
        """walk through whole hardrive
        http://stackoverflow.com/questions/16465399/
        need-the-path-for-particular-files-using-os-walk
        """
        files = []
        path = 'C:\\'
        # begining - one or more of anything but a $ - .lnk - end
        prog = re.compile(r"^[^\$]+\.lnk$", re.I)  # I flag to ignore case
        for root, dirnames, filenames in os.walk(path):  # r = raw string
            for filename in filenames:
                if prog.match(filename):
                    # print filename
                    files.append(os.path.join(root, filename))
    return files


def find_links_to_path(path, files):
    matches = []
    path = path.lower()
    for filename in files:  # loop through all links (shortcuts)
            # print "filename= ", filename
            shortcut = pythoncom.CoCreateInstance(
                shell.CLSID_ShellLink,
                None,
                pythoncom.CLSCTX_INPROC_SERVER,
                shell.IID_IShellLink)
            shortcut_path = filename
            persist_file = shortcut.QueryInterface(pythoncom.IID_IPersistFile)
            persist_file.Load(shortcut_path)
            name, _ = shortcut.GetPath(shell.SLGP_RAWPATH)
            icon, _ = shortcut.GetIconLocation()
            # print "Name = ", name
            # print "Icon= ", icon
            name = name.lower()
            icon = icon.lower()
            # if the right one change it
            if icon == path or (name == path and icon == ""):
                matches.append([shortcut, shortcut_path])

    return matches


def change_link(shortcut, shortcut_path, path, new_path):
    print "changing: ", shortcut_path
    persist_file = shortcut.QueryInterface(pythoncom.IID_IPersistFile)
    shortcut.SetPath(new_path)
    shortcut.SetDescription("Updated by Python to %s" % new_path)
    shortcut.SetIconLocation(path, 0)
    persist_file.Save(shortcut_path, 0)


if __name__ == "__main__":
    # Desktop = shell.SHGetSpecialFolderPath (None, shellcon.CSIDL_DESKTOP)
    new_dest = "C:\Windows\System32\calc.exe"
    old_dest = "C:\Windows\System32\mspaint.exe"
    print "testing"
    files = find_all_links(0)
    # print files
    matches = find_links_to_path(old_dest, files)
    print 'matches', matches
    for match in matches:
        resp = raw_input("Change %s ?(y,n)" % match[1])
        if resp == "y":
            print "Changing %s" % match[1]
            change_link(match[0], match[1], old_dest, old_dest)

# refrences
# http://www.blog.pythonlibrary.org/2010/02/13/using-python-to-edit-bad-shortcuts/
# http://timgolden.me.uk/python/win32_how_do_i/read-a-shortcut.html
# http://stackoverflow.com/questions/6805881/modify-windows-shortcuts-using-python

# more info
# http://timgolden.me.uk/python/win32_how_do_i/create-a-shortcut.html
# http://www.blog.pythonlibrary.org/2010/02/25/creating-windows-shortcuts-with-python-part-ii/

# all explained....

# http://ashishpython.blogspot.com/2014/09/create-shortcuts-using-python-for.html

# Icon stuff
# http://blogs.technet.com/b/heyscriptingguy/archive/2005/08/12/how-can-i-change-the-icon-for-an-existing-shortcut.aspx

# Windows Shell
# Get Icon
# https://msdn.microsoft.com/en-us/library/windows/desktop/bb774940(v=vs.85).aspx
# Get Path
# https://msdn.microsoft.com/en-us/library/windows/desktop/bb774944(v=vs.85).aspx
