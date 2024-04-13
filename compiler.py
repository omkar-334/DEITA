import re
import numpy as np

### Complexity
pattern = r'\[[1]\]\s*Score:\s*[0-9]\s*\[[2]\]\s*Score:\s*[0-9]\s*\[[3]\]\s*Score:\s*[0-9]\s*\[[4]\]\s*Score:\s*[0-9]\s*\[[5]\]\s*Score:\s*[0-9]'
pattern1 = r'\[[0-9]\]\s*Score:\s*[0-9]'
pattern2 = r'\[[0-9]\]\s*[0-9]'


def cleaner(text):
    temp=re.findall(pattern1, text)
    if not temp:
        temp=re.findall(pattern2, text)

    out = [i[-1] for i in temp]
    if len(out) == 10:
        if out[:5] == out[5:]:
            out=out[:5]
    if len(out) != 5:
        return None
    return out
cleanerx=np.vectorize(cleaner)

### Quality

# pattern1 = r'\[[1]\]\s*Score:\s*[0-9]'
pattern = r'\[[1]\]\s*Score:\s*[0-9]\s*\[[2]\]\s*Score:\s*[0-9]\s*\[[3]\]\s*Score:\s*[0-9]\s*\[[4]\]\s*Score:\s*[0-9]\s*\[[5]\]\s*Score:\s*[0-9]'
pattern1 = r'\[[0-9]\]\s*Score:\s*[0-9]'
pattern2 = r'\[[0-9]\]\s*[0-9]'


def cleaner(text):
    temp=re.findall(pattern1, text)
    if not temp:
        temp=re.findall(pattern2, text)

    out = [i[-1] for i in temp]
    if len(out) == 12:
        if out[:6] == out[6:]:
            out=out[:6]
    if len(out) != 6:
        return None
    return out
cleanerx = np.vectorize(cleaner)