
from win32com.client import Dispatch

wort = 'Naechrcht'

app = Dispatch('Word.Application')
app.Documents.Add()

if app.CheckSpelling(wort):
    print('Wort ist korrekt geschrieben!')
else:
    print('Wort ist falsch geschrieben!')
    print('Vorschlaege:')
    for wort in app.GetSpellingSuggestions(wort):
        print(wort)
