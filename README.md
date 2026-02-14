# Brain Tumor Detector - Application Windows Desktop

## 📋 Description

Application Windows avec interface graphique (GUI) pour détecter les tumeurs cérébrales à partir d'images IRM en utilisant un modèle CNN pré-entraîné.

## ✨ Fonctionnalités

- ✅ Interface graphique moderne et intuitive
- 🖼️ Chargement d'images IRM (PNG, JPG, JPEG, BMP, TIFF)
- 🔍 Analyse en temps réel avec le modèle CNN
- 📊 Affichage détaillé des résultats (probabilité, confiance)
- 📝 Historique des analyses dans un fichier log
- ⚠️ Avertissements médicaux appropriés

## 🚀 Installation

### Prérequis

- Windows 10/11
- Python 3.8 ou supérieur
- Le fichier `best_brain_tumor_model.keras` (généré par le notebook)

### Étape 1 : Installer Python

1. Téléchargez Python depuis [python.org](https://www.python.org/downloads/)
2. **IMPORTANT** : Cochez "Add Python to PATH" pendant l'installation
3. Vérifiez l'installation :
   ```bash
   python --version
   ```

### Étape 2 : Installer les dépendances

Ouvrez **Command Prompt** (cmd) ou **PowerShell** et exécutez :

```bash
pip install tensorflow opencv-python pillow numpy
```

**Note** : L'installation de TensorFlow peut prendre quelques minutes.

### Étape 3 : Préparer les fichiers

Organisez vos fichiers dans un dossier comme suit :

```
BrainTumorDetector/
├── brain_tumor_detector_app.py
├── best_brain_tumor_model.keras
└── README.md (ce fichier)
```

## 🎯 Utilisation

### Méthode 1 : Exécution directe

1. Ouvrez **Command Prompt** dans le dossier de l'application
2. Exécutez :
   ```bash
   python brain_tumor_detector_app.py
   ```

### Méthode 2 : Double-clic (recommandé)

1. Renommez `brain_tumor_detector_app.py` en `brain_tumor_detector_app.pyw` (optionnel, cache la console)
2. Double-cliquez sur le fichier pour lancer l'application

### Méthode 3 : Créer un raccourci

**Windows :**
1. Clic droit sur `brain_tumor_detector_app.py`
2. "Envoyer vers" → "Bureau (créer un raccourci)"
3. Renommez le raccourci en "Brain Tumor Detector"
4. Clic droit sur le raccourci → "Propriétés"
5. Dans "Cible", ajoutez `pythonw` devant le chemin :
   ```
   pythonw "C:\chemin\vers\brain_tumor_detector_app.py"
   ```

## 📖 Guide d'utilisation de l'application

### Interface principale

```
┌─────────────────────────────────────────────────┐
│     🧠 Brain Tumor Detector                     │
│  Détection de tumeurs cérébrales par IA         │
├─────────────────────────────────────────────────┤
│                                                 │
│           [Zone d'affichage de l'image]         │
│                                                 │
├─────────────────────────────────────────────────┤
│  [📁 Charger une IRM]  [🔍 Analyser]           │
├─────────────────────────────────────────────────┤
│              Résultats de l'analyse             │
│                                                 │
│  • Probabilité de tumeur: XX.XX%                │
│  • Niveau de confiance: XX.XX%                  │
│  • Recommandations médicales                    │
└─────────────────────────────────────────────────┘
```

### Étapes d'analyse

1. **Charger une image** :
   - Cliquez sur "📁 Charger une IRM"
   - Sélectionnez une image d'IRM cérébrale
   - L'image s'affiche dans la fenêtre

2. **Analyser l'image** :
   - Cliquez sur "🔍 Analyser"
   - Attendez quelques secondes
   - Les résultats s'affichent automatiquement

3. **Interpréter les résultats** :
   - ✅ **Pas de tumeur détectée** (texte vert)
   - ⚠️ **Tumeur détectée** (texte rouge)
   - Consultez la probabilité et la confiance

## 📊 Interprétation des résultats

### Résultats typiques

| Résultat | Probabilité de tumeur | Signification |
|----------|----------------------|---------------|
| ✅ Pas de tumeur | 0-50% | IRM normal |
| ⚠️ Tumeur détectée | 51-100% | Anomalie détectée |

### Niveaux de confiance

- **90-100%** : Très haute confiance
- **80-90%** : Haute confiance
- **70-80%** : Confiance modérée
- **<70%** : Faible confiance (nécessite vérification)

## ⚠️ AVERTISSEMENTS IMPORTANTS

### ⚕️ Usage médical

**CETTE APPLICATION EST À DES FINS ÉDUCATIVES ET DE RECHERCHE UNIQUEMENT**

- ❌ Ne remplace PAS un diagnostic médical professionnel
- ❌ Ne doit PAS être utilisée pour des décisions médicales
- ✅ Consultez TOUJOURS un médecin spécialiste
- ✅ Utilisez uniquement pour la recherche et l'apprentissage

### 🔒 Confidentialité

- Les images ne sont PAS envoyées sur Internet
- Tout le traitement est LOCAL sur votre ordinateur
- Les analyses sont enregistrées dans `analysis_log.txt` (fichier local)

## 🐛 Résolution des problèmes

### Erreur : "Le fichier modèle n'a pas été trouvé"

**Solution** : Assurez-vous que `best_brain_tumor_model.keras` est dans le même dossier que `brain_tumor_detector_app.py`

### Erreur : "No module named 'tensorflow'"

**Solution** : Installez TensorFlow :
```bash
pip install tensorflow
```

### Erreur : "No module named 'cv2'"

**Solution** : Installez OpenCV :
```bash
pip install opencv-python
```

### L'application ne se lance pas

**Solutions** :
1. Vérifiez que Python est installé : `python --version`
2. Réinstallez les dépendances : `pip install --upgrade tensorflow opencv-python pillow`
3. Lancez depuis la ligne de commande pour voir les erreurs :
   ```bash
   python brain_tumor_detector_app.py
   ```

### L'image ne s'affiche pas

**Solutions** :
1. Vérifiez le format de l'image (PNG, JPG supportés)
2. Assurez-vous que l'image n'est pas corrompue
3. Essayez de réduire la taille de l'image (<5 MB)

### Prédictions inexactes

**Causes possibles** :
- Image de mauvaise qualité
- Image non-IRM (radiographie, scanner, etc.)
- IRM d'une autre partie du corps
- Format de fichier non supporté

## 📦 Création d'un exécutable (.exe)

Pour distribuer l'application sans installer Python :

### Utiliser PyInstaller

1. Installez PyInstaller :
   ```bash
   pip install pyinstaller
   ```

2. Créez l'exécutable :
   ```bash
   pyinstaller --onefile --windowed --name="BrainTumorDetector" brain_tumor_detector_app.py
   ```

3. L'exécutable sera dans le dossier `dist/`

4. **IMPORTANT** : Copiez `best_brain_tumor_model.keras` dans le même dossier que l'exécutable

### Distribution

Créez un dossier avec :
```
BrainTumorDetector_v1.0/
├── BrainTumorDetector.exe
├── best_brain_tumor_model.keras
└── README.txt
```

## 🔧 Personnalisation

### Modifier les couleurs

Dans `brain_tumor_detector_app.py`, section `__init__` :

```python
self.bg_color = "#f0f4f8"        # Couleur de fond
self.primary_color = "#2563eb"   # Couleur principale
self.success_color = "#10b981"   # Couleur succès
self.danger_color = "#ef4444"    # Couleur danger
```

### Modifier le seuil de détection

Par défaut, le seuil est 0.5 (50%). Pour le modifier :

```python
# Dans la méthode analyze_image()
has_tumor = prediction > 0.5  # Changez 0.5 à votre seuil
```

### Ajouter des fonctionnalités

Vous pouvez ajouter :
- Export des résultats en PDF
- Comparaison de plusieurs IRM
- Historique visuel des analyses
- Statistiques des analyses

## 📝 Fichier de log

L'application crée automatiquement `analysis_log.txt` avec :

```
============================================================
Date: 2026-02-12 14:30:45
Image: brain_scan_001.jpg
Résultat: TUMEUR DÉTECTÉE
Probabilité: 87.34%
Confiance: 87.34%
============================================================
```

## 🆘 Support et contact

Pour toute question ou problème :
- Vérifiez d'abord la section "Résolution des problèmes"
- Consultez le notebook Jupyter pour plus de détails sur le modèle
- Vérifiez que votre modèle a une accuracy >92%

## 📄 Licence

Ce projet est à des fins éducatives uniquement.

## 🙏 Remerciements

- TensorFlow / Keras pour le framework de deep learning
- OpenCV pour le traitement d'images
- La communauté Python pour les bibliothèques

---

**Version** : 1.0  
**Date** : Février 2026  
**Auteur** : Votre Nom
