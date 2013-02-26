# recursively generates the lyrics to "Hey Jude"


def heyJude(repeats):
    if repeats == 0:
        print "Na na na na na na na... (fade out)"
    else:
        print "Na na na na na na na, na na na na, hey Jude."
        heyJude(repeats)
                
heyJude(15)