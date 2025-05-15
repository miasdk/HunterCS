### Chapter 10: Algorithm Design Techniques 
10.1 Greedy Algorithms
The first type of algorithm we will examine is the greedy algorithm. We have already seen
three greedy algorithms in Chapter 9: Dijkstra’s, Prim’s, and Kruskal’s algorithms. Greedy
algorithms work in phases. In each phase, a decision is made that appears to be good,
without regard for future consequences. Generally, this means that some local optimum is
chosen. This “take what you can get now” strategy is the source of the name for this class of
algorithms. When the algorithm terminates, we hope that the local optimum is equal to the
global optimum. If this is the case, then the algorithm is correct; otherwise, the algorithm has
produced a suboptimal solution. If the absolute best answer is not required, then simple
greedy algorithms are sometimes used to generate approximate answers, rather than using
the more complicated algorithms generally required to generate an exact answer.

