# RshellCoders
Payload Generator &amp; Encoder is a Python tool that generates a custom payload to establish a network connection via a socket (using a specified IP and port) and encodes it in various formats (Base64, Hex, ROT13, URL, UTF-16, Zlib)
```markdown
# Payload Generator & Encoder

**Payload Generator & Encoder** est un outil Python qui permet de générer un payload personnalisé pour se connecter à un serveur distant via socket, puis de l'encoder dans différents formats comme Base64, Hex, ROT13, URL, UTF-16 et Zlib. Ce script peut être utilisé pour créer des payloads masqués, souvent utilisés dans des tests de pénétration ou des environnements contrôlés pour évaluer la sécurité.

---

## 🚨 Avertissement

**Ce projet est à des fins éducatives uniquement.** Vous devez obtenir une autorisation explicite avant d'utiliser cet outil sur un réseau ou une machine cible. L'utilisation de cet outil pour compromettre des systèmes sans autorisation est illégale et peut entraîner des poursuites judiciaires.

L'auteur ne sera pas responsable de l'utilisation malveillante de ce code. Utilisez-le à vos risques et périls.

---

## 📜 Fonctionnalités

- **Génération de payload personnalisé** pour se connecter à un serveur distant via socket (en utilisant une adresse IP et un port donnés).
- **Encodage du payload** dans différents formats :
  - Base64
  - Hex
  - ROT13
  - URL encoding
  - UTF-16
  - Zlib compression
- **Génération d'un script Python** qui peut être exécuté pour décoder et exécuter le payload.
- **Interface interactive en ligne de commande** pour entrer les paramètres nécessaires et choisir le format d'encodage.

---

## ⚙️ Prérequis

- Python 3.x
- Bibliothèques Python standard (aucune dépendance externe requise)

---

## 🛠 Installation

1. Clonez ce dépôt sur votre machine :
   ```bash
   git clone https://github.com/votre-utilisateur/payload-generator-encoder.git
   ```

2. Accédez au répertoire du projet :
   ```bash
   cd payload-generator-encoder
   ```

---

## 🚀 Usage

### 1. Lancer le script

Exécutez le script `payload_generator.py` :

```bash
python payload_generator.py
```

### 2. Entrée des paramètres

- **IP** : Entrez l'adresse IP de la cible.
- **Port** : Entrez le port de la cible.
- **Nom du fichier de sortie** : Entrez le nom du fichier pour le script Python généré (sans extension `.py`).
- **Format d'encodage** : Choisissez l'un des formats suivants :
  - **1** : Base64
  - **2** : Hex
  - **3** : ROT13
  - **4** : URL encoding
  - **5** : UTF-16
  - **6** : Zlib

### 3. Exemple d'exécution

```
$ python payload_generator.py

[CDX] Enter your IP: 192.168.1.10
[CDX] Enter your port: 4444
[CDX] Enter the output filename (without extension): payload_script

[CDX] Choose the encoding format:
1. base64
2. hex
3. rot13
4. url
5. utf-16
6. zlib

[CDX] Enter the number of the encoding format: 1

[CDX] The script has been saved at: '/path/to/your/payload_script.py'.
```

---

## 🧳 Explication du code

1. **Génération du Payload** :
   - La fonction `generate_payload(ip, port)` génère un payload Python qui se connecte à un serveur via un socket en utilisant l'IP et le port fournis par l'utilisateur.
   
2. **Encodage du Payload** :
   - Le payload généré est ensuite encodé dans un format choisi par l'utilisateur : Base64, Hex, ROT13, URL, UTF-16, ou Zlib.

3. **Création du Script Python** :
   - La fonction `create_script(encoded_payload, encoding_format, output_filename)` génère un script Python qui inclut le payload encodé et un mécanisme de décodage pour exécuter le payload une fois le script lancé.

4. **Décodage et Exécution du Payload** :
   - Lorsque le script généré est exécuté, il décode le payload en fonction de l'encodage spécifié et utilise la fonction `exec()` pour l'exécuter.

---

## ⚠️ Licence

Ce projet est sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 📞 Contact

- **Auteur** : Hackfut
- **Contact** : [Telegram](https://t.me/HackfutSec)

---

## 🔧 Contributions

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ce projet ou ajouter de nouvelles fonctionnalités, veuillez soumettre une pull request.

---

## 📝 Remarques

- **Ethique** : Cet outil doit être utilisé uniquement dans des environnements de test où vous avez l'autorisation d'effectuer des évaluations de sécurité.
- **Usage malveillant** : L'utilisation de cet outil pour attaquer des systèmes sans autorisation est illégale.
- **Risques de sécurité** : Soyez prudent lorsque vous utilisez des payloads distants, surtout dans des environnements de production.

---

### Exemple de script généré :

```python
import base64
import binascii
import codecs
import urllib.parse
import zlib

def decode_payload(encoded_payload, encoding_format):
    if encoding_format == 'base64':
        return base64.b64decode(encoded_payload).decode('utf-8')
    elif encoding_format == 'hex':
        return binascii.unhexlify(encoded_payload).decode('utf-8')
    elif encoding_format == 'rot13':
        return codecs.decode(encoded_payload, 'rot_13')
    elif encoding_format == 'url':
        return urllib.parse.unquote(encoded_payload)
    elif encoding_format == 'utf-16':
        return encoded_payload.encode('latin-1').decode('utf-16')
    elif encoding_format == 'zlib':
        return zlib.decompress(bytes.fromhex(encoded_payload)).decode('utf-8')
    else:
        raise ValueError("Unrecognized encoding format.")

if __name__ == "__main__":
    encoded_payload = 'BASE64_ENCODED_PAYLOAD'
    encoding_format = 'base64'
    
    # Decode and execute the payload
    exec(decode_payload(encoded_payload, encoding_format))
```

---

**Attention** : Ce script génère des payloads qui peuvent potentiellement être utilisés à des fins malveillantes. Soyez responsable dans son utilisation.
```

---

### Explication des sections :

- **Usage** : Explique comment l'utilisateur interagit avec l'outil et fournit un exemple d'exécution.
- **Génération du payload** : Détaille les différentes étapes que suit le script pour créer un payload et l'encoder dans différents formats.
- **Licence** : Rappelle à l'utilisateur que le projet est sous licence MIT et doit être utilisé de manière éthique.
- **Contact** : Fournit un moyen de contacter l'auteur du projet.

Cela permettra à tout utilisateur de comprendre comment utiliser l'outil et d'en savoir plus sur son fonctionnement.
