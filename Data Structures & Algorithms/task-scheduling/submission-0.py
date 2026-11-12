class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=Counter(tasks)

        mf=max(c.values())
        mc=sum( 1 for x in c.values() if x==mf)


        return max(len(tasks), (mf - 1) * (n + 1) + mc)