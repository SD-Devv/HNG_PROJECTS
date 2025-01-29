import express from "express";
import cors from "cors";

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// API Endpoint
app.get("/", (req, res) => {
  res.json({
    email: "danielbuyikunmisolomon@gmail.com",
    current_datetime: new Date().toISOString(),
    github_url: "https://github.com/SD-Devv/HNG_PROJECTS",
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
