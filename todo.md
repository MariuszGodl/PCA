# TODO – PCA Presentation Project

## 1. Project Structure
- [ ] Create project repository
- [ ] Add folders:
  - /data
  - /notebooks
  - /src
  - /images
  - /presentation
- [ ] Add README.md
- [ ] Add requirements.txt (numpy, pandas, matplotlib, seaborn, scikit-learn)

---

## 2. Theoretical Section (Slides Content)

### 2.1 Introduction to PCA
- [ ] Define Principal Component Analysis (PCA)
- [ ] Explain why dimensionality reduction is needed
- [ ] Explain when PCA should be used
- [ ] Add intuitive explanation (variance maximization)

### 2.2 Mathematical Foundations
- [ ] Explain mean centering
- [ ] Derive covariance matrix
- [ ] Explain eigenvectors and eigenvalues
- [ ] Show proof that PCA maximizes variance
- [ ] Add geometric interpretation
- [ ] Add legend of symbols

### 2.3 Covariance Matrix Section
- [ ] Define covariance
- [ ] Show covariance matrix formula
- [ ] Explain why eigenvectors of covariance matrix matter

---

## 3. Visualization Section

### 3.1 2D Visualization
- [ ] Generate synthetic 2D correlated dataset
- [ ] Plot original axes
- [ ] Plot PCA principal component line
- [ ] Show projection onto PC1

### 3.2 3D Visualization
- [ ] Generate synthetic 3D dataset
- [ ] Plot original 3D axes
- [ ] Show PCA plane (first 2 PCs)
- [ ] Show projection onto lower dimension

### 3.3 Variance Explained Plot
- [ ] Scree plot
- [ ] Cumulative explained variance plot

---

## 4. Code Pipeline

### 4.1 Basic PCA Pipeline
- [ ] Load dataset
- [ ] Standardize data
- [ ] Exclude binary data
- [ ] Fit PCA
- [ ] Transform data
- [ ] Plot explained variance

### 4.2 Full ML Pipeline with PCA
- [ ] Build pipeline using:
  - StandardScaler
  - PCA
  - LogisticRegression
- [ ] Cross-validation
- [ ] Compare with model without PCA

---

## 5. Case Study: PCA Improving Model Accuracy

- [ ] Generate noisy dataset with redundant features
- [ ] Train baseline classifier
- [ ] Train classifier with PCA
- [ ] Compare accuracy
- [ ] Explain why PCA improved performance (noise reduction)

---

## 6. Explainability Section

- [ ] Explain why PCA reduces interpretability
- [ ] Show original feature importance
- [ ] Show PCA component loadings
- [ ] Discuss trade-offs

---

## 7. Final Presentation

- [ ] Prepare slides:
  - Motivation
  - Theory
  - Math
  - Visualization
  - Code
  - Case Study
  - Limitations
- [ ] Add speaker notes
- [ ] Add diagrams
- [ ] Rehearse presentation
