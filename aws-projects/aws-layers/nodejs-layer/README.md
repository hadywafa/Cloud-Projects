# 🌐 **5️⃣ Example 2: Creating a Node.js Lambda Layer (Latest Version)**

## **✅ Step 1: Install Dependencies Locally**

```sh
mkdir -p nodejs
npm install moment --prefix nodejs
```

📌 **This installs `moment.js` inside `nodejs/node_modules`.**

---

## **✅ Step 2: Zip the Directory**

```sh
zip -r nodejs-layer.zip nodejs/
```

or

```powershell
Compress-Archive -Path nodejs -DestinationPath nodejs-layer.zip
```

> 📌 **zip file should contain nodejs directory as lambda will map it to `/opt/nodejs/node_modules`.**

---

## **✅ Step 3: Upload the Layer to AWS**

```sh
aws lambda publish-layer-version \
  --layer-name NodeJsMomentLayer \
  --description "Moment.js library for Node.js" \
  --compatible-runtimes nodejs18.x \
  --zip-file fileb://nodejs-layer.zip
```

---

## **✅ Step 4: Use the Layer in a Node.js Lambda Function**

Modify `index.js`:

```javascript
import moment from "moment";

export const handler = async (event, context) => {
  console.log("EVENT: \n" + JSON.stringify(event, null, 2));
  return {
    statusCode: 200,
    body: `Current Time: ${moment().format("MMMM Do YYYY, h:mm:ss a")}`,
  };
};
```

📌 **Lambda will automatically load `moment.js` from `/opt/nodejs/node_modules`.**
