class AbilityScore:
    SCORE_MIN = 0
    SCORE_MAX = 30

    def __init__(self, score=10):
        self._score = self._check_score(score)

    def _check_score(self, score):
        score = int(score)
        if score > self.SCORE_MAX:
            raise ValueError('{} is too much'.format(score))
        if score < self.SCORE_MIN:
            raise ValueError('{} is too low'.format(score))
        return score

    def _get_modifier(self):
        return (self._score - 10)//2

    def _get_modifier_str(self):
        modifier = self._get_modifier()
        return str(modifier) if modifier < 0 else '+' + str(modifier)

    def to_string(self):
        return '{score} [{modifier}]'.format(
            score=self._score,
            modifier=self._get_modifier_str())


dex = AbilityScore()
print(dex.to_string())
con = AbilityScore(19)
print(con.to_string())