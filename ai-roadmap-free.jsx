import { useState } from "react";

const freeToolsBadges = [
  { name: "Ollama", desc: "Run LLMs locally", color: "#00D4FF" },
  { name: "HuggingFace", desc: "Free models & datasets", color: "#FF6B35" },
  { name: "LM Studio", desc: "Local LLM GUI", color: "#A855F7" },
  { name: "ChromaDB", desc: "Free vector DB", color: "#10B981" },
  { name: "PyTorch", desc: "Deep learning", color: "#FF6B35" },
  { name: "Scikit-learn", desc: "ML library", color: "#00D4FF" },
  { name: "LangChain", desc: "Agent framework", color: "#A855F7" },
  { name: "Streamlit", desc: "Free UI deployment", color: "#10B981" },
  { name: "FastAPI", desc: "Free API server", color: "#00D4FF" },
  { name: "CrewAI", desc: "Multi-agent (OSS)", color: "#FF6B35" },
  { name: "MLflow", desc: "Experiment tracking", color: "#A855F7" },
  { name: "Gradio", desc: "Free model UI", color: "#10B981" },
];

const roadmapData = [
  {
    id: 1,
    phase: "PHASE 01",
    title: "AI Foundations",
    subtitle: "Beginner → Intermediate",
    duration: "20 Hours",
    color: "#00D4FF",
    icon: "🧠",
    tagline: "Think like a machine. Build like an engineer.",
    weeks: [
      {
        week: "Week 1–2",
        topic: "Python for AI + Math Essentials",
        hours: "8 hrs",
        concepts: [
          "NumPy, Pandas, Matplotlib — all free, pip install",
          "Linear Algebra basics (Khan Academy — free)",
          "Probability & Statistics (free datasets on Kaggle)",
          "Python OOP for AI pipelines"
        ],
        project: {
          name: "📊 Smart Data Analyzer",
          desc: "Build a CLI + Streamlit web app that loads any CSV, auto-detects types, generates statistical summaries, plots distributions, and flags anomalies. Deploy locally via Streamlit — zero cost.",
          skills: ["Pandas", "Matplotlib", "Seaborn", "Streamlit"],
          freeNote: "All pip-installable. Dataset: Kaggle Titanic / UCI ML Repo (both free).",
          github: "scikit-learn/scikit-learn"
        }
      },
      {
        week: "Week 3",
        topic: "How AI Works — Core Concepts",
        hours: "6 hrs",
        concepts: [
          "Types of AI: Narrow / General / Super",
          "Supervised vs Unsupervised vs Reinforcement Learning",
          "Train / Validation / Test splits",
          "Bias, Variance, Overfitting & how to fix them"
        ],
        project: {
          name: "🤖 Spam Detector from Scratch",
          desc: "Train Naive Bayes + Logistic Regression on the free SMS Spam Collection dataset (UCI). Compare models, plot confusion matrices, build a Gradio UI so anyone can test it in the browser — runs 100% on your machine.",
          skills: ["Scikit-learn", "Gradio", "NLTK", "Pandas"],
          freeNote: "Dataset: UCI SMS Spam Collection (free). Gradio UI runs locally on port 7860.",
          github: "huggingface/datasets"
        }
      },
      {
        week: "Week 4",
        topic: "Local LLMs + RAG (No API Key Needed)",
        hours: "6 hrs",
        concepts: [
          "How LLMs work: tokens, context windows, temperature",
          "Running LLMs locally with Ollama (Llama 3, Mistral, Phi-3)",
          "Prompt engineering: zero-shot, few-shot, chain-of-thought",
          "RAG: chunking, embedding, vector search"
        ],
        project: {
          name: "📚 Offline Knowledge Assistant",
          desc: "Install Ollama → pull Llama 3.2 (free) → chunk your own PDF notes → embed with sentence-transformers (free, HuggingFace) → store in ChromaDB (free, local) → chat with your documents. Zero internet required after setup.",
          skills: ["Ollama", "LangChain", "ChromaDB", "sentence-transformers", "Gradio"],
          freeNote: "Ollama is free & open source. Llama 3.2 3B runs on 8GB RAM. No API key ever.",
          github: "ollama/ollama"
        }
      }
    ]
  },
  {
    id: 2,
    phase: "PHASE 02",
    title: "Agentic AI",
    subtitle: "Intermediate → Advanced",
    duration: "20 Hours",
    color: "#FF6B35",
    icon: "⚡",
    tagline: "Give AI a mission. Watch it execute.",
    weeks: [
      {
        week: "Week 1–2",
        topic: "Agents, Tools & ReAct Framework",
        hours: "8 hrs",
        concepts: [
          "ReAct: Reason + Act loop (how agents think)",
          "Tool use: give LLM functions it can call",
          "Memory: in-context (short) vs vector store (long)",
          "LangChain AgentExecutor with local Ollama backend"
        ],
        project: {
          name: "🔍 Local Web Research Agent",
          desc: "An agent powered by Ollama (Mistral 7B) that takes a research topic, uses DuckDuckGo Search (free, no key) + Wikipedia tool, reads pages with BeautifulSoup, and writes a structured markdown report. Fully offline-capable except DuckDuckGo queries.",
          skills: ["LangChain", "Ollama", "DuckDuckGo Search (free)", "BeautifulSoup4", "Gradio"],
          freeNote: "DuckDuckGo search via `duckduckgo-search` pip package — no API key. Ollama as LLM backend.",
          github: "langchain-ai/langchain"
        }
      },
      {
        week: "Week 3",
        topic: "Multi-Agent Systems",
        hours: "6 hrs",
        concepts: [
          "Orchestrator-Worker pattern",
          "Agent roles, goals, and backstories (CrewAI)",
          "Agents sharing context and passing outputs",
          "Error handling and retry logic"
        ],
        project: {
          name: "🏢 AI Dev Team Simulation",
          desc: "3 CrewAI agents: Architect (designs solution), Coder (writes Python), Reviewer (finds bugs). Give them a mini-task like 'build a to-do CLI app' — they collaborate, produce code, review it, and output a final README. Powered by Ollama locally.",
          skills: ["CrewAI (OSS)", "Ollama", "LangChain", "Python"],
          freeNote: "CrewAI is fully open source. pip install crewai. Uses Ollama as free local LLM.",
          github: "crewAIInc/crewAI"
        }
      },
      {
        week: "Week 4",
        topic: "Agentic Pipelines with LangGraph",
        hours: "6 hrs",
        concepts: [
          "LangGraph: stateful, graph-based agent workflows",
          "Conditional edges and looping agents",
          "Human-in-the-loop checkpoints",
          "Persisting agent state with SQLite (free)"
        ],
        project: {
          name: "💼 Resume Tailoring Agent",
          desc: "Paste a job description → LangGraph agent reads it (Ollama) → extracts required skills → rewrites your resume sections to match → generates a cover letter → saves outputs as .md files. All local, all free, state persisted in SQLite.",
          skills: ["LangGraph (OSS)", "Ollama", "SQLite", "Gradio"],
          freeNote: "LangGraph is open source by LangChain. SQLite is built into Python — no DB setup.",
          github: "langchain-ai/langgraph"
        }
      }
    ]
  },
  {
    id: 3,
    phase: "PHASE 03",
    title: "Machine Learning",
    subtitle: "Intermediate → Advanced",
    duration: "20 Hours",
    color: "#A855F7",
    icon: "📈",
    tagline: "Extract patterns. Make predictions. Automate decisions.",
    weeks: [
      {
        week: "Week 1–2",
        topic: "Classical ML Algorithms Deep Dive",
        hours: "8 hrs",
        concepts: [
          "Linear & Logistic Regression from scratch + sklearn",
          "Decision Trees, Random Forests, XGBoost (free)",
          "SVM, KNN, K-Means Clustering",
          "Feature engineering, selection, pipelines"
        ],
        project: {
          name: "🏦 Credit Risk Scoring System",
          desc: "Use the free Kaggle 'Give Me Some Credit' dataset (or UCI Credit dataset). Handle class imbalance with SMOTE, engineer financial features, train XGBoost, explain decisions with SHAP plots. Build a Streamlit dashboard — run locally.",
          skills: ["XGBoost (free)", "SHAP (free)", "imbalanced-learn", "Streamlit", "Pandas"],
          freeNote: "All free pip packages. Dataset from Kaggle (free account) or UCI ML Repo.",
          github: "dmlc/xgboost"
        }
      },
      {
        week: "Week 3",
        topic: "MLOps: Pipelines, Tracking & Serving",
        hours: "6 hrs",
        concepts: [
          "Scikit-learn Pipeline API",
          "Hyperparameter tuning with Optuna (free OSS)",
          "MLflow experiment tracking (self-hosted, free)",
          "Serving models via FastAPI (free)"
        ],
        project: {
          name: "🏠 House Price Predictor API",
          desc: "Full pipeline: EDA on California Housing dataset (built into sklearn, free) → feature engineering → Optuna tuning → log all runs to local MLflow → best model served via FastAPI endpoint → Dockerize (Docker is free). Production-grade, zero cost.",
          skills: ["Scikit-learn", "Optuna (OSS)", "MLflow (OSS)", "FastAPI", "Docker (free)"],
          freeNote: "California Housing dataset ships with sklearn. MLflow self-hosted = free forever.",
          github: "mlflow/mlflow"
        }
      },
      {
        week: "Week 4",
        topic: "Time Series & Recommender Systems",
        hours: "6 hrs",
        concepts: [
          "Time series: ARIMA, Prophet (Meta OSS), statsmodels",
          "Collaborative filtering from scratch + Surprise lib",
          "Content-based filtering with TF-IDF",
          "Hybrid recommender systems"
        ],
        project: {
          name: "🎬 Movie Recommender + Trend Predictor",
          desc: "MovieLens 100K dataset (free, GroupLens) → collaborative + content-based hybrid recommender. Add Prophet (free, Meta OSS) to predict genre popularity trends over time. Full Streamlit app with user-based recommendations.",
          skills: ["Surprise (OSS)", "Prophet (Meta OSS)", "Streamlit", "Scikit-learn"],
          freeNote: "MovieLens 100K is free for research. Prophet is open-sourced by Meta.",
          github: "facebook/prophet"
        }
      }
    ]
  },
  {
    id: 4,
    phase: "PHASE 04",
    title: "Deep Learning",
    subtitle: "Advanced → Expert",
    duration: "20 Hours",
    color: "#10B981",
    icon: "🔥",
    tagline: "Neural networks. Zero to frontier.",
    weeks: [
      {
        week: "Week 1–2",
        topic: "Neural Networks + CNNs",
        hours: "8 hrs",
        concepts: [
          "Backpropagation & gradient descent (build from scratch)",
          "CNN layers: Conv2D, MaxPool, BatchNorm",
          "Transfer learning: ResNet18, EfficientNet (free on HuggingFace)",
          "Data augmentation with Albumentations (free)"
        ],
        project: {
          name: "🩺 Medical Image Classifier",
          desc: "Chest X-Ray dataset from Kaggle (free, CC license). Fine-tune ResNet18 via PyTorch + torchvision (both free). Implement Grad-CAM heatmaps to visualize what the model sees. Deploy as Gradio app — runs on CPU if no GPU, or free Colab GPU.",
          skills: ["PyTorch (free)", "torchvision", "Gradio", "Albumentations (OSS)", "Grad-CAM"],
          freeNote: "PyTorch is 100% free & OSS. Use Google Colab free tier (T4 GPU) for training. Dataset: Kaggle free.",
          github: "pytorch/pytorch"
        }
      },
      {
        week: "Week 3",
        topic: "NLP + Transformers + Fine-Tuning",
        hours: "6 hrs",
        concepts: [
          "Attention mechanism & self-attention from scratch",
          "BERT, DistilBERT, RoBERTa architecture",
          "Fine-tuning with HuggingFace Trainer API (free)",
          "PEFT / LoRA: fine-tune large models on CPU/low RAM"
        ],
        project: {
          name: "📰 Fake News Detector",
          desc: "Fine-tune DistilBERT (lighter, faster than BERT) on the free LIAR dataset (HuggingFace datasets). Use PEFT/LoRA to fine-tune on even a laptop. Deploy as Gradio app. Optional: use free Colab T4 GPU to fine-tune full BERT.",
          skills: ["HuggingFace Transformers (free)", "PEFT / LoRA (free)", "Gradio", "Datasets lib"],
          freeNote: "HuggingFace is entirely free for open models. LIAR dataset free on HF Hub. LoRA reduces VRAM 10x.",
          github: "huggingface/transformers"
        }
      },
      {
        week: "Week 4",
        topic: "Generative AI — Diffusion & LLM Fine-Tuning",
        hours: "6 hrs",
        concepts: [
          "GANs: Generator + Discriminator training loop",
          "Diffusion models: DDPM forward & reverse process",
          "Stable Diffusion locally via diffusers (HuggingFace, free)",
          "LoRA fine-tuning for custom image styles"
        ],
        project: {
          name: "🎨 Custom AI Art Generator",
          desc: "Install diffusers + Stable Diffusion 1.5 (free weights on HuggingFace) locally. Fine-tune with LoRA on 20 of your own images to create a custom art model. Build a Gradio interface with prompt input, style controls, and image gallery. 100% local, runs on 8GB VRAM or Google Colab free.",
          skills: ["diffusers (HuggingFace OSS)", "LoRA / PEFT", "Gradio", "Stable Diffusion 1.5 (free weights)"],
          freeNote: "SD 1.5 weights are free on HuggingFace. diffusers is OSS. Colab free tier has enough GPU for inference.",
          github: "huggingface/diffusers"
        }
      }
    ]
  }
];

const freeResources = [
  { category: "Run LLMs Locally", tools: ["Ollama (ollama.com) — Free", "LM Studio — Free GUI", "llama.cpp — C++ backend", "GPT4All — Offline LLMs"] },
  { category: "Free Models (HuggingFace)", tools: ["Llama 3.2 (Meta, free)", "Mistral 7B (free)", "Phi-3 Mini (Microsoft, free)", "DistilBERT, RoBERTa (free)"] },
  { category: "Free Datasets", tools: ["Kaggle Datasets (free account)", "HuggingFace Datasets Hub", "UCI ML Repository", "Google Dataset Search"] },
  { category: "Free GPU (Training)", tools: ["Google Colab (T4 GPU free)", "Kaggle Notebooks (30hr/wk GPU)", "HuggingFace Spaces (free)", "Lightning.ai (free tier)"] },
  { category: "Free Deployment", tools: ["Gradio (local + HF Spaces)", "Streamlit (local + Community)", "FastAPI (self-hosted)", "HuggingFace Spaces (free)"] },
  { category: "Free Agent Frameworks", tools: ["LangChain (OSS)", "LangGraph (OSS)", "CrewAI (OSS)", "AutoGen (Microsoft, OSS)"] },
];

export default function AIRoadmapFree() {
  const [activePhase, setActivePhase] = useState(null);
  const [activeWeek, setActiveWeek] = useState(null);
  const [showResources, setShowResources] = useState(false);

  const toggle = (phaseId, weekIdx) => {
    const key = `${phaseId}-${weekIdx}`;
    setActiveWeek(prev => prev === key ? null : key);
    setActivePhase(phaseId);
  };

  return (
    <div style={{
      fontFamily: "'Courier New', monospace",
      background: "#080810",
      minHeight: "100vh",
      color: "#e0e0e0",
      overflowX: "hidden"
    }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');
        * { box-sizing: border-box; margin: 0; padding: 0; }
        .phase-header { cursor: pointer; transition: all 0.25s; }
        .phase-header:hover { filter: brightness(1.06); }
        .week-toggle { cursor: pointer; transition: all 0.2s; }
        .week-toggle:hover { opacity: 0.9; }
        .free-badge {
          display: inline-flex; align-items: center; gap: 4px;
          background: rgba(16,185,129,0.12); border: 1px solid rgba(16,185,129,0.35);
          border-radius: 4px; padding: 2px 8px; font-size: 10px;
          color: #10B981; font-weight: 700; letter-spacing: 0.5px;
        }
        .tool-tag {
          display: inline-block; background: #0f0f1a; border: 1px solid #222;
          border-radius: 4px; padding: 3px 9px; font-size: 10px;
          color: #888; margin: 2px; letter-spacing: 0.5px;
        }
        .resource-card {
          background: #0d0d18; border: 1px solid #1a1a2a;
          border-radius: 10px; padding: 18px;
        }
        .github-link {
          display: inline-flex; align-items: center; gap: 5px;
          color: #444; font-size: 11px; text-decoration: none;
          border: 1px solid #222; border-radius: 4px; padding: 3px 10px;
          transition: all 0.2s;
        }
        .github-link:hover { color: #888; border-color: #444; }
        .zero-cost-strip {
          background: linear-gradient(90deg, rgba(16,185,129,0.08), rgba(16,185,129,0.03));
          border: 1px solid rgba(16,185,129,0.2);
          border-radius: 6px; padding: 8px 14px;
          font-size: 11px; color: #10B981; margin-top: 10px;
          display: flex; align-items: flex-start; gap: 8px;
        }
      `}</style>

      {/* Hero */}
      <div style={{
        background: "#080810",
        borderBottom: "1px solid #12121e",
        padding: "56px 24px 48px",
        textAlign: "center",
        position: "relative",
        overflow: "hidden"
      }}>
        <div style={{
          position: "absolute", inset: 0,
          backgroundImage: "linear-gradient(#12121e 1px, transparent 1px), linear-gradient(90deg, #12121e 1px, transparent 1px)",
          backgroundSize: "48px 48px", opacity: 0.25
        }} />
        <div style={{ position: "relative", zIndex: 1 }}>
          {/* Free Banner */}
          <div style={{
            display: "inline-flex", alignItems: "center", gap: "10px",
            background: "rgba(16,185,129,0.1)", border: "1px solid rgba(16,185,129,0.4)",
            borderRadius: "6px", padding: "8px 20px", marginBottom: "24px"
          }}>
            <span style={{ fontSize: "16px" }}>🆓</span>
            <span style={{ color: "#10B981", fontSize: "12px", fontWeight: 700, letterSpacing: "2px" }}>
              100% FREE · OPEN SOURCE ONLY · NO API KEYS · NO SUBSCRIPTIONS
            </span>
          </div>

          <h1 style={{
            fontFamily: "'Syne', sans-serif",
            fontSize: "clamp(32px, 6vw, 66px)",
            fontWeight: 800,
            lineHeight: 1.05,
            background: "linear-gradient(135deg, #fff 0%, #a0e8c8 40%, #10B981 100%)",
            WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent",
            marginBottom: "14px"
          }}>
            AI Engineering<br/>Zero-Cost Roadmap
          </h1>
          <p style={{ color: "#555", fontSize: "15px", letterSpacing: "1px", marginBottom: "36px" }}>
            Student → Expert · 80 Hours · 12 Projects · $0 Budget Required
          </p>

          {/* Stats */}
          <div style={{ display: "flex", gap: "10px", justifyContent: "center", flexWrap: "wrap", maxWidth: "680px", margin: "0 auto 32px" }}>
            {[
              { v: "80hrs", l: "Total Learning" },
              { v: "12", l: "Real Projects" },
              { v: "$0", l: "Total Cost" },
              { v: "40+", l: "OSS Tools" },
              { v: "4", l: "Phases" },
            ].map(s => (
              <div key={s.l} style={{
                background: "#0f0f1a", border: "1px solid #1a1a28",
                borderRadius: "10px", padding: "16px 20px", textAlign: "center", flex: 1, minWidth: "100px"
              }}>
                <div style={{ fontSize: "26px", fontWeight: 700, color: "#10B981", fontFamily: "'Syne', sans-serif" }}>{s.v}</div>
                <div style={{ fontSize: "10px", color: "#444", letterSpacing: "1px", marginTop: "3px" }}>{s.l}</div>
              </div>
            ))}
          </div>

          {/* Free tools pills */}
          <div style={{ display: "flex", flexWrap: "wrap", gap: "6px", justifyContent: "center", maxWidth: "800px", margin: "0 auto" }}>
            {freeToolsBadges.map(t => (
              <div key={t.name} style={{
                background: `${t.color}10`, border: `1px solid ${t.color}30`,
                borderRadius: "20px", padding: "4px 14px",
                fontSize: "11px", color: t.color, fontWeight: 700
              }}>
                {t.name}
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Phase Flow Bar */}
      <div style={{ padding: "32px 24px 16px", textAlign: "center" }}>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "center", flexWrap: "wrap", gap: 0, maxWidth: "900px", margin: "0 auto" }}>
          {roadmapData.map((phase, i) => (
            <div key={phase.id} style={{ display: "flex", alignItems: "center" }}>
              <div
                onClick={() => setActivePhase(p => p === phase.id ? null : phase.id)}
                style={{
                  background: activePhase === phase.id ? phase.color : "transparent",
                  border: `2px solid ${phase.color}`,
                  borderRadius: "8px", padding: "10px 18px",
                  cursor: "pointer", transition: "all 0.25s",
                  color: activePhase === phase.id ? "#000" : phase.color,
                  fontSize: "12px", fontWeight: 700, letterSpacing: "1px", whiteSpace: "nowrap"
                }}>
                {phase.icon} {phase.title}
              </div>
              {i < roadmapData.length - 1 && (
                <div style={{ width: "36px", height: "2px", background: `linear-gradient(90deg, ${phase.color}, ${roadmapData[i+1].color})`, flexShrink: 0 }} />
              )}
            </div>
          ))}
        </div>
        <p style={{ color: "#2a2a3a", fontSize: "10px", marginTop: "10px", letterSpacing: "1px" }}>CLICK TO JUMP TO PHASE</p>
      </div>

      {/* Main Content */}
      <div style={{ maxWidth: "980px", margin: "0 auto", padding: "16px 24px 60px" }}>

        {roadmapData.map((phase, phaseIdx) => (
          <div key={phase.id} style={{ marginBottom: "14px" }}>

            {/* Phase Header */}
            <div
              className="phase-header"
              onClick={() => setActivePhase(p => p === phase.id ? null : phase.id)}
              style={{
                background: activePhase === phase.id
                  ? `linear-gradient(135deg, ${phase.color}14 0%, transparent 100%)`
                  : "#0d0d18",
                border: `1px solid ${activePhase === phase.id ? phase.color + "50" : "#1a1a26"}`,
                borderRadius: "12px",
                padding: "26px 28px",
                display: "flex", alignItems: "center", justifyContent: "space-between",
                flexWrap: "wrap", gap: "16px"
              }}>
              <div style={{ display: "flex", alignItems: "center", gap: "18px" }}>
                <div style={{
                  fontSize: "38px", width: "60px", height: "60px",
                  background: `${phase.color}12`, border: `1px solid ${phase.color}25`,
                  borderRadius: "12px", display: "flex", alignItems: "center", justifyContent: "center",
                  flexShrink: 0
                }}>{phase.icon}</div>
                <div>
                  <div style={{ fontSize: "10px", color: phase.color, letterSpacing: "3px", fontWeight: 700, marginBottom: "4px" }}>
                    {phase.phase} · {phase.duration}
                  </div>
                  <h2 style={{
                    fontFamily: "'Syne', sans-serif", margin: 0,
                    fontSize: "clamp(18px, 3vw, 26px)", fontWeight: 800, color: "#fff"
                  }}>{phase.title}</h2>
                  <div style={{ color: "#444", fontSize: "12px", marginTop: "3px" }}>{phase.subtitle}</div>
                </div>
              </div>
              <div style={{ display: "flex", flexDirection: "column", alignItems: "flex-end", gap: "8px" }}>
                <span className="free-badge">✓ 100% FREE</span>
                <div style={{ color: "#333", fontSize: "12px", fontStyle: "italic", maxWidth: "180px", textAlign: "right", lineHeight: 1.4 }}>
                  "{phase.tagline}"
                </div>
                <div style={{
                  color: activePhase === phase.id ? phase.color : "#2a2a3a",
                  transition: "transform 0.3s",
                  transform: activePhase === phase.id ? "rotate(180deg)" : "rotate(0deg)",
                  display: "inline-block", fontSize: "16px"
                }}>▼</div>
              </div>
            </div>

            {/* Phase Body */}
            {activePhase === phase.id && (
              <div style={{
                borderLeft: `3px solid ${phase.color}35`,
                marginLeft: "30px", paddingLeft: "22px", paddingTop: "6px"
              }}>
                {phase.weeks.map((week, wIdx) => {
                  const key = `${phase.id}-${wIdx}`;
                  const isOpen = activeWeek === key;
                  return (
                    <div key={wIdx} style={{ marginBottom: "8px" }}>
                      {/* Week Header */}
                      <div
                        className="week-toggle"
                        onClick={() => toggle(phase.id, wIdx)}
                        style={{
                          background: isOpen ? `${phase.color}10` : "#0b0b16",
                          border: `1px solid ${isOpen ? phase.color + "40" : "#181824"}`,
                          borderRadius: "10px", padding: "16px 22px",
                          display: "flex", alignItems: "center", justifyContent: "space-between",
                          flexWrap: "wrap", gap: "10px"
                        }}>
                        <div style={{ display: "flex", alignItems: "center", gap: "12px" }}>
                          <div style={{
                            width: "12px", height: "12px", borderRadius: "50%", flexShrink: 0,
                            background: isOpen ? phase.color : "transparent",
                            border: `2px solid ${phase.color}`
                          }} />
                          <div>
                            <div style={{ fontSize: "10px", color: phase.color, letterSpacing: "2px", marginBottom: "3px" }}>
                              {week.week} · {week.hours}
                            </div>
                            <div style={{ fontFamily: "'Syne', sans-serif", fontWeight: 600, fontSize: "15px", color: "#ccc" }}>
                              {week.topic}
                            </div>
                          </div>
                        </div>
                        <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
                          <div style={{
                            background: `${phase.color}15`, border: `1px solid ${phase.color}35`,
                            borderRadius: "20px", padding: "4px 12px",
                            fontSize: "11px", color: phase.color, fontWeight: 700
                          }}>
                            🚀 {week.project.name.split(" ").slice(1).join(" ")}
                          </div>
                          <span className="free-badge" style={{ fontSize: "9px" }}>FREE</span>
                          <div style={{ color: "#2a2a3a", fontSize: "13px" }}>{isOpen ? "▲" : "▼"}</div>
                        </div>
                      </div>

                      {/* Week Detail */}
                      {isOpen && (
                        <div style={{
                          background: "#070710",
                          border: `1px solid ${phase.color}20`,
                          borderTop: "none",
                          borderRadius: "0 0 10px 10px",
                          padding: "22px"
                        }}>
                          <div style={{
                            display: "grid",
                            gridTemplateColumns: "1fr 1fr",
                            gap: "22px"
                          }}
                          className="week-grid">
                            <style>{`.week-grid { @media(max-width:580px){ grid-template-columns: 1fr !important; } }`}</style>

                            {/* Concepts */}
                            <div>
                              <div style={{ fontSize: "10px", letterSpacing: "2px", color: "#333", marginBottom: "14px", fontWeight: 700 }}>CONCEPTS COVERED</div>
                              <div style={{ display: "flex", flexDirection: "column", gap: "9px" }}>
                                {week.concepts.map((c, ci) => (
                                  <div key={ci} style={{ display: "flex", gap: "10px", alignItems: "flex-start" }}>
                                    <div style={{ color: phase.color, fontSize: "9px", marginTop: "5px", flexShrink: 0 }}>◆</div>
                                    <div style={{ color: "#888", fontSize: "12px", lineHeight: 1.55 }}>{c}</div>
                                  </div>
                                ))}
                              </div>
                            </div>

                            {/* Project */}
                            <div>
                              <div style={{ fontSize: "10px", letterSpacing: "2px", color: "#333", marginBottom: "14px", fontWeight: 700 }}>CAPSTONE PROJECT</div>
                              <div style={{
                                background: `${phase.color}07`,
                                border: `1px solid ${phase.color}25`,
                                borderRadius: "10px", padding: "16px"
                              }}>
                                <div style={{ fontFamily: "'Syne', sans-serif", fontWeight: 700, fontSize: "14px", color: "#fff", marginBottom: "10px" }}>
                                  {week.project.name}
                                </div>
                                <p style={{ color: "#777", fontSize: "12px", lineHeight: 1.7, marginBottom: "14px" }}>
                                  {week.project.desc}
                                </p>

                                {/* Tech Stack */}
                                <div style={{ marginBottom: "10px" }}>
                                  <div style={{ fontSize: "9px", color: "#333", letterSpacing: "1px", marginBottom: "6px" }}>FREE TECH STACK</div>
                                  <div style={{ display: "flex", flexWrap: "wrap" }}>
                                    {week.project.skills.map((s, si) => (
                                      <span key={si} className="tool-tag">{s}</span>
                                    ))}
                                  </div>
                                </div>

                                {/* Zero Cost Note */}
                                <div className="zero-cost-strip">
                                  <span style={{ flexShrink: 0 }}>💡</span>
                                  <span style={{ lineHeight: 1.5 }}>{week.project.freeNote}</span>
                                </div>

                                {/* GitHub Link */}
                                <div style={{ marginTop: "10px" }}>
                                  <a
                                    href={`https://github.com/${week.project.github}`}
                                    target="_blank" rel="noopener noreferrer"
                                    className="github-link">
                                    ⭐ github.com/{week.project.github}
                                  </a>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      )}
                    </div>
                  );
                })}

                {/* Phase Footer */}
                <div style={{
                  background: `${phase.color}06`,
                  border: `1px dashed ${phase.color}25`,
                  borderRadius: "8px", padding: "14px 20px",
                  marginBottom: "12px",
                  display: "flex", justifyContent: "space-between",
                  flexWrap: "wrap", gap: "10px", alignItems: "center"
                }}>
                  <div style={{ fontSize: "12px", color: "#444" }}>
                    <span style={{ color: phase.color, fontWeight: 700 }}>Phase {phase.id} Complete</span> · {phase.weeks.length} modules · {phase.weeks.length} free projects
                  </div>
                  <span className="free-badge">All tools: $0 cost</span>
                </div>
              </div>
            )}
          </div>
        ))}

        {/* Free Resources Section */}
        <div style={{ marginTop: "48px" }}>
          <button
            onClick={() => setShowResources(p => !p)}
            style={{
              width: "100%", background: "#0d0d18",
              border: "1px solid #1e1e2e", borderRadius: "12px",
              padding: "22px 28px", cursor: "pointer",
              display: "flex", alignItems: "center", justifyContent: "space-between",
              color: "#fff", fontFamily: "'Syne', sans-serif",
              fontSize: "18px", fontWeight: 700
            }}>
            <span>🆓 Complete Free Resources Directory</span>
            <span style={{ color: "#10B981" }}>{showResources ? "▲ Hide" : "▼ Expand"}</span>
          </button>

          {showResources && (
            <div style={{
              background: "#09090f", border: "1px solid #1a1a26",
              borderTop: "none", borderRadius: "0 0 12px 12px",
              padding: "24px",
              display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(260px, 1fr))",
              gap: "14px"
            }}>
              {freeResources.map(cat => (
                <div key={cat.category} className="resource-card">
                  <div style={{ fontSize: "11px", color: "#10B981", letterSpacing: "2px", fontWeight: 700, marginBottom: "12px" }}>
                    {cat.category.toUpperCase()}
                  </div>
                  <div style={{ display: "flex", flexDirection: "column", gap: "7px" }}>
                    {cat.tools.map(t => (
                      <div key={t} style={{ display: "flex", alignItems: "center", gap: "8px", fontSize: "12px", color: "#777" }}>
                        <span style={{ color: "#10B981", fontSize: "9px" }}>✓</span> {t}
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Final Banner */}
        <div style={{
          marginTop: "32px",
          background: "linear-gradient(135deg, #070710 0%, #0a0f0d 100%)",
          border: "1px solid #10B98130",
          borderRadius: "16px", padding: "40px 28px", textAlign: "center",
          position: "relative", overflow: "hidden"
        }}>
          <div style={{
            position: "absolute", inset: 0,
            background: "radial-gradient(ellipse at 50% 0%, rgba(16,185,129,0.06) 0%, transparent 70%)"
          }} />
          <div style={{ position: "relative", zIndex: 1 }}>
            <div style={{ fontSize: "36px", marginBottom: "14px" }}>🎓</div>
            <h3 style={{
              fontFamily: "'Syne', sans-serif",
              fontSize: "clamp(18px, 3vw, 26px)", fontWeight: 800,
              color: "#fff", marginBottom: "10px"
            }}>
              80 Hours. $0 Spent. Expert-Level AI Engineer.
            </h3>
            <p style={{ color: "#444", fontSize: "13px", marginBottom: "22px" }}>
              Everything you need is free and open source. No excuses. Start today.
            </p>
            <div style={{ display: "flex", justifyContent: "center", flexWrap: "wrap", gap: "8px" }}>
              {[
                "✓ Build & Deploy AI Apps",
                "✓ Local LLMs with Ollama",
                "✓ Autonomous AI Agents",
                "✓ Train Custom ML Models",
                "✓ Fine-tune Neural Networks",
                "✓ Generative AI from Scratch"
              ].map(item => (
                <div key={item} style={{
                  background: "#0f0f1a", border: "1px solid #1a1a26",
                  borderRadius: "6px", padding: "8px 14px",
                  fontSize: "12px", color: "#666"
                }}>
                  <span style={{ color: "#10B981" }}>{item.split(" ")[0]}</span> {item.split(" ").slice(1).join(" ")}
                </div>
              ))}
            </div>
            <p style={{ color: "#1e1e2e", fontSize: "10px", marginTop: "28px", letterSpacing: "2px" }}>
              OPEN SOURCE · COMMUNITY POWERED · FREE FOREVER
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
