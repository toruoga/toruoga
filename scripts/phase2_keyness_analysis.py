import csv, re, math
from collections import Counter

STOP = set("""a an the this that these those and or but if then else when while of to in on at by for with
from as is are was were be been being have has had do does did will would shall should can could may might
must not no nor so than too very s t just don now i we you he she it they them his her its our their my your
me him us it's i'm we're they're he's she's what which who whom whose all each every both few more most other
some such only own same into out up down over under again further here there all any about above after before
below between into through during without within along across behind beyond plus except but nor not per via
also however therefore thus among upon toward towards amid amidst per se etc one two three  said says say
""".split())

def tokenize(text):
    words = re.findall(r"[A-Za-z']+", text.lower())
    return [w for w in words if w not in STOP and len(w) > 2]

def log_likelihood(a, b, c, d):
    # a = freq of word in target corpus, b = freq of word in reference corpus
    # c = total tokens in target, d = total tokens in reference
    if a == 0:
        return 0.0
    e1 = c * (a + b) / (c + d)
    e2 = d * (a + b) / (c + d)
    ll = 0.0
    if a > 0 and e1 > 0:
        ll += a * math.log(a / e1)
    if b > 0 and e2 > 0:
        ll += b * math.log(b / e2)
    return 2 * ll

with open("/home/user/toruoga/pilot_east_asia_2020_2025.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
with open("/home/user/toruoga/landmark_anchors.csv", encoding="utf-8") as f:
    rows += list(csv.DictReader(f))

texts = {"japan": [], "korea": [], "china": []}
for r in rows:
    texts[r["country"]].append(r["response_text"])

country_tokens = {c: tokenize(" ".join(t)) for c, t in texts.items()}
country_counts = {c: Counter(toks) for c, toks in country_tokens.items()}
country_totals = {c: len(toks) for c, toks in country_tokens.items()}

print("Token totals:", country_totals)
print()

for c in ["japan", "korea", "china"]:
    target_counts = country_counts[c]
    target_total = country_totals[c]
    ref_counts = Counter()
    ref_total = 0
    for c2 in ["japan", "korea", "china"]:
        if c2 != c:
            ref_counts.update(country_counts[c2])
            ref_total += country_totals[c2]
    scored = []
    for w, a in target_counts.items():
        if a < 3:
            continue
        b = ref_counts.get(w, 0)
        ll = log_likelihood(a, b, target_total, ref_total)
        # only overrepresented words (a/target_total > b/ref_total)
        if (a / target_total) > (b / ref_total if ref_total else 0):
            scored.append((ll, w, a, b))
    scored.sort(reverse=True)
    print(f"=== {c.upper()} top keywords (LL keyness vs other two countries) ===")
    for ll, w, a, b in scored[:15]:
        print(f"  {w:15s} LL={ll:7.2f}  freq_in_{c}={a:4d}  freq_in_others={b:4d}")
    print()
