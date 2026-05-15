from PIL import Image

def create_favicon():
    img_path = r"C:\Users\Henry\.gemini\antigravity\brain\4df8165c-036a-49aa-97c3-f40ac44702e0\media__1778865081306.png"
    img = Image.open(img_path)
    img = img.convert("RGBA")
    
    # Resize to a square
    img = img.resize((256, 256), Image.Resampling.LANCZOS)
    
    img.save('assets/favicon.ico', format='ICO', sizes=[(256, 256), (64, 64), (32, 32), (16, 16)])
    print("New favicon created and saved successfully.")

if __name__ == "__main__":
    create_favicon()
