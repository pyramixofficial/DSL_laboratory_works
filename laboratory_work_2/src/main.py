from grammar import Grammar

def main():
    VN = {'S', 'P', 'Q'}
    VT = {'a', 'b', 'c', 'd', 'e', 'f'}
    P = {
        'S': ['aP', 'bQ'],
        'P': ['bP', 'cP', 'dQ', 'e'],
        'Q': ['eQ', 'fQ', 'a']
    }
    S = 'S'
    grammar = Grammar(VN, VT, P, S)
    print(grammar.compute_type())

if __name__ == "__main__":
    main()    
