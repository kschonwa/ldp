from ldp.gesture import LRB, GestureSpeechRelation
from ldp.data import Utterances, Subjects
from util.count import FeatureCounter

lrb = LRB()
gsrel = GestureSpeechRelation()
subjects = Subjects()
utterances = Utterances()
count = FeatureCounter('Subject', 'Session', 'Project', 'Gesture')

P2 = set(subjects.project(2))

columns = 'subject, session, c_lrb, c_gs_rel'
filter  = 'session in (5, 8) and c_lrb != ""'

def pprint(args): print "\t".join(args)

for subj, sess, h, g in utterances(columns, filter, limit=''): 
    proj = 2 if subj in P2 else 3
    H = lrb.valid_values(h.upper())
    G = gsrel.valid_values(g, subcodes=False)
    for (h, g) in zip(H, G):
        code = "{0}+{1}".format(h, g)
        count(subj, sess, proj, code) 

count.print_report('Gesture')
