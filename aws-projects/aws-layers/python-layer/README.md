# 🐍 **3️⃣ Example 1: Creating a Python Lambda Layer (Latest Version)**

## **✅ Step 1: Install Python Dependencies Locally**

```sh
mkdir -p python
pip install requests -t python/
```

> 📌 **This installs the `requests` library inside a `python/` directory, which AWS Lambda expects.**

---

## **✅ Step 2: Zip the Directory**

```sh
zip -r python-layer.zip python/
```

or

```powershell
Compress-Archive -Path python -DestinationPath python-layer.zip
```

> 📌 **zip file should contain python directory as lambda will map it to `/opt/python/`.**

---

## **✅ Step 3: Upload the Layer to AWS**

```sh
aws lambda publish-layer-version \
  --layer-name PythonRequestsLayer \
  --description "Python requests library layer" \
  --compatible-runtimes python3.9 \
  --zip-file fileb://python-layer.zip
```

---

## **✅ Step 4: Use the Layer in a Python Lambda Function**

Attach the layer to your Lambda function, and modify your function like this:

```python
import requests

def lambda_handler(event, context):
    response = requests.get("https://api.github.com")
    return response.json()
```

> 📌 **The function automatically finds `requests` inside `/opt/python/`.**
