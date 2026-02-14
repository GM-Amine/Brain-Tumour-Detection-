"""
Test Script - Brain Tumor Detector
===================================
Script de test pour vérifier que le modèle et l'application fonctionnent correctement
"""

import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import sys

def test_model_loading():
    """Test 1: Vérifier que le modèle peut être chargé"""
    print("\n" + "="*60)
    print("TEST 1: Chargement du modèle")
    print("="*60)
    
    model_path = "best_brain_tumor_model.keras"
    
    if not os.path.exists(model_path):
        print(f"❌ ÉCHEC: Le fichier '{model_path}' n'existe pas")
        return False
    
    try:
        model = load_model(model_path)
        print(f"✅ SUCCÈS: Modèle chargé depuis '{model_path}'")
        print(f"   - Nombre de couches: {len(model.layers)}")
        print(f"   - Input shape: {model.input_shape}")
        print(f"   - Output shape: {model.output_shape}")
        return True, model
    except Exception as e:
        print(f"❌ ÉCHEC: Erreur lors du chargement du modèle")
        print(f"   Erreur: {str(e)}")
        return False, None

def test_image_preprocessing():
    """Test 2: Vérifier le prétraitement des images"""
    print("\n" + "="*60)
    print("TEST 2: Prétraitement d'image")
    print("="*60)
    
    # Créer une image de test (224x224 pixels)
    test_image = np.random.randint(0, 255, (224, 224), dtype=np.uint8)
    
    try:
        # Prétraitement
        img = test_image.astype('float32') / 255.0
        img = img.reshape(1, 224, 224, 1)
        
        print(f"✅ SUCCÈS: Prétraitement réussi")
        print(f"   - Shape originale: {test_image.shape}")
        print(f"   - Shape après prétraitement: {img.shape}")
        print(f"   - Plage de valeurs: [{img.min():.3f}, {img.max():.3f}]")
        return True, img
    except Exception as e:
        print(f"❌ ÉCHEC: Erreur lors du prétraitement")
        print(f"   Erreur: {str(e)}")
        return False, None

def test_model_prediction(model, preprocessed_image):
    """Test 3: Vérifier que le modèle peut faire des prédictions"""
    print("\n" + "="*60)
    print("TEST 3: Prédiction du modèle")
    print("="*60)
    
    try:
        prediction = model.predict(preprocessed_image, verbose=0)
        prob = prediction[0][0]
        
        print(f"✅ SUCCÈS: Prédiction réussie")
        print(f"   - Probabilité brute: {prob:.4f}")
        print(f"   - Probabilité en %: {prob*100:.2f}%")
        print(f"   - Classe prédite: {'Tumeur' if prob > 0.5 else 'Pas de tumeur'}")
        return True
    except Exception as e:
        print(f"❌ ÉCHEC: Erreur lors de la prédiction")
        print(f"   Erreur: {str(e)}")
        return False

def test_dependencies():
    """Test 4: Vérifier que toutes les dépendances sont installées"""
    print("\n" + "="*60)
    print("TEST 4: Vérification des dépendances")
    print("="*60)
    
    dependencies = {
        'tensorflow': 'TensorFlow',
        'cv2': 'OpenCV',
        'PIL': 'Pillow',
        'numpy': 'NumPy',
        'tkinter': 'Tkinter'
    }
    
    all_ok = True
    for module, name in dependencies.items():
        try:
            __import__(module)
            print(f"✅ {name:15} - Installé")
        except ImportError:
            print(f"❌ {name:15} - NON installé (pip install {module if module != 'cv2' else 'opencv-python'})")
            all_ok = False
    
    return all_ok

def test_file_structure():
    """Test 5: Vérifier que tous les fichiers nécessaires sont présents"""
    print("\n" + "="*60)
    print("TEST 5: Structure des fichiers")
    print("="*60)
    
    required_files = {
        'brain_tumor_detector_app.py': 'Script principal',
        'best_brain_tumor_model.keras': 'Modèle entraîné',
        'README.md': 'Documentation (optionnel)',
        'requirements.txt': 'Dépendances (optionnel)'
    }
    
    all_ok = True
    for filename, description in required_files.items():
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            size_str = f"{size/1024:.1f} KB" if size < 1024*1024 else f"{size/(1024*1024):.1f} MB"
            print(f"✅ {filename:35} ({size_str})")
        else:
            if "optionnel" in description:
                print(f"⚠️  {filename:35} (Optionnel - Non présent)")
            else:
                print(f"❌ {filename:35} (REQUIS - Non présent)")
                all_ok = False
    
    return all_ok

def test_model_architecture(model):
    """Test 6: Vérifier l'architecture du modèle"""
    print("\n" + "="*60)
    print("TEST 6: Architecture du modèle")
    print("="*60)
    
    try:
        # Compter les types de couches
        layer_types = {}
        for layer in model.layers:
            layer_type = type(layer).__name__
            layer_types[layer_type] = layer_types.get(layer_type, 0) + 1
        
        print("Types de couches:")
        for layer_type, count in sorted(layer_types.items()):
            print(f"   - {layer_type}: {count}")
        
        total_params = model.count_params()
        print(f"\n📊 Paramètres totaux: {total_params:,}")
        
        # Vérifier que c'est bien un modèle CNN
        has_conv = any('Conv' in type(layer).__name__ for layer in model.layers)
        has_dense = any('Dense' in type(layer).__name__ for layer in model.layers)
        
        if has_conv and has_dense:
            print("✅ Architecture CNN valide (Conv + Dense)")
            return True
        else:
            print("⚠️  Architecture inhabituelle")
            return False
            
    except Exception as e:
        print(f"❌ Erreur lors de l'analyse: {str(e)}")
        return False

def run_all_tests():
    """Exécuter tous les tests"""
    print("\n" + "="*60)
    print("🧪 TESTS DE L'APPLICATION BRAIN TUMOR DETECTOR")
    print("="*60)
    
    results = []
    
    # Test 1: Dépendances
    results.append(("Dépendances", test_dependencies()))
    
    # Test 2: Structure des fichiers
    results.append(("Structure des fichiers", test_file_structure()))
    
    # Test 3: Chargement du modèle
    success, model = test_model_loading()
    results.append(("Chargement du modèle", success))
    
    if not success or model is None:
        print("\n❌ Impossible de continuer les tests (modèle non chargé)")
        print_summary(results)
        return
    
    # Test 4: Architecture
    results.append(("Architecture du modèle", test_model_architecture(model)))
    
    # Test 5: Prétraitement
    success, img = test_image_preprocessing()
    results.append(("Prétraitement d'image", success))
    
    if not success or img is None:
        print("\n❌ Impossible de continuer les tests (prétraitement échoué)")
        print_summary(results)
        return
    
    # Test 6: Prédiction
    results.append(("Prédiction du modèle", test_model_prediction(model, img)))
    
    # Résumé
    print_summary(results)

def print_summary(results):
    """Afficher le résumé des tests"""
    print("\n" + "="*60)
    print("📊 RÉSUMÉ DES TESTS")
    print("="*60)
    
    total = len(results)
    passed = sum(1 for _, result in results if result)
    
    for test_name, result in results:
        status = "✅ PASSÉ" if result else "❌ ÉCHOUÉ"
        print(f"{status:12} - {test_name}")
    
    print("\n" + "-"*60)
    print(f"Résultat global: {passed}/{total} tests réussis ({passed/total*100:.0f}%)")
    print("-"*60)
    
    if passed == total:
        print("\n🎉 TOUS LES TESTS ONT RÉUSSI!")
        print("L'application est prête à être utilisée.")
    else:
        print("\n⚠️  CERTAINS TESTS ONT ÉCHOUÉ")
        print("Veuillez corriger les problèmes avant d'utiliser l'application.")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    try:
        run_all_tests()
    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrompus par l'utilisateur")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Erreur inattendue: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
