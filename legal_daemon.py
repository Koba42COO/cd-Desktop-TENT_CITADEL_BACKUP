"""
PHASE 289: LEGAL RESEARCH DAEMON (CONTINUOUS BACKGROUND)
=========================================================
A long-running background process that:
1. Seeds initial legal knowledge
2. Actively scrapes public legal sources via headless browser
3. Re-evaluates existing knowledge for gaps
4. Continuously seeks new legal information

Runs indefinitely until stopped. Logs all activity.
"""

import time
import json
import logging
import asyncio
import hashlib
from datetime import datetime, timedelta
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler('legal_daemon.log'),
        logging.StreamHandler()
    ]
)
log = logging.getLogger("LegalDaemon")

# Import UPG
try:
    from upg_store import UniversalPrimeGraph
except ImportError:
    log.warning("UPG not found, running in demo mode")
    UniversalPrimeGraph = None

# Try to import Playwright for headless browser
try:
    from playwright.async_api import async_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    log.warning("Playwright not installed. Install with: pip install playwright && playwright install")


class LegalResearchDaemon:
    """
    Continuous Legal Research Daemon.
    Runs in background, scrapes public sources, expands knowledge.
    """
    
    def __init__(self, cycle_interval_minutes=5):
        self.cycle_interval = cycle_interval_minutes * 60
        self.running = True
        self.cycle_count = 0
        self.nodes_added = 0
        self.last_scrape = {}
        
        # Load UPG
        if UniversalPrimeGraph:
            self.upg = UniversalPrimeGraph()
        else:
            self.upg = None
            
        # Public legal source URLs (no login required)
        self.sources = {
            # US Sources
            "congress_recent": "https://www.congress.gov/search?q=%7B%22source%22%3A%22legislation%22%7D&pageSort=latestAction%3Adesc",
            "congress_laws": "https://www.congress.gov/public-laws",
            "courtlistener_opinions": "https://www.courtlistener.com/opinion/",
            "supremecourt_opinions": "https://www.supremecourt.gov/opinions/opinions.aspx",
            "federal_register": "https://www.federalregister.gov/documents/current",
            
            # UK Sources
            "uk_legislation": "https://www.legislation.gov.uk/new",
            "uk_parliament_bills": "https://bills.parliament.uk/",
            
            # EU Sources
            "eur_lex_recent": "https://eur-lex.europa.eu/homepage.html?locale=en",
            
            # International
            "un_treaties": "https://treaties.un.org/",
            "icj_decisions": "https://www.icj-cij.org/en/decisions",
            
            # Open Legal Data
            "courtlistener_scotus": "https://www.courtlistener.com/opinion/?court=scotus",
            "caselaw_harvard": "https://case.law/",
            "justia_recent": "https://law.justia.com/",
        }
        
        # Legal knowledge categories to track
        self.categories = [
            "constitutional_law", "civil_rights", "criminal_law",
            "corporate_law", "environmental_law", "international_law",
            "intellectual_property", "tax_law", "labor_law",
            "healthcare_law", "immigration_law", "administrative_law"
        ]
        
        # Seed initial curriculum
        self._seed_initial_knowledge()
    
    def _seed_initial_knowledge(self):
        """Seed foundational legal knowledge."""
        if not self.upg:
            return
            
        # Import and run legal curriculum
        try:
            from legal_curriculum import LegalCurriculum
            curriculum = LegalCurriculum()
            count = curriculum.seed_all()
            log.info(f"Seeded {count} foundational legal nodes")
        except Exception as e:
            log.warning(f"Could not seed curriculum: {e}")
    
    async def scrape_page(self, url, source_name):
        """Scrape a page using headless browser."""
        if not PLAYWRIGHT_AVAILABLE:
            log.warning(f"Skipping {source_name}: Playwright not available")
            return None
        
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page()
                
                log.info(f"🌐 Scraping: {source_name}")
                await page.goto(url, timeout=30000)
                await page.wait_for_load_state('networkidle', timeout=15000)
                
                # Extract text content
                content = await page.content()
                title = await page.title()
                
                # Extract links for further exploration
                links = await page.evaluate('''() => {
                    return Array.from(document.querySelectorAll('a[href]'))
                        .map(a => ({href: a.href, text: a.innerText}))
                        .filter(l => l.href.startsWith('http'))
                        .slice(0, 50);
                }''')
                
                await browser.close()
                
                return {
                    "url": url,
                    "title": title,
                    "content_length": len(content),
                    "links": links,
                    "scraped_at": datetime.utcnow().isoformat()
                }
                
        except Exception as e:
            log.error(f"Scrape failed for {source_name}: {e}")
            return None
    
    def extract_legal_entities(self, content):
        """Extract legal entities from scraped content."""
        entities = []
        
        # Simple pattern matching (would use NLP in production)
        patterns = {
            "bill": r"H\.R\.\s*\d+|S\.\s*\d+",
            "public_law": r"P\.L\.\s*\d+-\d+",
            "usc_cite": r"\d+\s*U\.S\.C\.\s*§?\s*\d+",
            "cfr_cite": r"\d+\s*C\.F\.R\.\s*§?\s*[\d\.]+",
            "case_cite": r"\d+\s*(U\.S\.|S\.Ct\.|F\.\d+d?|F\.Supp\.\d*d?)\s*\d+"
        }
        
        import re
        for entity_type, pattern in patterns.items():
            matches = re.findall(pattern, str(content), re.IGNORECASE)
            for match in matches[:10]:  # Limit to prevent overflow
                entities.append({"type": entity_type, "value": match})
        
        return entities
    
    def mint_knowledge(self, source_name, data):
        """Mint new knowledge nodes from scraped data."""
        if not self.upg or not data:
            return 0
        
        minted = 0
        
        # Create node from scraped source
        node_id = f"LEGAL_SCRAPE_{hashlib.md5(data['url'].encode()).hexdigest()[:12]}"
        
        if node_id not in self.upg.nodes:
            self.upg.nodes[node_id] = {
                "title": f"Legal Source: {data['title'][:80]}",
                "abstract": f"Scraped from {source_name}. {data['content_length']} bytes. {len(data.get('links', []))} links found.",
                "type": "legal_source",
                "source": data['url'],
                "category": "scraped_legal",
                "mass": "PENDING_REVIEW",
                "scraped_at": data['scraped_at'],
                "created": datetime.utcnow().isoformat()
            }
            minted += 1
            
        # Extract and mint entities
        entities = self.extract_legal_entities(data.get('content', ''))
        for entity in entities[:5]:  # Limit per source
            entity_id = f"LEGAL_ENTITY_{hashlib.md5(entity['value'].encode()).hexdigest()[:12]}"
            if entity_id not in self.upg.nodes:
                self.upg.nodes[entity_id] = {
                    "title": f"{entity['type'].upper()}: {entity['value']}",
                    "abstract": f"Legal citation extracted from {source_name}",
                    "type": "legal_citation",
                    "source": data['url'],
                    "entity_type": entity['type'],
                    "mass": "PENDING_VERIFICATION",
                    "created": datetime.utcnow().isoformat()
                }
                minted += 1
        
        return minted
    
    def evaluate_knowledge_gaps(self):
        """Analyze existing knowledge and identify gaps."""
        if not self.upg:
            return []
        
        gaps = []
        
        # Count nodes by category
        category_counts = {}
        for node in self.upg.nodes.values():
            cat = node.get('category', 'unknown')
            category_counts[cat] = category_counts.get(cat, 0) + 1
        
        # Identify underrepresented categories
        for cat in self.categories:
            count = category_counts.get(cat, 0)
            if count < 10:
                gaps.append({"category": cat, "current": count, "target": 10})
        
        log.info(f"📊 Knowledge gaps identified: {len(gaps)}")
        return gaps
    
    async def research_cycle(self):
        """Run one cycle of research."""
        self.cycle_count += 1
        log.info(f"\n{'='*60}")
        log.info(f"⚖️  LEGAL RESEARCH CYCLE #{self.cycle_count}")
        log.info(f"{'='*60}")
        
        cycle_minted = 0
        
        # 1. Scrape each source
        for source_name, url in self.sources.items():
            # Check if we scraped recently (rate limiting)
            last = self.last_scrape.get(source_name, datetime.min)
            if datetime.utcnow() - last < timedelta(hours=1):
                log.info(f"⏭️  Skipping {source_name} (scraped recently)")
                continue
            
            data = await self.scrape_page(url, source_name)
            if data:
                minted = self.mint_knowledge(source_name, data)
                cycle_minted += minted
                self.last_scrape[source_name] = datetime.utcnow()
                log.info(f"   ✅ Minted {minted} nodes from {source_name}")
            
            # Be polite - wait between requests
            await asyncio.sleep(2)
        
        # 2. Re-evaluate knowledge
        gaps = self.evaluate_knowledge_gaps()
        
        # 3. Save progress
        if self.upg:
            self.upg.save_graph()
        
        self.nodes_added += cycle_minted
        
        log.info(f"\n📈 CYCLE COMPLETE:")
        log.info(f"   Nodes minted this cycle: {cycle_minted}")
        log.info(f"   Total nodes added: {self.nodes_added}")
        log.info(f"   Total UPG nodes: {len(self.upg.nodes) if self.upg else 'N/A'}")
        log.info(f"   Knowledge gaps: {len(gaps)}")
        log.info(f"   Next cycle in: {self.cycle_interval // 60} minutes")
        
        return cycle_minted
    
    async def run_forever(self):
        """Run the daemon continuously."""
        log.info("=" * 70)
        log.info("⚖️  LEGAL RESEARCH DAEMON STARTING")
        log.info("=" * 70)
        log.info(f"📚 Initial node count: {len(self.upg.nodes) if self.upg else 'N/A'}")
        log.info(f"🌐 Sources configured: {len(self.sources)}")
        log.info(f"⏱️  Cycle interval: {self.cycle_interval // 60} minutes")
        log.info(f"🖥️  Playwright available: {PLAYWRIGHT_AVAILABLE}")
        log.info("=" * 70)
        log.info("Press Ctrl+C to stop\n")
        
        while self.running:
            try:
                await self.research_cycle()
                
                # Wait for next cycle
                for remaining in range(self.cycle_interval, 0, -60):
                    if not self.running:
                        break
                    log.info(f"💤 Next cycle in {remaining // 60} minutes...")
                    await asyncio.sleep(min(60, remaining))
                    
            except KeyboardInterrupt:
                log.info("\n🛑 Shutdown requested")
                self.running = False
            except Exception as e:
                log.error(f"Cycle error: {e}")
                await asyncio.sleep(60)  # Wait before retry
        
        log.info("=" * 70)
        log.info("⚖️  LEGAL RESEARCH DAEMON STOPPED")
        log.info(f"   Cycles completed: {self.cycle_count}")
        log.info(f"   Nodes added: {self.nodes_added}")
        log.info("=" * 70)


def main():
    """Launch the legal research daemon."""
    # Create daemon with 30-minute cycles
    daemon = LegalResearchDaemon(cycle_interval_minutes=30)
    
    # Run forever
    try:
        asyncio.run(daemon.run_forever())
    except KeyboardInterrupt:
        print("\nDaemon stopped by user")


if __name__ == "__main__":
    main()
