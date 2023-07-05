from pywinauto.application import Application
app = Application(backend="win32").start('notepad.exe').connect(title='Untitled - Notepad')

# describe the window inside Notepad.exe process
dlg_spec = app.UntitledNotepad
# wait till the window is really open
actionable_dlg = dlg_spec.wait('visible')
app.UntitledNotepad.print_control_identifiers()