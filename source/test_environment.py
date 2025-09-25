#!/usr/bin/env python3
"""
Environment verification script for Language Translator Bot
"""

import sys
import importlib

def test_import(package_name, display_name=None):
    """Test if a package can be imported"""
    if display_name is None:
        display_name = package_name
    
    try:
        importlib.import_module(package_name)
        print(f"✅ {display_name}: OK")
        return True
    except ImportError as e:
        print(f"❌ {display_name}: FAILED - {e}")
        return False

def main():
    print("🔍 Testing Language Translator Environment...")
    print(f"Python version: {sys.version}")
    print("-" * 50)
    
    # Test all required packages
    packages = [
        ("streamlit", "Streamlit"),
        ("speech_recognition", "Speech Recognition"),
        ("googletrans", "Google Translate"),
        ("gtts", "Google Text-to-Speech"),
        ("pygame", "Pygame"),
        ("pyaudio", "PyAudio")
    ]
    
    all_passed = True
    for package, display in packages:
        if not test_import(package, display):
            all_passed = False
    
    print("-" * 50)
    if all_passed:
        print("🎉 All packages installed successfully!")
        print("Your environment is ready for the translator project.")
    else:
        print("⚠️  Some packages failed to import.")
        print("Please install missing packages before proceeding.")

if __name__ == "__main__":
    main()
