# MisinfoX WhatsApp Bot

AI-powered WhatsApp bot to detect and explain misinformation.

flowchart TD

A[User on WhatsApp] --> B[Twilio API / WhatsApp Business API]
B --> C[Backend Service (Cloud Function)]

C --> D[Pre-Processing Module]
D --> D1[Detect Forwarded]
D --> D2[Language Detection]
D --> D3[Classification: News / Myth / Scam]

C --> E[Claim Detection (NLP)]

C --> F[Verification Engine]
F --> F1[Google Search / APIs]
F --> F2[RAG + Fact-check DBs]
F --> F3[Govt/Trusted Portals]

C --> G[AI Analysis (LLM)]
G --> G1[Evaluate Claim]
G --> G2[Explain Why True/False/Misleading]

C --> H[Output Generator]
H --> H1[Corrective Reply]
H --> H2[Trusted Sources]
H --> H3[Explanation]

H --> I[User Response via WhatsApp]

I --> J[Admin Dashboard]
J --> J1[Firestore/BigQuery]
J --> J2[Trends & Reports]
