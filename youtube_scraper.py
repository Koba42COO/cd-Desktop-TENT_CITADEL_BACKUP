#!/usr/bin/env python3
"""TENT YOUTUBE SCRAPER - Educational video titles from RSS feeds (no API key)."""

import xml.etree.ElementTree as ET
import urllib.request
from upg_store import UniversalPrimeGraph

# Educational YouTube channels (channel IDs)
CHANNELS = {
    "3Blue1Brown": "UCYO_jab_esuFRV4b17AJtAw",
    "Computerphile": "UC9-y-6csu5WGm29I7JiwpnA",
    "Numberphile": "UCoxcjq-8xIDTYp3uz647V5A",
    "TwoMinutePapers": "UCbfYPyITQ-7l4upoX8nvctg",
    "Veritasium": "UCHnyfMqiRRG1u-2MsSQLbXA",
    "SmarterEveryDay": "UC6107grRI4m0o2-emgoDnAA",
    "SteveMould": "UCEIwxahdLz7bap-VDs9h35A",
    "MITOpenCourseWare": "UCEBb1b_L6zDS3xTUrIALZOw",
}

class YouTubeScraper:
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        self.stats = {"fetched": 0, "seeded": 0}
    
    def fetch_channel_feed(self, channel_id: str) -> list:
        """Fetch RSS feed for a channel."""
        url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "TENT/1.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                return self._parse_feed(resp.read().decode())
        except Exception as e:
            print(f"  ❌ Error: {e}")
            return []
    
    def _parse_feed(self, xml_content: str) -> list:
        """Parse Atom feed."""
        videos = []
        ns = {"atom": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015"}
        
        try:
            root = ET.fromstring(xml_content)
            for entry in root.findall("atom:entry", ns):
                title = entry.find("atom:title", ns)
                video_id = entry.find("yt:videoId", ns)
                if title is not None and video_id is not None:
                    videos.append({
                        "title": title.text,
                        "video_id": video_id.text
                    })
        except:
            pass
        return videos
    
    def seed_video(self, video: dict, channel: str) -> bool:
        title = video.get("title", "")
        video_id = video.get("video_id", "")
        if not title:
            return False
        
        node_id = f"YT_{channel.upper().replace(' ', '_')[:15]}_{video_id}"
        
        self.upg.add_node(node_id, {
            "title": title[:200],
            "type": "educational_video",
            "source": "youtube",
            "channel": channel,
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "mass": "SOLID"
        })
        self.stats["seeded"] += 1
        return True
    
    def scrape(self, per_channel: int = 10):
        print("=" * 60)
        print("YOUTUBE EDUCATIONAL SCRAPER")
        print("=" * 60)
        print(f"Channels: {len(CHANNELS)}\n")
        
        for name, channel_id in CHANNELS.items():
            print(f"📺 [{name}]...")
            videos = self.fetch_channel_feed(channel_id)
            self.stats["fetched"] += len(videos)
            
            for video in videos[:per_channel]:
                self.seed_video(video, name)
            print(f"   ✅ {min(len(videos), per_channel)} videos")
        
        self.upg.save_graph()
        print(f"\n✅ Fetched: {self.stats['fetched']}, Seeded: {self.stats['seeded']}")
        return self.stats

if __name__ == "__main__":
    YouTubeScraper().scrape(10)
