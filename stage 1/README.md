# **Number Classification API**  

## **Overview**  
The **Number Classification API** takes an integer as input and returns its mathematical properties along with a fun fact.  

## **Endpoint**  
- **GET** `/api/classify-number?number=<integer>` 

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
    "number": "alphabet",
    "error": true
}
```  

## **Setup & Usage**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/SD-Devv/HNG_PROJECTS.git
cd HNG_PROJECTS/stage%201
```  

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```  

### **3️⃣ Run the API Locally**  
To run the API locally, use the following command:
```bash
python app.py
```

This will start the Flask API on `http://127.0.0.1:5000`.

## **Deployment**  
The API is publicly accessible at:  
👉 **`https://hng-public-api.onrender.com/api/classify-number?number=371`**

## **License**  
This project is licensed under the **MIT License**.
