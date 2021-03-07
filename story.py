#!/data/data/com.termux/files/usr/bin/python

owner = 'gumma'
point_in_time = 'kvällen'

threat_chain = [['getabock', 'gå hem'],
                ['varg', 'bita'],
                ['björn', 'riva'],
                ['skytt', 'skjuta'],
                ['fura', 'fälla'],
                ['yxa', 'hugga'],
                ['eld', 'bränna'],
                ['vatten', 'släcka'],
                ['oxe', 'dricka'],
                ['slaktare', 'slakta'],
                ['rep', 'hänga'],
                ['råtta', 'gnaga sönder'],
                ['katt', 'äta'],
                ]

global vowels
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']

def definite(word : str) -> str:
    if word[-1] in vowels:
        word=word+'n'
    else:
        word=word+'en'
    return word

print('Sagan om ' + definite(owner) + ' och ' + definite(threat_chain[0][0]) + ' som inte ville ' + threat_chain[0][1])

input('Press return key to change page...')

print('Det var en gång en ' + owner + ' som hade en ' + threat_chain[0][0] + ' som inte ville ' + threat_chain[0][1] + ' på ' + point_in_time)

chapter_start = 'Då bad ' + definite(owner)
refusal_chain_text = ' på ' + point_in_time + '.'
execution_chain_text = ' som inte ville ' + threat_chain[0][1] + '.'
for i in range(1, len(threat_chain)):
    prev_noun, prev_verb = threat_chain[i-1]
    noun, verb = threat_chain[i]
    expression_of_not_wanting = ' ' + definite(prev_noun) + ' som inte ville ' + prev_verb
    refusal_chain_text = expression_of_not_wanting + refusal_chain_text
    chapter_unique = ' en ' + noun + ' att ' + verb
    print(chapter_start + chapter_unique + refusal_chain_text)
    execution_chain_text = definite(noun) + ' på ' + definite(prev_noun) + ' och ' + execution_chain_text
    if i == len(threat_chain) - 1:
        print(definite(noun).capitalize() + ' sa ja!')
    else:
        print('Men ' + definite(noun) + ' sa nej.')
        input()

print('Då blev det ' + execution_chain_text)

