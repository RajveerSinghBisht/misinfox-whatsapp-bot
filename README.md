<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MisinfoX — WhatsApp Fact-Checking Bot</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f3f4f6;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }
        .code-block {
            background-color: #2d3748;
            color: #e2e8f0;
            padding: 1rem;
            border-radius: 0.5rem;
            overflow-x: auto;
            font-family: monospace;
            white-space: pre-wrap;
            word-break: break-all;
        }
        .highlight {
            background-color: #6366f1;
            color: #ffffff;
            font-weight: 600;
            padding: 0.2rem 0.5rem;
            border-radius: 0.375rem;
            display: inline-block;
        }
        .download-btn {
            background-color: #2563eb;
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 9999px;
            font-weight: 600;
            transition: all 0.2s;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            text-decoration: none;
            display: inline-block;
        }
        .download-btn:hover {
            background-color: #1e40af;
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
        }
        .emoji {
            font-size: 1.25rem;
            vertical-align: middle;
            margin-right: 0.5rem;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">

    <div class="container bg-white rounded-lg shadow-lg mt-10 mb-10 p-8">

        <header class="text-center mb-10">
            <h1 class="text-4xl sm:text-5xl font-extrabold text-gray-900 leading-tight">
                <span class="emoji">🚀</span> MisinfoX — The WhatsApp Fact-Checking Bot
            </h1>
            <p class="text-lg text-gray-600 mt-4 max-w-2xl mx-auto">
                **MisinfoX** is an AI-powered WhatsApp bot that automatically verifies messages, forwarded content, and circulating claims. Using <span class="highlight">Google Custom Search</span> and <span class="highlight">Google Gemini AI</span>, it provides **quick, reliable, and concise fact-checks**, making it easy to spot misinformation.
            </p>
            <div class="mt-8">
                <button id="download-button" class="download-btn">
                    Download this README
                </button>
            </div>
        </header>

        <hr class="my-10 border-gray-200">

        <section class="mb-10">
            <h2 class="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                <span class="emoji">✨</span> Key Features
            </h2>
            <ul class="list-none space-y-4 text-gray-700 text-lg">
                <li class="flex items-start">
                    <span class="emoji mr-2">✅</span> 
                    <div>
                        <strong class="text-gray-900">Fact-Check Any Claim</strong>: Send `verify <your claim>` and get a detailed verdict with trusted sources.
                    </div>
                </li>
                <li class="flex items-start">
                    <span class="emoji mr-2">📨</span> 
                    <div>
                        <strong class="text-gray-900">Automatic Forwarded Message Detection</strong>: The bot intelligently detects long or chain messages, automatically checks them, and provides an instant verdict.
                    </div>
                </li>
                <li class="flex items-start">
                    <span class="emoji mr-2">📝</span> 
                    <div>
                        <strong class="text-gray-900">User-Friendly Replies</strong>: Replies are crafted to be concise and easy to understand on WhatsApp, with links to source materials for deeper dives.
                    </div>
                </li>
                <li class="flex items-start">
                    <span class="emoji mr-2">🖥️</span> 
                    <div>
                        <strong class="text-gray-900">Interactive Commands</strong>:
                        <ul class="list-disc list-inside mt-2 text-base">
                            <li>`<span class="font-mono">hi</span>` / `<span class="font-mono">hello</span>` → Get a friendly greeting.</li>
                            <li>`<span class="font-mono">help</span>` / `<span class="font-mono">menu</span>` → View a quick guide to all commands.</li>
                            <li>**Forwarded messages** → The bot automatically verifies the content for you.</li>
                        </ul>
                    </div>
                </li>
            </ul>
        </section>

        <hr class="my-10 border-gray-200">

        <section class="mb-10">
            <h2 class="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                <span class="emoji">🎯</span> Live Demo
            </h2>
            <p class="text-lg text-gray-700 mb-6">See **MisinfoX** in action!</p>

            <h3 class="text-2xl font-semibold text-gray-900 mb-4">1. Verifying a Direct Claim</h3>
            <div class="bg-gray-100 p-6 rounded-lg mb-6">
                <p class="font-bold text-gray-900 mb-2">User:</p>
                <div class="code-block mb-4">
                    verify The earth is flat
                </div>
                <p class="font-bold text-gray-900 mb-2">Bot:</p>
                <div class="code-block">
                    📰 Fact-check for: The earth is flat<br>
                    Verdict: ❌ False<br>
                    Explanation: The earth is spherical, a fact confirmed by NASA and numerous scientific sources.<br>
                    Sources:<br>
                    https://www.nasa.gov<br>
                    https://www.scientificamerican.com/article/why-the-earth-is-round/
                </div>
            </div>

            <h3 class="text-2xl font-semibold text-gray-900 mb-4">2. Checking a Forwarded Message</h3>
            <div class="bg-gray-100 p-6 rounded-lg">
                <p class="font-bold text-gray-900 mb-2">User: <span class="text-gray-600 italic">*forwards a long message about a recent event*</span></p>
                <p class="font-bold text-gray-900 mb-2">Bot:</p>
                <div class="code-block">
                    📨 Detected forwarded/long message — quick check:<br><br>
                    📰 Fact-check for: &lt;forwarded message text&gt;<br>
                    Verdict: ⚠️ Misleading<br>
                    Explanation: Some claims in this message are inaccurate based on verified sources.<br>
                    Sources:<br>
                    &lt;link 1&gt;<br>
                    &lt;link 2&gt;
                </div>
            </div>
        </section>

        <hr class="my-10 border-gray-200">

        <section class="mb-10">
            <h2 class="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                <span class="emoji">🛠️</span> Installation
            </h2>
            <p class="text-lg text-gray-700 mb-6">
                Get **MisinfoX** up and running on your system in just a few steps.
            </p>

            <ol class="list-decimal list-inside space-y-6 text-lg text-gray-700">
                <li>
                    <strong class="text-gray-900">Clone the repository</strong>
                    <div class="code-block mt-2">
                        git clone https://github.com/&lt;your-username&gt;/misinfox.git<br>
                        cd misinfox
                    </div>
                </li>
                <li>
                    <strong class="text-gray-900">Create a virtual environment</strong>
                    <div class="code-block mt-2">
                        python3 -m venv venv<br>
                        # On macOS/Linux<br>
                        source venv/bin/activate<br>
                        # On Windows<br>
                        venv\Scripts\activate
                    </div>
                </li>
                <li>
                    <strong class="text-gray-900">Install dependencies</strong>
                    <div class="code-block mt-2">
                        pip install -r requirements.txt
                    </div>
                </li>
                <li>
                    <strong class="text-gray-900">Set up environment variables</strong>
                    <p class="text-base text-gray-600 mt-2">
                        Create a `.env` file in the project's root directory and add your API keys.
                    </p>
                    <div class="code-block mt-2">
                        GOOGLE_API_KEY=&lt;your_google_api_key&gt;<br>
                        GOOGLE_CX=&lt;your_google_custom_search_cx&gt;<br>
                        GEMINI_API_KEY=&lt;your_gemini_api_key&gt;
                    </div>
                    <p class="text-base text-gray-600 mt-2">
                        <strong class="font-bold">Note</strong>: You'll need a Google API Key and Custom Search CX for searching, and a Gemini API Key for the AI-powered verdicts and message formatting.
                    </p>
                </li>
                <li>
                    <strong class="text-gray-900">Run locally for testing</strong>
                    <div class="code-block mt-2">
                        flask run
                    </div>
                    <p class="text-base text-gray-600 mt-2">
                        The bot will now accept POST requests from your Twilio WhatsApp sandbox.
                    </p>
                </li>
            </ol>
        </section>

        <hr class="my-10 border-gray-200">

        <section class="mb-10">
            <h2 class="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                <span class="emoji">📱</span> Twilio Setup
            </h2>
            <p class="text-lg text-gray-700">
                To connect the bot to WhatsApp, you'll need a **Twilio account** and to activate the **WhatsApp sandbox**. Configure your Twilio webhook URL to point to your deployed function or local tunnel (e.g., using `ngrok`). Once set up, send a message to your sandbox number to test the bot.
            </p>
        </section>

        <hr class="my-10 border-gray-200">

        <section class="mb-10">
            <h2 class="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                <span class="emoji">⚙️</span> How It Works
            </h2>
            <ol class="list-decimal list-inside space-y-4 text-lg text-gray-700">
                <li>A user sends a WhatsApp message to the bot.</li>
                <li>The bot's logic in `<span class="font-mono">main.py</span>` checks the message content.</li>
                <li>If the message is a greeting or a command like `<span class="font-mono">help</span>`, it responds accordingly.</li>
                <li>If the message starts with `<span class="font-mono">verify</span>` or is a long, forwarded message, the bot:
                    <ul class="list-disc list-inside mt-2 text-base ml-4 space-y-2">
                        <li>Uses **Google Custom Search** to find relevant information.</li>
                        <li>Feeds the search results to **Gemini AI** to get a concise verdict and explanation.</li>
                        <li>Formats a user-friendly response with links to sources.</li>
                    </ul>
                </li>
                <li>The bot sends the clean, concise response back to the user.</li>
            </ol>
        </section>

        <hr class="my-10 border-gray-200">

        <section class="mb-10">
            <h2 class="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                <span class="emoji">⚠️</span> Important Notes
            </h2>
            <ul class="list-disc list-inside space-y-4 text-lg text-gray-700">
                <li>**MisinfoX** provides automated guidance; always cross-check critical claims with trusted sources.</li>
                <li>The bot requires an active internet connection to function.</li>
                <li>While designed for WhatsApp, the core logic can be adapted for other messaging platforms.</li>
            </ul>
        </section>

        <hr class="my-10 border-gray-200">

        <section class="mb-10">
            <h2 class="text-3xl font-bold text-gray-900 mb-6 flex items-center">
                <span class="emoji">📝</span> License
            </h2>
            <p class="text-lg text-gray-700">
                This project is licensed under the **MIT License**. See the `LICENSE` file for details.
            </p>
        </section>

        <hr class="my-10 border-gray-200">

        <footer class="text-center text-gray-600 mb-10">
            <h2 class="text-3xl font-bold text-gray-900 mb-4 flex items-center justify-center">
                <span class="emoji">👨‍💻</span> Author
            </h2>
            <p class="text-lg">
                **Rajveer Singh Bisht** — Creator of MisinfoX
            </p>
        </footer>

    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const downloadButton = document.getElementById('download-button');
            downloadButton.addEventListener('click', () => {
                const htmlContent = document.documentElement.outerHTML;
                const blob = new Blob([htmlContent], { type: 'text/html' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'MisinfoX_README.html';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
            });
        });
    </script>

</body>
</html>
