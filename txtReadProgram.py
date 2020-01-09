
from win32gui import FindWindow, FindWindowEx, SendMessage, PyGetString
from win32con import WM_GETTEXT, WM_GETTEXTLENGTH
from array import array

main_window = FindWindow('Notepad', None)
print('main window handle = {:08x}'.format(main_window))
assert main_window

edit_control = FindWindowEx(main_window, None, 'Edit', None)
print('edit control handle = {:08x}'.format(edit_control))
assert edit_control

buffer_len = SendMessage(edit_control, WM_GETTEXTLENGTH, 0, 0) + 1
buffer = array('b', b'\x00\x00' * buffer_len)
text_len = SendMessage(edit_control, WM_GETTEXT, buffer_len, buffer)
text = PyGetString(buffer.buffer_info()[0], buffer_len - 1)
print('WM_GETTEXT returned {!r}'.format(text))