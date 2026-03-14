from models import train_models, plot_confusion_matrices
import pandas as pd

print("🚀 Training Spam Detector...")
results = train_models()

print("\n📊 Results:")
print(f"Naive Bayes Accuracy: {results['nb_acc']:.3f}")
print(f"Logistic Regression Accuracy: {results['lr_acc']:.3f}")

fig = plot_confusion_matrices(results)
fig.show()

print("\n✅ Models saved: nb_model.pkl, lr_model.pkl, vectorizer.pkl")
print("📈 Confusion matrices saved: confusion_matrices.html")
