# **HNG12 Public API**  

This is my submission for the **Stage 0 Backend** task in the **HNG12 internship**. The API returns my **registered email**, the **current datetime in ISO 8601 format**, and the **GitHub URL** of the project.  

## **API Endpoint**  

### **GET `/`**  

Returns:  

```json
{
  "email": "danielbuyikunmisolomon@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/SD-Devv/HNG_PROJECTS"
}
```  

## **How to Run Locally**  

1. Clone the repository:  
   ```bash
   git clone https://github.com/SD-Devv/HNG_PROJECTS.git && cd hng-public-api
   ```  
2. Install dependencies:  
   ```bash
   npm install
   ```  
3. Start the server:  
   ```bash
   node index.js
   ```  
   Runs at **`http://localhost:3000`**.  

## **Deployment**  

🔗 **Live API:** [https://hng-public-api.onrender.com](https://hng-public-api.onrender.com)  

## **Submission Compliance**  

✅ Returns correct JSON response  
✅ ISO 8601 timestamp (UTC)  
✅ Hosted on **GitHub** (Public)  
✅ **Deployed & publicly accessible**  
