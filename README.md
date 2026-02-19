# 🧠 Segmentation Automatique d’Images Histologiques de Biopsies Rénales

## 📚 Projet de Fin d’Études – ILIA 5e année  
**Achour Othmane**  
Laboratoire LEAD – Université de Bourgogne  
Année universitaire 2025–2026  

---

## 🎯 Objectif du Projet

Ce projet vise à développer une solution d’intelligence artificielle pour la segmentation automatique de structures histologiques dans des biopsies rénales.

Nous réalisons une étude comparative entre :

- 🔵 Une approche classique CNN spécialisée : **Attention R2U-Net**
- 🟣 Un modèle de fondation promptable : **LiteMedSAM**

---

## 🏥 Contexte Médical

L’analyse histologique des biopsies rénales est :

- Chronophage  
- Sujette à variabilité inter-observateur  
- Complexe (12 classes sémantiques)

Ce projet propose un outil d’assistance IA pour :

- Automatiser la segmentation
- Améliorer la reproductibilité
- Réduire le temps d’analyse

---

## 🧩 Classes Segmentées

Le dataset contient 12 classes, incluant :

- Glomérules
- Tubules proximaux / distaux
- Tubules atrophiques
- Cortex
- Fibrose
- Structures vasculaires (veines, média, intima)
- Artefacts

---

## ⚙️ Structure du Projet

.
├── AttR2UNet/
│ ├── data_preparation/
│ ├── training/
│ └── README.md
│
├── LiteMedSAM/
│ ├── data_pipeline/
│ ├── training/
│ └── README.md
│
├── dataset/
├── experiments/
└── README.md


---

## 🔬 Approches Comparées

| Critère | AttR2U-Net | LiteMedSAM |
|----------|------------|------------|
| Type | CNN Spécialiste | Modèle de Fondation |
| Entraînement | From scratch | Transfer Learning |
| Entrée | Image seule | Image + Prompt (Bounding Box) |
| Multi-classes | 12 modèles (One-vs-All) | Modèle unique |
| Interactivité | ❌ | ✅ |

---

## 🗂️ Données

- Format source : COCO JSON
- Images haute résolution
- Annotations expertes (CHU Dijon)
- Conversion en :
  - Masques binaires (AttR2U-Net)
  - Paires Image + Bounding Box (LiteMedSAM)

---

## 📈 Résultats

### LiteMedSAM
- Convergence rapide
- Dice Loss + Cross Entropy
- Bonne segmentation qualitative
- Approche interactive prometteuse

### AttR2U-Net
- Entraînement lancé avec succès
- Problèmes de validation métrique
- Comparatif quantitatif à finaliser

---

## 🚀 Perspectives

- Finalisation du comparatif quantitatif
- Génération automatique de prompts
- Intégration dans interface graphique
- Déploiement clinique potentiel

---

## 👨‍🔬 Encadrement

- M. Nasser Dandana – Doctorant IA  
- M. Patrick Bard – Encadrant  
- Collaboration avec le CHU de Dijon  

---

## 📝 Licence

Projet académique – Usage recherche uniquement.
