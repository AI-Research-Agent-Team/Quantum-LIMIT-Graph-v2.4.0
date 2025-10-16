# -*- coding: utf-8 -*-
"""
Quantum LIMIT-GRAPH v2.4.0 - Complete Demo
Demonstrates backend comparison, QEC integration, and visualization
"""
import sys
import os
import numpy as np

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from evaluation.quantum_backend_comparison import QuantumBackendComparator
from evaluation.leaderboard_generator import LeaderboardGenerator
from agent.repair_qec_extension import REPAIRQECExtension
from agent.backend_selector import BackendSelector
from visualization.edit_trace_visualizer import EditTraceVisualizer


def demo_backend_comparison():
    """Demo 1: Backend Comparison"""
    print("\n" + "=" * 70)
    print("DEMO 1: Backend Comparison (Russian vs IBM)")
    print("=" * 70)
    
    # Initialize comparator
    comparator = QuantumBackendComparator(
        backends=['russian', 'ibm'],
        languages=['en', 'ru', 'es', 'fr', 'de']
    )
    
    # Run quick comparison
    print("\n🔬 Running backend comparison...")
    results = comparator.quick_compare(num_edits=200)
    
    # Display results
    print("\n📊 Comparison Results:")
    for backend, metrics in results.items():
        print(f"\n{backend.upper()}:")
        print(f"  Success Rate: {metrics.edit_success_rate:.1%}")
        print(f"  Hallucination Rate: {metrics.hallucination_rate:.1%}")
        print(f"  Latency: {metrics.avg_latency_ms:.1f}ms")
        print(f"  Fidelity: {metrics.circuit_fidelity:.3f}")
    
    # Generate report
    comparator.generate_report(output='backend_comparison_demo.html')
    
    return results


def demo_leaderboard():
    """Demo 2: Leaderboard Generation"""
    print("\n\n" + "=" * 70)
    print("DEMO 2: Leaderboard Generation")
    print("=" * 70)
    
    # Get backend results
    comparator = QuantumBackendComparator()
    results = comparator.quick_compare(num_edits=150)
    
    # Generate leaderboard
    print("\n🏆 Generating leaderboard...")
    generator = LeaderboardGenerator()
    leaderboard = generator.generate_leaderboard(results)
    
    # Display
    generator.display_leaderboard()
    
    # Export
    generator.export_leaderboard('leaderboard_demo.json')
    
    return leaderboard


def demo_qec_integration():
    """Demo 3: QEC Integration"""
    print("\n\n" + "=" * 70)
    print("DEMO 3: QEC Integration with REPAIR")
    print("=" * 70)
    
    # Initialize QEC
    qec = REPAIRQECExtension(code_type='surface', code_distance=5)
    
    # Create sample edits
    print("\n🔬 Applying QEC to REPAIR edits...")
    edits = [
        {'id': f'edit_{i}', 'code': f'sample_code_{i}', 'lang': 'en'}
        for i in range(50)
    ]
    
    # Apply QEC
    results = qec.batch_apply_qec(edits, backend='russian')
    
    # Display results
    print(f"\n📊 QEC Results:")
    print(f"  Total Edits: {len(results)}")
    print(f"  Syndromes Detected: {sum(len(r.syndromes_detected) for r in results)}")
    print(f"  Corrections Applied: {sum(len(r.corrections_applied) for r in results)}")
    print(f"  Successful Corrections: {sum(1 for r in results if r.correction_success)}")
    
    # Get statistics
    stats = qec.get_statistics()
    print(f"\n📈 QEC Statistics:")
    print(f"  Detection Rate: {stats.get('detection_rate', 0):.1%}")
    print(f"  Correction Rate: {stats.get('correction_rate', 0):.1%}")
    
    return results


def demo_backend_selector():
    """Demo 4: Backend Selection"""
    print("\n\n" + "=" * 70)
    print("DEMO 4: Intelligent Backend Selection")
    print("=" * 70)
    
    # Initialize selector
    selector = BackendSelector(
        backends=['russian', 'ibm'],
        selection_strategy='balanced'
    )
    
    # Create diverse edits
    print("\n🎯 Selecting optimal backends for edits...")
    edits = [
        {'id': 'edit_1', 'lang': 'ru', 'domain': 'scientific'},
        {'id': 'edit_2', 'lang': 'en', 'domain': 'code'},
        {'id': 'edit_3', 'lang': 'es', 'domain': 'text'},
        {'id': 'edit_4', 'lang': 'ru', 'domain': 'math'},
        {'id': 'edit_5', 'lang': 'en', 'domain': 'scientific'},
    ]
    
    # Select backends
    for edit in edits:
        selected = selector.select_backend(edit)
        print(f"  {edit['id']} ({edit['lang']}, {edit['domain']}): {selected.upper()}")
    
    # Get stats
    stats = selector.get_selection_stats()
    print(f"\n📊 Selection Statistics:")
    print(f"  Total Selections: {stats['total_selections']}")
    for backend, ratio in stats['backend_distribution'].items():
        print(f"  {backend.upper()}: {ratio:.1%}")
    
    return selector


def demo_visualization():
    """Demo 5: Visualization"""
    print("\n\n" + "=" * 70)
    print("DEMO 5: Performance Visualization")
    print("=" * 70)
    
    # Create sample edit logs
    print("\n📊 Creating performance visualizations...")
    np.random.seed(42)
    
    edit_logs = []
    backends = ['russian', 'ibm']
    languages = ['en', 'ru', 'es', 'fr', 'de']
    domains = ['code', 'math', 'text']
    
    for i in range(200):
        edit_logs.append({
            'id': f'edit_{i}',
            'backend': np.random.choice(backends),
            'lang': np.random.choice(languages),
            'domain': np.random.choice(domains),
            'success': np.random.rand() > 0.15,
            'latency_ms': np.random.normal(88, 10),
            'type': np.random.choice(['optimization', 'correction', 'translation'])
        })
    
    # Create visualizer
    viz = EditTraceVisualizer()
    
    # Create dashboard
    dashboard = viz.create_dashboard(
        edit_logs,
        backends=backends,
        languages=languages
    )
    
    if dashboard:
        print("✓ Dashboard created (call .show() to display)")
        # dashboard.show()  # Uncomment to display
    else:
        print("⚠️  Visualization requires plotly: pip install plotly")
    
    # Create heatmap
    heatmap = viz.create_heatmap(edit_logs, x_axis='language', y_axis='domain')
    if heatmap:
        print("✓ Heatmap created")
    
    return viz


def main():
    """Run all demos"""
    print("\n" + "🚀" * 35)
    print("Quantum LIMIT-GRAPH v2.4.0 - Complete Demo")
    print("🚀" * 35)
    
    try:
        # Demo 1: Backend Comparison
        backend_results = demo_backend_comparison()
        
        # Demo 2: Leaderboard
        leaderboard = demo_leaderboard()
        
        # Demo 3: QEC Integration
        qec_results = demo_qec_integration()
        
        # Demo 4: Backend Selection
        selector = demo_backend_selector()
        
        # Demo 5: Visualization
        viz = demo_visualization()
        
        # Final Summary
        print("\n\n" + "=" * 70)
        print("🎉 DEMO COMPLETE - Summary")
        print("=" * 70)
        
        print(f"\n✅ Backend Comparison:")
        print(f"   Backends tested: {len(backend_results)}")
        print(f"   Report generated: backend_comparison_demo.html")
        
        print(f"\n✅ Leaderboard:")
        print(f"   Entries: {len(leaderboard)}")
        print(f"   Winner: {leaderboard[0].backend.upper()}")
        
        print(f"\n✅ QEC Integration:")
        print(f"   Edits processed: {len(qec_results)}")
        print(f"   Corrections: {sum(len(r.corrections_applied) for r in qec_results)}")
        
        print(f"\n✅ Backend Selection:")
        stats = selector.get_selection_stats()
        print(f"   Selections made: {stats['total_selections']}")
        
        print(f"\n✅ Visualization:")
        print(f"   Figures created: {len(viz.figures)}")
        
        print(f"\n{'=' * 70}")
        print("📚 Next Steps:")
        print("  1. View report: open backend_comparison_demo.html")
        print("  2. Check leaderboard: cat leaderboard_demo.json")
        print("  3. Run tests: pytest tests/ -v")
        print("  4. Deploy to HF: python scripts/deploy_to_hf.py")
        print("=" * 70 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error during demo: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
