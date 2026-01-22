#!/usr/bin/env python3
"""TENT LOCAL FILE INDEXER - Index your own codebase into UPG."""

import os
import re
from pathlib import Path
from upg_store import UniversalPrimeGraph

# Directories to scan
SCAN_DIRS = [
    "/Volumes/WD Drive/Backup dev folder/dev/prime-sparse-saas",
]

# File extensions to index
EXTENSIONS = {".py", ".md", ".txt", ".json", ".yaml", ".yml"}

class LocalFileIndexer:
    def __init__(self):
        self.upg = UniversalPrimeGraph()
        self.stats = {"scanned": 0, "indexed": 0}
    
    def extract_docstring(self, content: str) -> str:
        """Extract first docstring from Python file."""
        match = re.search(r'"""(.+?)"""', content, re.DOTALL)
        if match:
            return match.group(1).strip()[:300]
        match = re.search(r"'''(.+?)'''", content, re.DOTALL)
        if match:
            return match.group(1).strip()[:300]
        return ""
    
    def extract_md_header(self, content: str) -> str:
        """Extract first markdown header and following content."""
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('# '):
                # Get header and next few lines
                snippet = '\n'.join(lines[i:i+5])
                return snippet[:300]
        return content[:200]
    
    def index_file(self, filepath: Path) -> bool:
        """Index a single file."""
        try:
            content = filepath.read_text(errors='ignore')[:5000]
        except:
            return False
        
        # Extract summary based on file type
        if filepath.suffix == '.py':
            summary = self.extract_docstring(content) or filepath.name
        elif filepath.suffix == '.md':
            summary = self.extract_md_header(content)
        else:
            summary = content[:200]
        
        # Create node
        rel_path = str(filepath).replace("/Volumes/WD Drive/Backup dev folder/dev/", "")
        node_id = f"LOCAL_{rel_path.upper().replace('/', '_').replace('.', '_')[:50]}"
        
        self.upg.add_node(node_id, {
            "title": filepath.name,
            "type": "local_file",
            "source": "local",
            "path": str(filepath),
            "abstract": summary,
            "extension": filepath.suffix,
            "mass": "SOLID"
        })
        self.stats["indexed"] += 1
        return True
    
    def scan_directory(self, dir_path: str):
        """Scan a directory for files."""
        path = Path(dir_path)
        if not path.exists():
            print(f"  ❌ Directory not found: {dir_path}")
            return
        
        for filepath in path.rglob("*"):
            if filepath.is_file() and filepath.suffix in EXTENSIONS:
                # Skip hidden and cache dirs
                if any(p.startswith('.') for p in filepath.parts):
                    continue
                if '__pycache__' in str(filepath):
                    continue
                
                self.stats["scanned"] += 1
                if self.index_file(filepath):
                    if self.stats["indexed"] % 20 == 0:
                        print(f"   Indexed {self.stats['indexed']} files...")
    
    def index(self):
        print("=" * 60)
        print("LOCAL FILE INDEXER")
        print("=" * 60)
        print(f"Directories: {len(SCAN_DIRS)}\n")
        
        for dir_path in SCAN_DIRS:
            print(f"📁 Scanning: {dir_path}")
            self.scan_directory(dir_path)
        
        self.upg.save_graph()
        print(f"\n✅ Scanned: {self.stats['scanned']}, Indexed: {self.stats['indexed']}")
        return self.stats

if __name__ == "__main__":
    LocalFileIndexer().index()
