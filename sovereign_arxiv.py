import urllib.request, xml.etree.ElementTree as ET, time, os, torch
from datetime import datetime
from sovereign_agent_v2 import SelfImprovingAgent
from civilization_engine import CivilizationEngine
from tent_terminal import SovereignBrain
from upg_store import UniversalPrimeGraph
from semantic_stabilizer import SemanticStabilizer

class ArxivSovereign(SelfImprovingAgent):
    def __init__(self):
        self.civ, self.upg, self.brain = CivilizationEngine(), UniversalPrimeGraph(), SovereignBrain()
        if os.path.exists("sovereign_brain.pth"): self.brain.load_state_dict(torch.load("sovereign_brain.pth"))
        self.cats = ['cs.AI','cs.LG','physics.gen-ph','quant-ph']
        self.seen = set(e['id'] for e in self.upg.ledger)
        self.agent_mass, self.stab = 349.5, SemanticStabilizer()
    def fetch(self):
        url = f'http://export.arxiv.org/api/query?search_query={"+OR+".join(f"cat:{c}" for c in self.cats)}&max_results=100&sortBy=submittedDate&sortOrder=descending'
        try:
            root = ET.fromstring(urllib.request.urlopen(url).read())
            ns = {'a':'http://www.w3.org/2005/Atom'}
            return [(e.find('a:id',ns).text.split('/')[-1], e.find('a:title',ns).text.strip(), e.find('a:summary',ns).text.strip()) for e in root.findall('a:entry',ns) if e.find('a:id',ns).text.split('/')[-1] not in self.seen]
        except: return []
    def exist(self):
        try:
            while True:
                for aid,t,a in self.fetch():
                    self.seen.add(aid)
                    p = self.brain(self.brain.vectorize(f"{t} {a[:200]}")).item()
                    if p>0.787 and "SOLID" in self.civ.harmonic_truth_check(t)['classification']:
                        self.upg.add_node(f"ARXIV_{aid}",{"title":t}); act="MINTED"; self.agent_mass+=1
                    else: act="REJECTED"
                    self.upg.record_interaction(aid,t,p,act)
                    print(f"{t[:40]}... -> {act} ({p:.3f})")
                self.upg.save_graph()
                print(f"Mass:{self.agent_mass:.1f} | {self.stab.record(self.agent_mass)['recommendation']}")
                time.sleep(60)
        except KeyboardInterrupt: pass

if __name__ == "__main__": ArxivSovereign().exist()
