# 🚀 MisinfoX — The WhatsApp Fact-Checking Bot

**MisinfoX** is an AI-powered WhatsApp bot designed to fight misinformation. Using the power of **Google Custom Search**, **Google Cloud Platform**and **Vertes AI**, it provides **quick, reliable, and concise fact-checks** for messages, forwarded content, and circulating claims directly within your chats.

-----

## ✨ Key Features

  * **Fact-Check Any Claim**: Just send `verify <your claim>` and get a detailed verdict with trusted sources.

  * **Automatic Forwarded Message Detection**: The bot intelligently detects long or chain messages, automatically checks them, and provides an instant verdict.

  * **User-Friendly Replies**: Replies are crafted to be concise and easy to understand on WhatsApp, with links to source materials for deeper dives.

  * **Interactive Commands**:

    \<comment-tag id="2"\>\* `hi` / `hello` → Get a friendly greeting.

      * `help` / `menu` → View a quick guide to all commands.

      * **Forwarded messages** → The bot automatically verifies the content for you.\</comment-tag id="2" text="The current formatting is a bit fragmented. Using a simple, consistent bulleted list can make the commands easier to read and understand at a glance.

Example:

  * **`hi` / `hello`**: Get a friendly greeting from the bot.
  * **`help` / `menu`**: View a quick guide to all available commands.
  * **Forwarded messages**: The bot automatically verifies the content for you." type="suggestion"\>

## 🎯 Live Demo

See **MisinfoX** in action\!

### 1\. Verifying a Direct Claim

**User:**

```
verify The earth is flat

```

**Bot:**

````
📰 Fact-check for: The earth is flat
Verdict: ❌ False
Explanation: The earth is spherical, a fact confirmed by NASA and numerous scientific sources.
Sources:
<comment-tag id="3">[https://www.nasa.gov](https://www.nasa.gov)
[https://www.scientificamerican.com/article/why-the-earth-is-round/](https://www.scientificamerican.com/article/why-the-earth-is-round/)

```</comment-tag id="3" text="The links in this code block are formatted as Markdown, but within a code block, they will not render correctly. For a 'live demo' that mimics what the bot actually sends, you should show the plain text links. This makes the demo more authentic.

Example:
Sources:
[https://www.nasa.gov](https://www.nasa.gov)
[https://www.scientificamerican.com/article/why-the-earth-is-round/](https://www.scientificamerican.com/article/why-the-earth-is-round/)" type="suggestion">

### 2. Checking a Forwarded Message

**User:** *forwards a long message about a recent event*

**Bot:**

````

📨 Detected forwarded/long message — quick check:

📰 Fact-check for: \<forwarded message text\>
Verdict: ⚠️ Misleading
Explanation: Some claims in this message are inaccurate based on verified sources.
Sources:

\<link 1\>
\<link 2\>

```

## 🛠️ Installation

Get **MisinfoX** up and running on your system in just a few steps.

### 1. Clone the repository

```

git clone https://github.com/RajveerSinghBisht/misinfox-whatsapp-bot
cd misinfox

```

### 2. Create a virtual environment

```

python3 -m venv venv

# On macOS/Linux

source venv/bin/activate

# On Windows

venv\\Scripts\\activate

```

### 3. Install dependencies

```

pip install -r requirements.txt

```

### 4. Set up environment variables

<comment-tag id="4">Create a `.env` file in the project's root directory and add your API keys.

```

GOOGLE\_API\_KEY=\<your\_google\_api\_key\>
GOOGLE\_CX=\<your\_google\_custom\_search\_cx\>
GEMINI\_API\_KEY=\<your\_gemini\_api\_key\>

```

**Note**: You'll need a Google API Key and Custom Search CX for searching, and a Gemini API Key for the AI-powered verdicts and message formatting.</comment-tag id="4" text="The note about the API keys is very important but currently blends in with the rest of the text. To draw more attention and make it more scannable, you can combine this into a single, emphasized paragraph or list item.

Example:
**Important: Set up your environment variables**
Create a `.env` file in the root directory with your API keys. You will need a Google API Key and Custom Search CX for searching, and a Gemini API Key for the AI-powered verdicts.
`GOOGLE_API_KEY=<your_google_api_key>`
`GOOGLE_CX=<your_google_custom_search_cx>`
`GEMINI_API_KEY=<your_gemini_api_key>`" type="suggestion">

### 5. Run locally for testing

```

flask run

```

The bot will now accept POST requests from your Twilio WhatsApp sandbox.

## 📱 Twilio Setup

To connect the bot to WhatsApp, you'll need a **Twilio account** and to activate the **WhatsApp sandbox**. Configure your Twilio webhook URL to point to your deployed function or local tunnel (e.g., using `ngrok`). Once set up, send a message to your sandbox number to test the bot.

## ⚙️ How It Works

<comment-tag id="5">1. A user sends a WhatsApp message to the bot.

2. The bot's logic in `main.py` checks the message content.

3. If the message is a greeting or a command like `help`, it responds accordingly.

4. If the message starts with `verify` or is a long, forwarded message, the bot:

   * Uses **Google Custom Search** to find relevant information.

   * Feeds the search results to **Gemini AI** to get a concise verdict and explanation.

   * Formats a user-friendly response with links to sources.

5. The bot sends the clean, concise response back to the user.</comment-tag id="5" text="The current numbered list is functional but could be more descriptive and engaging. Rephrasing it into more narrative steps can make the process clearer and more impressive to potential users and contributors.

Example:
1.  **Incoming Message:** The bot receives a message from a user.
2.  **Command Detection:** The bot's logic in `main.py` checks for specific commands (`verify`, `help`, etc.) or detects if it is a forwarded/long message.
3.  **Fact-Checking Process:** For fact-checking, the bot uses **Google Custom Search** to find relevant information.
4.  **AI-Powered Verdict:** The search results are then fed to **Gemini AI**, which processes the information to create a concise verdict and a clear explanation.
5.  **Instant Response:** The bot formats a user-friendly response with sources and sends it back to the user on WhatsApp." type="suggestion">

## ⚠️ Important Notes

* **MisinfoX** provides automated guidance; always cross-check critical claims with trusted sources.

* The bot requires an active internet connection to function.

* While designed for WhatsApp, the core logic can be adapted for other messaging platforms.

## 📝 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

## 👨‍💻 Author

**Rajveer Singh Bisht** — Creator of MisinfoX
*Suggestions added*
```
