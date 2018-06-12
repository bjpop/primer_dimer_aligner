from align_rec import Aligner

def complement(base):
    if base == 'A':
        return 'T'
    elif base == 'T':
        return 'A'
    elif base == 'G':
        return 'C'
    elif base == 'C':
        return 'G'
    else:
        return base

def reverse_complement(seq):
    return "".join([complement(base) for base in seq[::-1]])

def test1():
    primer = "CCCCCGGGGAAACACTTTTAAAA"
    template = "GCCAATTTAAAAAATTTGGGGCATATCTCAGCGCAGC"
    rc_primer = reverse_complement(primer)
    print("aligning: {} with {}".format(rc_primer, template))
    print(Aligner(match=3, mismatch=-3, gap=2).align(rc_primer, template))

def test2():
    s1 = "TGTTACGG"
    s2 = "GGTTGACTA"
    print("aligning: {} with {}".format(s1, s2))
    print(Aligner(match=3, mismatch=-3, gap=2).align(s1, s2))

def main():
    test1()
    test2()

if __name__ == '__main__':
    main()
