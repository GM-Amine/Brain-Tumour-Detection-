# 🚀 QUICK START GUIDE - Brain Tumor Detector

## Installation rapide (5 minutes)

### 1️⃣ Installer Python (si pas déjà fait)
- Téléchargez: https://www.python.org/downloads/
- ⚠️ IMPORTANT: Cochez "Add Python to PATH"
- Installez normalement

### 2️⃣ Installer les dépendances
Ouvrez **Command Prompt** et exécutez:
```bash
pip install -r requirements.txt
```
OU installez manuellement:
```bash
pip install tensorflow opencv-python pillow numpy
```

### 3️⃣ Vérifier les fichiers nécessaires
Assurez-vous d'avoir ces fichiers dans le même dossier:
```
✅ brain_tumor_detector_app.py
✅ best_brain_tumor_model.keras
✅ launch_app.bat (optionnel)
```

### 4️⃣ Lancer l'application

**Option A - Double-clic sur le fichier batch:**
```
Double-clic sur: launch_app.bat
```

**Option B - Ligne de commande:**
```bash
python brain_tumor_detector_app.py
```

**Option C - Mode silencieux (sans console):**
```bash
pythonw brain_tumor_detector_app.py
```

---

## 📱 Utilisation de l'application

### Étape 1: Charger une IRM
1. Cliquez sur **"📁 Charger une IRM"**
2. Sélectionnez votre image (.jpg, .png, etc.)
3. L'image apparaît à l'écran

### Étape 2: Analyser
1. Cliquez sur **"🔍 Analyser"**
2. Attendez 2-3 secondes
3. Les résultats s'affichent

### Étape 3: Interpréter les résultats

**✅ Résultat VERT = Pas de tumeur**
```
✅ PAS DE TUMEUR DÉTECTÉE
Probabilité de tumeur: 15.34%
Niveau de confiance: 84.66%
```

**⚠️ Résultat ROUGE = Tumeur détectée**
```
⚠️ TUMEUR DÉTECTÉE
Probabilité de tumeur: 89.72%
Niveau de confiance: 89.72%
```

---

## ❓ Problèmes fréquents

### ❌ "Python n'est pas reconnu..."
**Solution:** Réinstallez Python en cochant "Add Python to PATH"

### ❌ "ModuleNotFoundError: No module named 'tensorflow'"
**Solution:** 
```bash
pip install tensorflow
```

### ❌ "Le fichier modèle n'a pas été trouvé"
**Solution:** Copiez `best_brain_tumor_model.keras` dans le même dossier

### ❌ L'application ne se lance pas
**Solution:** Lancez depuis cmd pour voir l'erreur:
```bash
python brain_tumor_detector_app.py
```

---

## 🎨 Personnalisation rapide

### Changer le titre de la fenêtre
Dans `brain_tumor_detector_app.py`, ligne ~25:
```python
self.root.title("Votre Titre Ici")
```

### Changer la taille de la fenêtre
Dans `brain_tumor_detector_app.py`, ligne ~26:
```python
self.root.geometry("1000x800")  # largeur x hauteur
```

### Modifier le seuil de détection (par défaut 50%)
Dans la fonction `analyze_image()`:
```python
has_tumor = prediction > 0.5  # Changez 0.5 (50%) à votre valeur
```

---

## 📊 Formats d'images supportés

✅ PNG (.png)  
✅ JPEG (.jpg, .jpeg)  
✅ BMP (.bmp)  
✅ TIFF (.tiff, .tif)

---

## 🔒 Sécurité et confidentialité

✅ Traitement 100% LOCAL (pas d'Internet requis)  
✅ Aucune image envoyée en ligne  
✅ Logs stockés localement dans `analysis_log.txt`  
✅ Vous contrôlez toutes vos données  

---

## ⚕️ AVERTISSEMENT MÉDICAL

⚠️ **CETTE APPLICATION EST À DES FINS ÉDUCATIVES UNIQUEMENT**

- Ne remplace PAS un diagnostic médical
- Consultez TOUJOURS un médecin professionnel
- Ne prenez PAS de décisions médicales basées uniquement sur cette app
- Utilisez uniquement pour l'apprentissage et la recherche

---

## 🆘 Besoin d'aide?

1. Lisez le **README.md** complet
2. Vérifiez la section "Résolution des problèmes"
3. Consultez le notebook Jupyter pour comprendre le modèle
4. Vérifiez que votre modèle a une accuracy >92%

---

## 📦 Créer un exécutable Windows (.exe)

Pour distribuer l'app sans installer Python:

```bash
# 1. Installer PyInstaller
pip install pyinstaller

# 2. Créer l'exécutable
pyinstaller --onefile --windowed --name="BrainTumorDetector" brain_tumor_detector_app.py

# 3. Copiez le modèle dans dist/
copy best_brain_tumor_model.keras dist/

# 4. Votre .exe est dans dist/BrainTumorDetector.exe
```

---

## 🎯 Checklist avant de distribuer

- [ ] Python installé (version 3.8+)
- [ ] Dépendances installées (`pip install -r requirements.txt`)
- [ ] Fichier `best_brain_tumor_model.keras` présent
- [ ] Application se lance sans erreur
- [ ] Test avec plusieurs images IRM
- [ ] Résultats cohérents (>90% accuracy)

---

**Version:** 1.0  
**Dernière mise à jour:** Février 2026  
**Testé sur:** Windows 10, Windows 11
