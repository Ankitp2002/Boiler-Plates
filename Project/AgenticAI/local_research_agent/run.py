import sys
import os
from datetime import datetime
from agent import research_topic
import markdown

os.makedirs("reports", exist_ok=True)

def generate_report(content, topic):
    """Structured markdown report."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/{topic.replace(' ', '_')}_{timestamp}.md"
    
    report = f"""# 🔍 Research Report: {topic}

## Key Findings
{markdown.markdown(content[:500])}

## Full Analysis
{content}

## Sources
*(Auto-collected by agent via DuckDuckGo/Wikipedia)*
"""
    
    with open(filename, 'w') as f:
        f.write(report)
    print(f"📄 Report saved: {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run.py 'quantum computing'")
        sys.exit(1)
    
    topic = " ".join(sys.argv[1:])
    print(f"🤖 Researching: {topic}")
    
    result = research_topic(topic)
    print("\n📋 Summary:")
    print(result)
    
    generate_report(result, topic)
