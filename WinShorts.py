import os, sys


def check_win():
    if sys.platform in ["win32", "cygwin"]:
        return True
        import glob
        import pythoncom
        from win32com.shell import shell, shellcon
        import win32com.client
    else:
        return False
check_win()

#get the target of a shortcut 
#http://timgolden.me.uk/python/win32_how_do_i/read-a-shortcut.html
def shortcut_target(filename):
  link = pythoncom.CoCreateInstance (
    shell.CLSID_ShellLink,    
    None,
    pythoncom.CLSCTX_INPROC_SERVER,    
    shell.IID_IShellLink
  )
  link.QueryInterface (pythoncom.IID_IPersistFile).Load (filename)
  #
  # GetPath returns the name and a WIN32_FIND_DATA structure
  # which we're ignoring. The parameter indicates whether
  # shortname, UNC or the "raw path" are to be
  # returned. Bizarrely, the docs indicate that the 
  # flags can be combined.
  #
  name, _ = link.GetPath (shell.SLGP_UNCPRIORITY)
  return name

def find_links(depth = 0):
    #dest = path linked to, depth: 0 = only start menu and desktop (faster), 1 = all files/folders (slow)
    _shell_ = win32com.client.Dispatch("WScript.Shell")
    files = []
    if depth == 0:
        #Desktop
        path = shell.SHGetSpecialFolderPath (None, shellcon.CSIDL_DESKTOP)
        files = glob.glob(os.path.join (path, "*.lnk"))

        #Start Menu
        path = shell.SHGetSpecialFolderPath  (None, shellcon.CSIDL_STARTMENU)
        files = files + glob.glob(os.path.join (path, "*.lnk"))

        #Common Start Menu
        path = shell.SHGetSpecialFolderPath  (None, shellcon.CSIDL_COMMON_STARTMENU)
        files = files + glob.glob(os.path.join (path, "*.lnk"))

    if depth == 1:
    #walk through whole hardrive
    #http://stackoverflow.com/questions/16465399/need-the-path-for-particular-files-using-os-walk
        files = []
        for root, dirnames, filenames in os.walk('C:\\'):               #r = raw string
            for filename in filenames:
                if filename.endswith(('.lnk')):
                    files.append(os.path.join(root, filename))
        
    return files

def change_links(old_dest, new_dest, files):
    for filename in files:      #loop through all links (shortcuts)
            # print "filename= ", filename
            #shortcut = _shell_.CreateShortCut(filename)  #old way
            #target = shortcut.Targetpath

            shortcut = pythoncom.CoCreateInstance (
                shell.CLSID_ShellLink,
                None,
                pythoncom.CLSCTX_INPROC_SERVER,
                shell.IID_IShellLink)
            shortcut_path = filename
            persist_file = shortcut.QueryInterface (pythoncom.IID_IPersistFile)
            persist_file.Load (shortcut_path)
            name, _ = shortcut.GetPath (shell.SLGP_RAWPATH)
            icon, _ = shortcut.GetIconLocation()
            # print "Name = ", name
            # print "Icon= ", icon

            # if the right one change it
            if icon == old_dest or (name == old_dest and icon == ""):
                print "changing: ", filename
                shortcut.SetPath (new_dest)
                shortcut.SetDescription ("Updated by Python to %s" %new_dest)
                shortcut.SetIconLocation (old_dest, 0)

                persist_file.Save (shortcut_path, 0)


if __name__ == "__main__":
    #Desktop = shell.SHGetSpecialFolderPath (None, shellcon.CSIDL_DESKTOP)
    new_dest = "C:\Windows\System32\calc.exe" #QtGui.QFileDialog.getOpenFileName(parent, 'Orriginal Link Destination', '/home')
    old_dest = "C:\Windows\System32\mspaint.exe" #QtGui.QFileDialog.getOpenFileName(
                   #parent, 'New Link Destination', '', 'Executables (*.exe)',
                   #'', QtGui.QFileDialog.DontUseNativeDialog)
    files = find_links()
    print files
    if files:
        print "2"
        change_links(new_dest, new_dest, files) 

#refrences
    #http://www.blog.pythonlibrary.org/2010/02/13/using-python-to-edit-bad-shortcuts/

    #http://timgolden.me.uk/python/win32_how_do_i/read-a-shortcut.html
    #http://stackoverflow.com/questions/6805881/modify-windows-shortcuts-using-python
    #more info
    #http://timgolden.me.uk/python/win32_how_do_i/create-a-shortcut.html
    #http://www.blog.pythonlibrary.org/2010/02/25/creating-windows-shortcuts-with-python-part-ii/

#all explained....

#http://ashishpython.blogspot.com/2014/09/create-shortcuts-using-python-for.html

#Icon stuff
    #http://blogs.technet.com/b/heyscriptingguy/archive/2005/08/12/how-can-i-change-the-icon-for-an-existing-shortcut.aspx

#Windows Shell
    # Get Icon
    # https://msdn.microsoft.com/en-us/library/windows/desktop/bb774940(v=vs.85).aspx
    # Get Path
    # https://msdn.microsoft.com/en-us/library/windows/desktop/bb774944(v=vs.85).aspx
