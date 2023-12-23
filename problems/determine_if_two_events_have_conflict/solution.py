class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1_start, event1_end = event1
        event2_start, event2_end = event2
        return False if event2_start > event1_end or event1_start > event2_end else True