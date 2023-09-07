This script calculate the probability of a paper being accepted by EMNLP2023 based on [score distribution of ACL2023](https://aclanthology.org/2023.acl-long.0.pdf). Use this script like:
```shell
python accept_prob.py 3 4
```
where the first score 3 is the average soundness, and the second score 4 is the average excitement. It will output:
```shell
Main: 0.4592064544731725
Findings: 0.20714542818067555
Reject: 0.3336481173461519
```
Basically, I count pixels in Figure 5(d) in to estimate the number of papers with scores in every range in that histogram to get the score distribution of all the results including main, findings, and reject. Then a paper being accepted as a main is computed as the posterior $p(M|s\in r_i^s,e\in r_j^e)\propto p(s\in r_i^s|M)p(s\in r_j^e|M)p(M)$, where $r_i^s$/$r_j^e$ is a specific soundness and excitement range in the histogram. This probability is just for reference given that I might have errors in counting the number in the histogram (which is hard because one has to count the pixels), and it assumes soundness and excitement to be independent given the result (because there doesn't exist a 2-D histogram for full conditional estimation).
