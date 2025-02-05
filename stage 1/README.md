# **Number Classification API**  

## **Overview**  
The **Number Classification API** takes an integer as input and returns its mathematical properties along with a fun fact.  

## **Endpoint**  
### **GET /api/classify-number?number={integer}**  

#### **✅ Success Response (200 OK)**  
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```  
#### **❌ Error Response (400 Bad Request)**  
```json
{
    "number": "abc",
    "error": true
}
```  

## **Setup & Usage**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/SD-username/number-classification-api.git
cd number-classification-api
```  
### **2️⃣ Install Dependencies**  
#### **Python (FastAPI)**  
```bash
pip install -r requirements.txt
```  
#### **Node.js (Express)**  
```bash
npm install
```  

### **3️⃣ Run the API**  
#### **Python (FastAPI)**  
```bash
uvicorn app:app --reload
```  
#### **Node.js (Express)**  
```bash
node index.js
```  

## **Deployment**  
The API is publicly accessible at:  
👉 **`https://SD-deployment-url.com/api/classify-number?number=371`**  

## **License**  
This project is licensed under the **MIT License**.  
