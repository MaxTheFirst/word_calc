import win32com.client as win32
from calc import get_calc

def get_selections():
    word = win32.gencache.EnsureDispatch('Word.Application')
    doc = word.ActiveDocument
    return word.Selection

def main():
    selection = get_selections()
    omaths = selection.OMaths(1)
    omaths.Linearize()
    result = get_calc(selection.Range.Text.strip())
    selection.InsertAfter('='+result)
    omaths.BuildUp()

if __name__ == '__main__':
    main()

