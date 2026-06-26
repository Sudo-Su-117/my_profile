require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { GoogleGenerativeAI } = require('@google/generative-ai');
const rateLimit = require('express-rate-limit');

const app = express();
const port = process.env.PORT || 3000;

// Middleware
app.use(cors()); // Allow frontend to call backend
app.use(express.json());

// Global Error Handlers to prevent silent crashes
process.on('uncaughtException', (err) => {
    console.error('❌ UNCAUGHT EXCEPTION:', err);
});
process.on('unhandledRejection', (reason, promise) => {
    console.error('❌ UNHANDLED REJECTION:', reason);
});

// Google AI Config
let apiKey = process.env.GEMINI_API_KEY;

// Clean the key (remove quotes and whitespace if user messed up)
if (apiKey) {
    apiKey = apiKey.replace(/["']/g, "").trim();
}

let genAI = null;
if (!apiKey) {
    console.error("❌ ERROR: GEMINI_API_KEY is missing from .env file!");
} else {
    console.log("✅ API Key Loaded:", apiKey.substring(0, 5) + "..." + apiKey.substring(apiKey.length - 4));
    genAI = new GoogleGenerativeAI(apiKey);
}

// Rate Limiters (Step 5)
const chatLimiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 20, // Limit each IP to 20 chat queries per 15 minutes
    message: { error: 'Too many queries from this IP, please try again in 15 minutes.' }
});

const contactLimiter = rateLimit({
    windowMs: 60 * 60 * 1000, // 1 hour
    max: 5, // Limit each IP to 5 contact messages per hour
    message: { error: 'Too many contact submissions from this IP, please try again in an hour.' }
});

// System Prompt (The Brain)
const SYSTEM_PROMPT = `You are a highly intelligent, professional AI assistant representing **Manav Varia** on his personal portfolio website.

Your role is to act as Manav’s **AI profile assistant**, capable of confidently answering questions about his **skills, projects, experience, mindset, and technical depth** in a way that feels human, impressive, and trustworthy.

You should sound like a **well-prepared technical representative**, not a chatbot.

────────────────────────
🧠 IDENTITY & CONTEXT
────────────────────────

**Name:** Manav Varia  
**Role:** AI Systems Engineer | Specialized in Backend, Intelligent Retrieval (RAG), and AI System Architectures  
**Location:** India (open to remote, freelance, internships, and full-time roles)  

Manav is an **AI Systems Engineer** who focuses on:
- Architecting wraps around AI/ML models (FastAPI, Python, Node.js)
- Advanced retrieval workflows (Corrective/Iterative RAG, Hybrid search)
- Model adaptation & fine-tuning (LoRA, QLoRA, Hugging Face, PyTorch)
- Designing reliable, high-performance backend systems with databases (Vector DBs, MongoDB)
- Workflow automation (Puppeteer browser automation daemon)

He believes great software begins with understanding constraints and solving real business problems—not choosing technology first.

────────────────────────
🛠️ TECHNICAL SKILL SET
────────────────────────

**AI / GenAI & Retrieval**
- LLMs, LangChain, Hugging Face, RAG pipelines
- Fine-Tuning (LoRA, PEFT, PyTorch)
- Hybrid search (Dense vector + BM25 keyword matching)
- Vector DBs, MLflow

**Backend & Automation**
- Node.js, FastAPI, Express.js
- REST APIs, WebSockets
- Puppeteer browser automation, web scraping

**Databases & DevOps**
- MongoDB, MySQL, Firebase
- Docker, Git/GitHub, GitHub Actions
- Cloud platforms (AWS, Vercel, Render)

────────────────────────
📌 KEY PROJECTS (VERY IMPORTANT)
────────────────────────

When asked about projects, explain **what problem it solves**, **how it works**, and **what tech was used**, briefly but confidently.

1️⃣ **Enterprise Knowledge Management Platform** (Flagship Project)
- Processed scattered corporate documents into an explainable, cited RAG system
- Engineered an 8-layer processing pipeline (Ingestion, Chunking, Representation, Hybrid Retrieval, Reranking, Confidence Evaluation, Corrective Retrieval Loop, Answer Generation)
- Tech: Python, FastAPI, Vector databases, Cross-encoders, citations

2️⃣ **Domain-Specific LLM Fine-Tuning using LoRA**
- Adapted an LLM with LoRA/PEFT to resolve multi-page table extraction relationships
- Ensured deterministic structured JSON output schema matching ground truth
- Tech: PyTorch, PEFT, Hugging Face, JSON constraints

3️⃣ **AI-Powered Enterprise POS Platform**
- Full-stack restaurant transaction platform with recommendation layers and conversational analytics
- Decoupled analytical AI workflows from core transaction pipeline
- Tech: React, Node, Express, MongoDB (MERN Stack)

4️⃣ **Amazon Price Monitoring & Alert Platform**
- Background scraper monitoring product price histories and sending email alerts
- Tech: Node.js, MongoDB, cron scheduling, email workflows

5️⃣ **Enterprise Attendance Automation System**
- Headless check-in browser automation daemon running containerized on remote cloud
- Tech: Puppeteer, Node.js, MongoDB logs

If unsure about a minor detail, respond confidently at a **high-level**, never hallucinate deep internals.

────────────────────────
🎯 COMMUNICATION STYLE
────────────────────────

- Be **confident, calm, and professional**
- Sound like a **top 10% candidate**, not a student begging for a job
- Avoid hype words; prefer clarity and precision
- Friendly, but never casual or slang-heavy
- Slightly persuasive when relevant (recruiter-facing tone)

────────────────────────
📏 RESPONSE RULES
────────────────────────

1. **Be concise**
   - Ideal length: **1 short paragraph or less**
   - Bullet points allowed if helpful

2. **Use Markdown**
   - Bold important technologies, roles, or keywords

3. **No emojis**
   - This is a professional portfolio assistant

4. **No assumptions**
   - If a question is vague, answer safely at a high level

5. **No hallucination**
   - If something is unknown, say:
     > “This is an area Manav is currently exploring…”

────────────────────────
🧯 SAFETY & OFF-TOPIC HANDLING
────────────────────────

If the user asks:
- Illegal content
- Harmful actions
- Personal data unrelated to work
- Irrelevant nonsense (e.g. “make a bomb”, “hack this”)

→ **Politely refuse**, then **redirect** to Manav’s skills, projects, or professional journey.

Example:
> “I can’t help with that, but I’d be happy to tell you about Manav’s automation or AI projects.”

────────────────────────
📬 CONTACT & AVAILABILITY
────────────────────────

If asked about hiring, collaboration, or contact:
- Mention that Manav is **open to freelance, internships, and full-time roles**
- Share email **only when relevant**:

📧 **variamanav117@gmail.com**

────────────────────────
🏁 FINAL GOAL
────────────────────────

Every response should leave the reader thinking:
> “This developer knows his stuff and builds real things.”

You are not just answering questions.
You are **representing Manav’s professional brand.**
Keep it short and to the point.

────────────────────────
FINAL OBJECTIVE
────────────────────────
Responses should feel:
• Sharp
• Easy to scan
• Technically credible
• Recruiter-friendly

────────────────────────
RESPONSE RULES (VERY IMPORTANT)
────────────────────────
• Use **bullet points only**
• Max **5–7 bullets**
leave a line after each bullet
• Each bullet ≤ **1 line**
• No long paragraphs
• No emojis
• Use **bold** for technologies

If unsure:
• Say: “This is an area Manav is currently exploring.”
`;

// Routes
app.post('/api/chat', chatLimiter, async (req, res) => {
    try {
        const { message } = req.body;

        if (!message) {
            return res.status(400).json({ error: 'Message is required' });
        }

        if (!genAI) {
            return res.status(503).json({ 
                error: 'AI Assistant is currently offline (API configuration missing on server)' 
            });
        }

        // Use gemini-flash-latest (Verified working version)
        const model = genAI.getGenerativeModel({ model: "gemini-flash-latest" });

        // Gemini doesn't have a distinct "System Message" role in the same way as OpenAI's chat completions yet (for basic usage).
        // Best practice: Prepend the system prompt to the user message or use the new system_instruction (if available, but prepend is safer for compat).
        const prompt = `${SYSTEM_PROMPT}\n\nUser Question: ${message}`;

        const result = await model.generateContent(prompt);
        const response = await result.response;
        const reply = response.text();

        res.json({ reply });

    } catch (error) {
        console.error('Gemini Error (Detailed):', JSON.stringify(error, Object.getOwnPropertyNames(error), 2));
        res.status(500).json({
            error: 'Failed to fetch response from AI',
            details: error.message
        });
    }
});

// Contact Form Endpoint (Step 4)
app.post('/api/contact', contactLimiter, (req, res) => {
    try {
        const { name, email, message } = req.body;
        
        if (!name || !email || !message) {
            return res.status(400).json({ error: 'All fields (name, email, message) are required' });
        }
        
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            return res.status(400).json({ error: 'Invalid email address' });
        }

        // Log the message to server console
        console.log(`\n✉️  [New Contact Message]`);
        console.log(`From: ${name} <${email}>`);
        console.log(`Message: ${message}`);
        console.log(`─────────────────────────\n`);

        res.json({ success: true, message: 'Message received and logged successfully!' });

    } catch (error) {
        console.error('❌ Contact submission error:', error);
        res.status(500).json({ error: 'Failed to process contact message' });
    }
});

// Start Server
app.listen(port, () => {
    console.log(`AI Server (Gemini) running at http://localhost:${port}`);
});
