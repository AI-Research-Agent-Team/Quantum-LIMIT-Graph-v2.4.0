#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quantum LIMIT-Graph v2.4.0 Structure Validation Script

Validates that all expected files and directories are present
according to the quantum-limit-graph-v2.4.0.txt structure specification.
"""

import os
import sys
from pathlib import Path

def validate_v240_structure():
    """Validate v2.4.0 directory structure"""
    
    base_path = Path(__file__).parent
    
    # Expected structure from quantum-limit-graph-v2.4.0.txt
    expected_structure = {
        'src/evaluation': [
            'quantum_backend_comparison.py',
            'leaderboard_generator.py',
            '__init__.py'
        ],
        'src/agent': [
            'repair_qec_extension.py',
            'backend_selector.py',
            '__init__.py'
        ],
        'src/visualization': [
            'edit_trace_visualizer.py',
            '__init__.py'
        ],
        'configs': [
            'backend_config.yaml'
        ],
        'notebooks': [
            'backend_comparison_demo.ipynb'
        ],
        '.': [
            'demo_v2.4.0.py',
            'README.md',
            'requirements.txt',
            'VISUAL_SUMMARY.md'
        ]
    }
    
    missing_files = []
    found_files = []
    
    print("🔍 Validating Quantum LIMIT-Graph v2.4.0 Structure...")
    print(f"📁 Base Path: {base_path}\n")
    
    for directory, files in expected_structure.items():
        dir_path = base_path / directory if directory != '.' else base_path
        print(f"Checking {directory}/")
        
        for file in files:
            file_path = dir_path / file
            if file_path.exists():
                found_files.append(str(file_path.relative_to(base_path)))
                print(f"  ✅ {file}")
            else:
                missing_files.append(str(file_path.relative_to(base_path)))
                print(f"  ❌ {file} (MISSING)")
    
    print(f"\n{'='*60}")
    print(f"📊 Validation Summary:")
    print(f"  Total Expected: {sum(len(files) for files in expected_structure.values())}")
    print(f"  Found: {len(found_files)}")
    print(f"  Missing: {len(missing_files)}")
    
    if missing_files:
        print(f"\n❌ VALIDATION FAILED")
        print(f"Missing files:")
        for file in missing_files:
            print(f"  - {file}")
        return False
    else:
        print(f"\n✅ VALIDATION PASSED - All v2.4.0 components present!")
        print(f"\n🎯 Structure aligns with:")
        print(f"  - quantum-limit-graph-v2.4.0.txt")
        print(f"  - README.md documentation")
        print(f"  - QUANTUM_LIMIT_GRAPH_V2.4.0_DELIVERY.md")
        return True

if __name__ == "__main__":
    success = validate_v240_structure()
    sys.exit(0 if success else 1)
