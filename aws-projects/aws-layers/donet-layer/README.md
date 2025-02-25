# 🏗 **4️⃣ Example 3: Creating a C# Lambda Layer (.NET 6)**

`Creating .NET Lambda Function is Very Bad Idea`

## **✅ Step 1: Create a .NET Core Project & Install Dependencies**

```sh
mkdir dotnet-layer && cd dotnet-layer
dotnet new classlib -n MyLambdaLayer
cd MyLambdaLayer
dotnet add package Newtonsoft.Json
dotnet build -c Release
```

> 📌 **This creates a .NET class library and installs `Newtonsoft.Json`.**
> 📌 **Please Specify the dotnet version as it current only support dotnet8**

---

## **✅ Step 2: Prepare the Layer Structure**

Create a directory and copy the compiled files:

```sh
mkdir -p dotnet/bin
cp -r bin/Release/net8.0/* dotnet/bin/
```

---

## **✅ Step 3: Zip and Upload the Layer**

```sh
zip -r dotnet-layer.zip dotnet/
aws lambda publish-layer-version \
  --layer-name DotNetLayer \
  --description "Layer for .NET 6 with Newtonsoft.Json" \
  --compatible-runtimes dotnet6 \
  --zip-file fileb://dotnet-layer.zip
```

or

```powershell
Compress-Archive -Path dotnet/bin -DestinationPath dotnet-layer.zip
```

> 📌 **zip file should contain bin directory as lambda will map it to `/opt/bin`.**

---

## **✅ Step 4: Use the Layer in a C# Lambda Function**

Modify `Function.cs` to use the library:

```csharp
using System;
using Newtonsoft.Json.Linq;

public class Function
{
    public string FunctionHandler(string input)
    {
        JObject json = JObject.Parse("{\"message\":\"Hello from Lambda\"}");
        return json["message"].ToString();
    }
}
```

📌 **Lambda will automatically load `Newtonsoft.Json` from `/opt/bin`.**
