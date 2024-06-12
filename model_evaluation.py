from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Mengevaluasi model pada data tes
y_pred = model.predict(X_test)
y_pred = np.argmax(y_pred, axis=1)

# Menghitung akurasi
accuracy = (y_pred == y_test).mean()
print(f'Akurasi: {accuracy:.4f}')

# Menghitung classification report
report = classification_report(y_test, y_pred, target_names=class_names)
print(report)

# Menghitung confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Memvisualisasikan confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, cmap='Blues', xticklabels=class_names, yticklabels=class_names)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()