from genanki import Model, Deck, Note, Package

MODEL_ID = 2544947637 # random number generator was used to get this number
DECK_ID = 2059400110
my_model = Model(
    MODEL_ID,
    'vocab model',
    fields=[
        {'name': 'Word' },
        {'name': 'Def'},
    ],
    templates=[
        {'name': 'Card 1',
         'qfmt': '{{Word}}',
         'afmt': '{{Def}}'
        }
    ]    
)

my_note = Note(model=my_model, fields=['word','def<br><img src="asian.png">'])
my_deck = Deck(DECK_ID, 'Vocab Words')
my_deck.add_note(my_note)

p = Package(my_deck)
p.media_files = ['/Users/yuhsinho/Desktop/img/asian.png']
p.write_to_file('out.apkg')

