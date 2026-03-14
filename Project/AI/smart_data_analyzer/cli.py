import sys
import click
from analyzer import DataAnalyzer
import pandas as pd

@click.command()
@click.argument('csv_file', type=click.Path(exists=True))
def analyze(csv_file):
    df = pd.read_csv(csv_file)
    analyzer = DataAnalyzer(df)
    
    print("📊 Data Shape:", df.shape)
    print("\n🔍 Detected Types:")
    for col, dtype in analyzer.dtypes_detected.items():
        print(f"  {col}: {dtype}")
    
    print("\n📈 Numeric Summary:")
    print(analyzer.stats_summary().get('numeric', 'No numeric columns'))
    
    print("\n🚨 Anomalies:")
    anomalies = analyzer.detect_anomalies()
    for col, indices in anomalies.items():
        print(f"  {col}: rows {indices}")
    
    print("\n✅ Analysis complete!")

if __name__ == "__main__":
    analyze()
