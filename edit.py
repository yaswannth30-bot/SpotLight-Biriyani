import re

with open("d:\\spotlight_biriyani_website\\style.css", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Menu Grid
text = re.sub(r'\.menu-grid\s*\{[\s\S]*?\}', '.menu-grid {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));\n  gap: 24px;\n}', text, count=1)

# 2. Royale Menu Card
text = re.sub(r'\.menu-card\s*\{[\s\S]*?\}', '.menu-card {\n  background: #1c1815;\n  border: 1px solid #3c3224;\n  border-radius: 12px;\n  padding: 32px 24px;\n  min-height: 260px;\n  transition: all 0.3s ease;\n  box-shadow: 0 4px 15px rgba(0,0,0,0.2);\n  position: relative;\n  overflow: hidden;\n}', text, count=1)

text = re.sub(r'\.menu-card:hover\s*\{[\s\S]*?\}', '.menu-card:hover {\n  transform: translateY(-8px);\n  box-shadow: 0 15px 35px rgba(201,164,92,0.15);\n  border-color: #c9a45c;\n}', text, count=1)

# Typography inside card
text = re.sub(r'\.menu-card h3\s*\{[\s\S]*?\}', '.menu-card h3 {\n  font-family: "Cormorant Garamond";\n  font-size: 30px;\n  color: #c9a45c;\n  margin: 42px 0 10px;\n}', text, count=1)
text = re.sub(r'\.menu-card p\s*\{[\s\S]*?\}', '.menu-card p {\n  font-size: 13px;\n  color: #e9e0d3;\n}', text, count=1)

# Card top (the badge and price)
text = re.sub(r'\.card-top\s*\{[\s\S]*?\}', '.card-top {\n  display: flex;\n  justify-content: space-between;\n  color: #e9e0d3;\n  font-size: 10px;\n  letter-spacing: 1px;\n  font-weight: 700;\n  align-items: center;\n  margin-bottom: 20px;\n}', text, count=1)
text = re.sub(r'\.card-top b\s*\{[\s\S]*?\}', '.card-top b {\n  font-size: 20px;\n  color: #c9a45c;\n  background: none;\n}', text, count=1)

# add badge span style
if '.card-top span {' not in text:
    text = text.replace('.card-top {', '.card-top span {\n  background: #c9a45c;\n  color: #1c1815;\n  padding: 4px 12px;\n  border-radius: 20px;\n  display: inline-block;\n}\n.card-top {')

# Full menu section (Royale style)
text = re.sub(r'\.full-menu\s*\{[\s\S]*?\}', '.full-menu {\n  margin-top: 60px;\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));\n  gap: 20px;\n  background: #1c1815;\n  border-radius: 12px;\n  border: 1px solid #3c3224;\n  box-shadow: 0 10px 30px rgba(0,0,0,0.3);\n}', text, count=1)
text = re.sub(r'\.full-menu\s*>\s*div\s*\{[\s\S]*?\}', '.full-menu > div {\n  padding: 35px;\n  border-right: 1px solid #3c3224;\n}', text, count=1)
text = re.sub(r'\.full-menu h3\s*\{[\s\S]*?\}', '.full-menu h3 {\n  font-family: "Cormorant Garamond";\n  font-size: 25px;\n  color: #c9a45c;\n}', text, count=1)
text = re.sub(r'\.full-menu p\s*\{[\s\S]*?\}', '.full-menu p {\n  font-size: 13px;\n  color: #c5bbae;\n  margin-top: 8px;\n}', text, count=1)

# Menu Section background & Header colors
if '.menu-section {' not in text:
    text = text.replace('.menu-grid {', '.menu-section {\n  background: #110e0c;\n}\n.menu-section .section-head h2 {\n  color: #f8f0e4;\n}\n.menu-section .section-head p:last-child {\n  color: #c5bbae;\n}\n.menu-grid {')

# WhatsApp button fix
if '.whatsapp-btn {' not in text:
    text = text.replace('footer {', '.whatsapp-btn {\n  background-color: #25D366 !important;\n  color: #ffffff !important;\n  border: none !important;\n}\n.whatsapp-btn:hover {\n  background-color: #128C7E !important;\n}\n.whatsapp-btn svg {\n  fill: #ffffff !important;\n}\nfooter {')

with open("d:\\spotlight_biriyani_website\\style.css", "w", encoding="utf-8") as f:
    f.write(text)
