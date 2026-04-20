# 🤖 AI in Manufacturing: Why LLMs Fail

Software Architektur im Stream's latest episode is about  **industrial AI architecture** with Nikita Golovko from Siemens, and it gives great insights into how AI is being used successfully for these demanding applications.

Here are the main points:

**LLMs are probabilistic text generators — not decision engines.** In factories where a single wrong call stops production lines worth millions, "probably correct" isn't good enough. You need *guaranteed determinism*.

**Key takeaways from our conversation:**

🔴 Why LLMs fail in industrial settings:
- They can't guarantee reproducible results
- Silent drift happens without alerts
- They're fundamentally incompatible with deterministic requirements

✅ What actually works:
- **Classical ML models** (decision trees, random forests) → interpretable & auditable
- **Computer vision models** → defect detection with human validation loops
- **Simplex architecture** → AI + deterministic fallback + human oversight
- **Hexagonal architecture** → isolate AI as a replaceable component

💡 As a bonus: An **arc42 extension for AI** and suggestions how to provide transparency to model governance — exactly what you need for AI Act compliance by 2026.

**The main idea?** Treat AI components like other system dependency: abstract them behind ports, version them carefully, monitor inputs & confidence scores, and *always* have a fallback when the model doubts itself.

This isn't about avoiding AI. It's about engineering it properly from day one.

🎙️ Full episode: https://software-architektur.tv/2026/04/17/episode310.html (video / podcast).
