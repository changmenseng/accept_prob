import numpy as np
import sys

s_ths = np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5])
s_main_per_margins = np.array([8, 110, 843, 1655, 208])
s_findings_per_margins = np.array([16, 325, 1290, 902, 51])
s_reject_per_margins = np.array([310, 2350, 2702, 686, 43])

e_ths = np.array([0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25])
e_main_per_margins = np.array([0, 7, 45, 152, 419, 895, 1107, 178, 21])
e_findings_per_margins = np.array([4, 33, 143, 419, 692, 738, 457, 59, 9])
e_reject_per_margins = np.array([95, 390, 1090, 1642, 1450, 1016, 397, 38, 2])

def get_margin_id(v, ths):
    n = len(ths)
    for i in range(n - 1):
        if ths[i] <= v < ths[i + 1]:
            return i
    return -1

if __name__ == '__main__':
    avg_s, avg_e = list(map(float, sys.argv[1:]))
    if avg_s < 0.5 or avg_s >= 5.5:
        raise ValueError(f'Average soundness should larger than 0.5 and smaller than 5.5, but get {avg_s}.')
    if avg_e < 0.75 and avg_e >= 5.25:
        raise ValueError(f'Average excitement should larger than 0.75 and smaller than 5.25, but get {avg_e}.')
    s_id = get_margin_id(avg_s, s_ths)
    e_id = get_margin_id(avg_e, e_ths)
    accept_probs = np.array([
        0.22 * (s_main_per_margins[s_id] / s_main_per_margins.sum()) * (e_main_per_margins[e_id] / e_main_per_margins.sum()),
        0.13 * (s_findings_per_margins[s_id] / s_findings_per_margins.sum()) * (e_findings_per_margins[e_id] / e_findings_per_margins.sum()),
        0.65 * (s_reject_per_margins[s_id] / s_reject_per_margins.sum()) * (e_reject_per_margins[e_id] / e_reject_per_margins.sum()),
    ])
    accept_probs /= accept_probs.sum()
    print(f'Main: {accept_probs[0]}\nFindings: {accept_probs[1]}\nReject: {accept_probs[2]}')
