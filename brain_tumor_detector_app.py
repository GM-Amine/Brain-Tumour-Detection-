"""
Brain Tumor Detection - Windows Desktop Application
====================================================
Application GUI pour détecter les tumeurs cérébrales à partir d'IRM
Utilise le modèle CNN entraîné (best_brain_tumor_model.keras)

Auteur: Votre Nom
Date: 2026
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os
from datetime import datetime

class BrainTumorDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Brain Tumor Detector - Détection de Tumeurs Cérébrales")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        
        # Configuration des couleurs
        self.bg_color = "#f0f4f8"
        self.primary_color = "#2563eb"
        self.success_color = "#10b981"
        self.danger_color = "#ef4444"
        self.text_color = "#1f2937"
        
        self.root.configure(bg=self.bg_color)
        
        # Variables
        self.model = None
        self.current_image_path = None
        self.current_image = None
        self.img_size = 224
        
        # Charger le modèle
        self.load_model()
        
        # Créer l'interface
        self.create_widgets()
        
    def load_model(self):
        """Charge le modèle CNN pré-entraîné"""
        model_path = "best_brain_tumor_model.keras"
        
        try:
            if os.path.exists(model_path):
                self.model = load_model(model_path)
                print(f"✓ Modèle chargé avec succès depuis {model_path}")
            else:
                messagebox.showerror(
                    "Erreur", 
                    f"Le fichier modèle '{model_path}' n'a pas été trouvé.\n\n"
                    "Veuillez vous assurer que le fichier 'best_brain_tumor_model.keras' "
                    "est dans le même dossier que cette application."
                )
                self.root.destroy()
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du chargement du modèle:\n{str(e)}")
            self.root.destroy()
    
    def create_widgets(self):
        """Crée tous les widgets de l'interface"""
        
        # Header
        header_frame = tk.Frame(self.root, bg=self.primary_color, height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="🧠 Brain Tumor Detector",
            font=("Segoe UI", 24, "bold"),
            bg=self.primary_color,
            fg="white"
        )
        title_label.pack(pady=20)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Détection de tumeurs cérébrales par Intelligence Artificielle",
            font=("Segoe UI", 10),
            bg=self.primary_color,
            fg="#e0e7ff"
        )
        subtitle_label.pack()
        
        # Main content frame
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        # Image display frame
        image_frame = tk.LabelFrame(
            main_frame,
            text="Image IRM",
            font=("Segoe UI", 12, "bold"),
            bg="white",
            fg=self.text_color,
            relief=tk.RIDGE,
            borderwidth=2
        )
        image_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        self.image_label = tk.Label(
            image_frame,
            text="Aucune image chargée\n\nCliquez sur 'Charger une IRM' pour commencer",
            font=("Segoe UI", 12),
            bg="white",
            fg="#6b7280",
            width=50,
            height=15
        )
        self.image_label.pack(padx=20, pady=20)
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg=self.bg_color)
        buttons_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Load button
        self.load_btn = tk.Button(
            buttons_frame,
            text="📁 Charger une IRM",
            command=self.load_image,
            font=("Segoe UI", 12, "bold"),
            bg=self.primary_color,
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            cursor="hand2",
            relief=tk.FLAT,
            padx=30,
            pady=12
        )
        self.load_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        
        # Analyze button
        self.analyze_btn = tk.Button(
            buttons_frame,
            text="🔍 Analyser",
            command=self.analyze_image,
            font=("Segoe UI", 12, "bold"),
            bg=self.success_color,
            fg="white",
            activebackground="#059669",
            activeforeground="white",
            cursor="hand2",
            relief=tk.FLAT,
            padx=30,
            pady=12,
            state=tk.DISABLED
        )
        self.analyze_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(10, 0))
        
        # Results frame
        self.results_frame = tk.LabelFrame(
            main_frame,
            text="Résultats de l'analyse",
            font=("Segoe UI", 12, "bold"),
            bg="white",
            fg=self.text_color,
            relief=tk.RIDGE,
            borderwidth=2
        )
        self.results_frame.pack(fill=tk.BOTH)
        
        self.result_label = tk.Label(
            self.results_frame,
            text="En attente d'analyse...",
            font=("Segoe UI", 11),
            bg="white",
            fg="#6b7280",
            justify=tk.LEFT,
            anchor="w"
        )
        self.result_label.pack(padx=20, pady=20, fill=tk.BOTH)
        
        # Footer
        footer_frame = tk.Frame(self.root, bg=self.bg_color, height=40)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        footer_frame.pack_propagate(False)
        
        footer_label = tk.Label(
            footer_frame,
            text="Powered by TensorFlow & Keras | CNN Model Accuracy: >92%",
            font=("Segoe UI", 8),
            bg=self.bg_color,
            fg="#6b7280"
        )
        footer_label.pack(pady=10)
    
    def load_image(self):
        """Ouvre un dialogue pour charger une image IRM"""
        file_path = filedialog.askopenfilename(
            title="Sélectionner une image IRM",
            filetypes=[
                ("Images", "*.png *.jpg *.jpeg *.bmp *.tiff"),
                ("PNG", "*.png"),
                ("JPEG", "*.jpg *.jpeg"),
                ("Tous les fichiers", "*.*")
            ]
        )
        
        if file_path:
            try:
                # Charger l'image
                self.current_image_path = file_path
                img = Image.open(file_path)
                
                # Redimensionner pour l'affichage (garder le ratio)
                display_size = 400
                img.thumbnail((display_size, display_size), Image.Resampling.LANCZOS)
                
                # Convertir pour Tkinter
                photo = ImageTk.PhotoImage(img)
                
                # Afficher l'image
                self.image_label.configure(image=photo, text="")
                self.image_label.image = photo  # Garder une référence
                
                # Activer le bouton d'analyse
                self.analyze_btn.config(state=tk.NORMAL)
                
                # Réinitialiser les résultats
                self.result_label.config(
                    text="Image chargée avec succès!\nCliquez sur 'Analyser' pour détecter les tumeurs.",
                    fg="#059669"
                )
                
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible de charger l'image:\n{str(e)}")
    
    def preprocess_image(self, image_path):
        """
        Prétraite l'image pour le modèle CNN
        
        Args:
            image_path: chemin vers l'image
            
        Returns:
            image prétraitée au format attendu par le modèle
        """
        # Charger l'image en niveaux de gris
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        # Redimensionner à 224×224
        img = cv2.resize(img, (self.img_size, self.img_size))
        
        # Normaliser les pixels entre 0 et 1
        img = img.astype('float32') / 255.0
        
        # Reshape pour le modèle (1, 224, 224, 1)
        img = img.reshape(1, self.img_size, self.img_size, 1)
        
        return img
    
    def analyze_image(self):
        """Analyse l'image IRM et affiche les résultats"""
        if not self.current_image_path:
            messagebox.showwarning("Attention", "Veuillez d'abord charger une image.")
            return
        
        try:
            # Désactiver le bouton pendant l'analyse
            self.analyze_btn.config(state=tk.DISABLED, text="⏳ Analyse en cours...")
            self.root.update()
            
            # Prétraiter l'image
            preprocessed_img = self.preprocess_image(self.current_image_path)
            
            # Prédiction
            prediction = self.model.predict(preprocessed_img, verbose=0)[0][0]
            
            # Interpréter les résultats
            has_tumor = prediction > 0.5
            confidence = prediction if has_tumor else (1 - prediction)
            
            # Préparer l'affichage des résultats
            result_text = self.format_results(has_tumor, prediction, confidence)
            
            # Afficher les résultats avec couleur appropriée
            result_color = self.danger_color if has_tumor else self.success_color
            self.result_label.config(text=result_text, fg=result_color, font=("Segoe UI", 11, "bold"))
            
            # Sauvegarder le résultat dans un fichier log (optionnel)
            self.log_result(has_tumor, prediction, confidence)
            
            # Réactiver le bouton
            self.analyze_btn.config(state=tk.NORMAL, text="🔍 Analyser")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'analyse:\n{str(e)}")
            self.analyze_btn.config(state=tk.NORMAL, text="🔍 Analyser")
    
    def format_results(self, has_tumor, prediction, confidence):
        """
        Formate les résultats de l'analyse
        
        Args:
            has_tumor: booléen indiquant la présence de tumeur
            prediction: probabilité brute du modèle
            confidence: niveau de confiance (0-1)
            
        Returns:
            texte formaté des résultats
        """
        if has_tumor:
            status = "⚠️ TUMEUR DÉTECTÉE"
            recommendation = (
                "Une tumeur a été détectée sur cette IRM.\n\n"
                "⚕️ RECOMMANDATION:\n"
                "Veuillez consulter un médecin spécialiste immédiatement\n"
                "pour une évaluation complète et un diagnostic professionnel."
            )
        else:
            status = "✅ PAS DE TUMEUR DÉTECTÉE"
            recommendation = (
                "Aucune tumeur n'a été détectée sur cette IRM.\n\n"
                "ℹ️ NOTE:\n"
                "Ce résultat est une prédiction par IA et ne remplace pas\n"
                "un diagnostic médical professionnel."
            )
        
        result_text = f"""
╔════════════════════════════════════════════════════════╗
  {status}
╚════════════════════════════════════════════════════════╝

📊 DÉTAILS DE L'ANALYSE:
   • Probabilité de tumeur: {prediction * 100:.2f}%
   • Niveau de confiance: {confidence * 100:.2f}%
   • Date d'analyse: {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}

{recommendation}

⚠️ AVERTISSEMENT:
Cette application utilise un modèle d'intelligence artificielle à des 
fins éducatives et de recherche uniquement. Les résultats ne doivent 
jamais remplacer l'avis d'un professionnel de santé qualifié.
"""
        return result_text
    
    def log_result(self, has_tumor, prediction, confidence):
        """
        Enregistre les résultats dans un fichier log
        
        Args:
            has_tumor: présence de tumeur
            prediction: probabilité
            confidence: confiance
        """
        try:
            log_file = "analysis_log.txt"
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            status = "TUMEUR DÉTECTÉE" if has_tumor else "PAS DE TUMEUR"
            
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(f"\n{'='*60}\n")
                f.write(f"Date: {timestamp}\n")
                f.write(f"Image: {os.path.basename(self.current_image_path)}\n")
                f.write(f"Résultat: {status}\n")
                f.write(f"Probabilité: {prediction*100:.2f}%\n")
                f.write(f"Confiance: {confidence*100:.2f}%\n")
                f.write(f"{'='*60}\n")
                
        except Exception as e:
            print(f"Erreur lors de l'enregistrement du log: {e}")


def main():
    """Point d'entrée de l'application"""
    root = tk.Tk()
    app = BrainTumorDetectorApp(root)
    
    # Centrer la fenêtre sur l'écran
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()


if __name__ == "__main__":
    main()
