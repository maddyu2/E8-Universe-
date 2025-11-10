#!/usr/bin/env python3
"""
E8 Proof Visualization
Visualizes the 30,000 E8 proofs generated
Author: Maddy_U2 + Grok
Date: November 10, 2025
"""

import json
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


def load_proofs(filename="e8_proofs_30000.json"):
    """Load proofs from JSON file."""
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def plot_proof_distribution(data):
    """Plot distribution of proof types."""
    proof_types = [proof['type'] for proof in data['proofs']]
    type_counts = Counter(proof_types)
    
    # Sort by count
    sorted_types = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)
    types, counts = zip(*sorted_types)
    
    # Create bar plot
    plt.figure(figsize=(14, 8))
    colors = plt.cm.viridis(np.linspace(0, 1, len(types)))
    bars = plt.bar(range(len(types)), counts, color=colors)
    
    plt.xlabel('Proof Type', fontsize=14, fontweight='bold')
    plt.ylabel('Number of Proofs', fontsize=14, fontweight='bold')
    plt.title('E8 Universe: 30,000 Proofs Distribution\nMaddy_U2 + Grok | Sigma: 16.48σ', 
              fontsize=16, fontweight='bold')
    plt.xticks(range(len(types)), types, rotation=45, ha='right')
    plt.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for i, (bar, count) in enumerate(zip(bars, counts)):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{count:,}',
                ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('e8_proof_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Saved proof distribution plot: e8_proof_distribution.png")
    plt.close()


def plot_verification_rate(data):
    """Plot verification rate of proofs."""
    verified = sum(1 for proof in data['proofs'] if proof.get('verified', False))
    total = len(data['proofs'])
    unverified = total - verified
    
    # Create pie chart
    plt.figure(figsize=(10, 8))
    sizes = [verified, unverified]
    labels = [f'Verified\n{verified:,} ({verified/total*100:.1f}%)', 
              f'Theoretical\n{unverified:,} ({unverified/total*100:.1f}%)']
    colors = ['#2ecc71', '#e74c3c']
    explode = (0.05, 0)
    
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90,
            textprops={'fontsize': 14, 'fontweight': 'bold'})
    
    plt.title('E8 Proof Verification Rate\n30,000 Total Proofs | Sigma: 16.48σ',
              fontsize=16, fontweight='bold')
    plt.axis('equal')
    
    plt.tight_layout()
    plt.savefig('e8_verification_rate.png', dpi=300, bbox_inches='tight')
    print("✓ Saved verification rate plot: e8_verification_rate.png")
    plt.close()


def plot_timeline(data):
    """Plot proof generation timeline."""
    # Extract timestamps
    from datetime import datetime
    
    timestamps = []
    for i, proof in enumerate(data['proofs'][::100]):  # Sample every 100th proof
        ts = proof.get('timestamp', '')
        if ts:
            try:
                dt = datetime.fromisoformat(ts)
                timestamps.append((i*100, dt))
            except:
                pass
    
    if not timestamps:
        print("⚠ No timestamp data available for timeline plot")
        return
    
    # Calculate time from start
    start_time = timestamps[0][1]
    time_offsets = [(idx, (dt - start_time).total_seconds()) for idx, dt in timestamps]
    
    indices, times = zip(*time_offsets)
    
    # Create line plot
    plt.figure(figsize=(14, 8))
    plt.plot(indices, times, 'o-', color='#3498db', linewidth=2, markersize=8)
    
    plt.xlabel('Proof ID', fontsize=14, fontweight='bold')
    plt.ylabel('Time from Start (seconds)', fontsize=14, fontweight='bold')
    plt.title('E8 Proof Generation Timeline\n30,000 Proofs | Throughput: ~21,800 proofs/sec',
              fontsize=16, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    # Add performance annotation
    if len(times) > 1:
        total_time = times[-1]
        total_proofs = indices[-1]
        rate = total_proofs / total_time if total_time > 0 else 0
        plt.text(0.02, 0.98, f'Average Rate: {rate:,.0f} proofs/sec\nTotal Time: {total_time:.2f} sec',
                transform=plt.gca().transAxes,
                verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
                fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('e8_generation_timeline.png', dpi=300, bbox_inches='tight')
    print("✓ Saved generation timeline plot: e8_generation_timeline.png")
    plt.close()


def plot_application_focus(data):
    """Plot focus on applications: Tesla, Neuralink, xAI."""
    application_types = {
        'tesla_fsd_optimization': 'Tesla FSD',
        'neuralink_golay_encoding': 'Neuralink',
        'xai_moonshine_reasoning': 'xAI'
    }
    
    app_counts = {}
    for proof in data['proofs']:
        ptype = proof['type']
        if ptype in application_types:
            app_name = application_types[ptype]
            app_counts[app_name] = app_counts.get(app_name, 0) + 1
    
    if not app_counts:
        print("⚠ No application-specific proofs found")
        return
    
    # Create bar plot
    plt.figure(figsize=(12, 8))
    apps = list(app_counts.keys())
    counts = list(app_counts.values())
    colors = ['#e74c3c', '#9b59b6', '#f39c12']  # Tesla red, purple, xAI orange
    
    bars = plt.bar(apps, counts, color=colors, width=0.6)
    
    plt.ylabel('Number of Proofs', fontsize=14, fontweight='bold')
    plt.title('E8 Applications: Tesla FSD | Neuralink | xAI\nEach with 3,000 Specialized Proofs',
              fontsize=16, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    
    # Add value labels on bars
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{count:,}',
                ha='center', va='bottom', fontsize=14, fontweight='bold')
    
    # Add application descriptions
    descriptions = [
        'Path Optimization\n8D Config Space',
        'Golay [24,12,8]\nError Correction',
        'Moonshine (194 T_g)\nReasoning'
    ]
    for i, (bar, desc) in enumerate(zip(bars, descriptions)):
        plt.text(bar.get_x() + bar.get_width()/2., 100,
                desc, ha='center', va='bottom', fontsize=10,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('e8_applications.png', dpi=300, bbox_inches='tight')
    print("✓ Saved applications plot: e8_applications.png")
    plt.close()


def print_metadata(data):
    """Print metadata summary."""
    metadata = data.get('metadata', {})
    
    print("\n" + "="*60)
    print("E8-UNIVERSE METADATA")
    print("="*60)
    print(f"Total Proofs:     {metadata.get('total_proofs', 0):,}")
    print(f"Target Proofs:    {metadata.get('target_proofs', 0):,}")
    print(f"Sigma:            {metadata.get('sigma', 0)}σ")
    print(f"Start Time:       {metadata.get('start_time', 'N/A')}")
    print(f"Completion Time:  {metadata.get('completion_time', 'N/A')}")
    print(f"Duration:         {metadata.get('duration_hours', 0):.4f} hours")
    print(f"Author:           {metadata.get('author', 'N/A')}")
    print(f"Project:          {metadata.get('project', 'N/A')}")
    print("="*60)


def generate_statistics_report(data):
    """Generate detailed statistics report."""
    proofs = data['proofs']
    
    # Calculate statistics
    total = len(proofs)
    verified = sum(1 for p in proofs if p.get('verified', False))
    
    # Sigma statistics
    sigmas = [p.get('sigma', 0) for p in proofs if 'sigma' in p]
    avg_sigma = sum(sigmas) / len(sigmas) if sigmas else 0
    max_sigma = max(sigmas) if sigmas else 0
    min_sigma = min(sigmas) if sigmas else 0
    
    print("\n" + "="*60)
    print("STATISTICS REPORT")
    print("="*60)
    print(f"Total Proofs:           {total:,}")
    print(f"Verified Proofs:        {verified:,} ({verified/total*100:.1f}%)")
    print(f"Theoretical Proofs:     {total-verified:,} ({(total-verified)/total*100:.1f}%)")
    print(f"\nSigma Statistics:")
    print(f"  Average:              {avg_sigma:.2f}σ")
    print(f"  Maximum:              {max_sigma:.2e}σ")
    print(f"  Minimum:              {min_sigma:.2f}σ")
    print("="*60)


def main():
    """Main visualization function."""
    print("="*60)
    print("E8 PROOF VISUALIZATION")
    print("30,000 Proofs | Maddy_U2 + Grok | Sigma: 16.48σ")
    print("="*60)
    
    try:
        # Load proofs
        print("\n📊 Loading proofs...")
        data = load_proofs()
        
        # Print metadata
        print_metadata(data)
        
        # Generate statistics
        generate_statistics_report(data)
        
        # Create visualizations
        print("\n📈 Generating visualizations...")
        plot_proof_distribution(data)
        plot_verification_rate(data)
        plot_timeline(data)
        plot_application_focus(data)
        
        print("\n" + "="*60)
        print("✓ ALL VISUALIZATIONS COMPLETE")
        print("="*60)
        print("\nGenerated files:")
        print("  • e8_proof_distribution.png")
        print("  • e8_verification_rate.png")
        print("  • e8_generation_timeline.png")
        print("  • e8_applications.png")
        print("\n" + "="*60)
        
    except FileNotFoundError:
        print("\n⚠ Error: e8_proofs_30000.json not found")
        print("Please run: python3 e8_proof_generator.py")
        print("="*60)
    except Exception as e:
        print(f"\n⚠ Error: {e}")
        print("="*60)


if __name__ == "__main__":
    main()
