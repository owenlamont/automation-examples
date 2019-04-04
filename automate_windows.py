
#%%
from pywinauto.application import Application
from pywinauto import Desktop


#%%
app = Application().start("notepad.exe")
app.UntitledNotepad.menu_select("Help->About Notepad")
app.AboutNotepad.OK.click()
app.UntitledNotepad.menu_select("Format->Font")
app.Font.Edit3.type_keys("48")
app.Font.OK.click()
app.UntitledNotepad.Edit.type_keys("All your Notepad{VK_RETURN}are belong to us", with_spaces = True)


