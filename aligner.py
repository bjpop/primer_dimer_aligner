class Aligner(object):
    def __init__(self, match, mismatch, gap):
        self.match_score = match
        self.mismatch_score = mismatch
        self.gap_penalty = gap

    def substitution(self, base1, base2):
        if base1 == base2:
            return self.match_score 
        else:
            return self.mismatch_score 

    def align(self, s1, s2):
        self.memo = {}
        self.s1 = s1
        self.s2 = s2
        return self.align_rec(0, 0, True)

    def align_rec(self, i, j, start):
        if (i, j, start) in self.memo:
            return self.memo[(i, j, start)]
        if i >= len(self.s1) or j >= len(self.s2):
            result = 0
        else:
            match = self.align_rec(i + 1, j + 1, False) + \
                        self.substitution(self.s1[i], self.s2[j])
            if start:
                shift1 = self.align_rec(i + 1, j, True)
                shift2 = self.align_rec(i, j + 1, True)
            else:
                shift1 = self.align_rec(i + 1, j, False) - self.gap_penalty
                shift2 = self.align_rec(i, j + 1, False) - self.gap_penalty 
            result = max(match, shift1, shift2, 0)
        self.memo[(i, j, start)] = result
        return result
