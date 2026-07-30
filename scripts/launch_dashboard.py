#!/usr/bin/env python3
"""
Lyra Intel - Launch Enhanced Dashboard
"""

import sys
from pathlib import Path

# Add the repo root to the path so `src` is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.api.enhanced_server import EnhancedAPIServer

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║              🔮 LYRA INTEL DASHBOARD v2.0                   ║
║         Enterprise Code Intelligence Platform               ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

Features:
  ✓ GitHub URL Import & Analysis
  ✓ Real-time Progress Tracking
  ✓ 100+ Intelligence Features
  ✓ Interactive Visualizations
  ✓ Security Scanning
  ✓ Knowledge Graph
  ✓ AI-Powered Insights
  ✓ Performance Profiling
  ✓ And much more...

Starting server...
""")
    
    server = EnhancedAPIServer(host="0.0.0.0", port=8080)
    server.start()
