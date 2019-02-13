def vlag(richting, kleuren):

    vlag = ''

    if richting == 'verticaal':
        streepje =  ' | '
    else:
        streepje = '\n-\n'

    for kleur in kleuren:
        vlag += kleur + streepje

    return vlag[:-3]

print(vlag('horizontaal',('rood', 'wit', 'blauw')))
