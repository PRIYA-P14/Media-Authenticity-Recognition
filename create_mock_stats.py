import matplotlib.pyplot as plt
import numpy as np
import os

# Create mock training history
epochs = range(1, 21)
train_acc = [0.5 + 0.02*i + np.random.normal(0, 0.01) for i in epochs]
val_acc = [0.48 + 0.018*i + np.random.normal(0, 0.015) for i in epochs]
train_loss = [0.7 - 0.03*i + np.random.normal(0, 0.02) for i in epochs]
val_loss = [0.72 - 0.025*i + np.random.normal(0, 0.025) for i in epochs]

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(epochs, train_acc, label='Training Accuracy', color='blue')
plt.plot(epochs, val_acc, label='Validation Accuracy', color='orange')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.plot(epochs, train_loss, label='Training Loss', color='blue')
plt.plot(epochs, val_loss, label='Validation Loss', color='orange')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
os.makedirs('static', exist_ok=True)
plt.savefig('static/training_history.png', dpi=150, bbox_inches='tight')
plt.close()

print("Mock training statistics created!")