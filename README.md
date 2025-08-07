# 🤖 AI Research Topic Explainer

An intelligent system that uses multiple AI agents to research, summarize, visualize, and create educational materials for any technical topic.

## 🎯 What It Does

This project demonstrates **Agentic AI** by coordinating 4 specialized AI agents that work together to create comprehensive study guides:

1. **🔍 Research Agent** - Searches the web for authoritative sources
2. **📝 Summarizer Agent** - Condenses information into clear summaries
3. **🎨 Visualizer Agent** - Creates diagrams and visual representations
4. **📚 Tutor Agent** - Generates flashcards, quizzes, and educational materials

## 🏗️ Architecture

```
User Input → Research Agent → Summarizer Agent → Visualizer Agent → Tutor Agent → Study Guide
```

### Agent Responsibilities

| Agent | Role | Output |
|-------|------|--------|
| **Research Agent** | Web search & information gathering | Raw research data from multiple sources |
| **Summarizer Agent** | Information condensation | Structured summaries with key concepts |
| **Visualizer Agent** | Diagram creation | Mermaid diagrams (flowcharts, mind maps) |
| **Tutor Agent** | Educational content | Flashcards, MCQs, learning objectives |

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up API Keys

Create a `.env` file with your API keys:

```env
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

**Required APIs:**
- **OpenAI API**: For LLM interactions (GPT-4 recommended)
- **Tavily API**: For web search (free tier available)

### 3. Run the System

```bash
python cli.py
```

### 4. Example Usage

```
🔍 Enter a topic to research: Retrieval-Augmented Generation (RAG)

🚀 Starting research on: Retrieval-Augmented Generation (RAG)
📚 Step 1: Researching topic...
📝 Step 2: Summarizing research...
🎨 Step 3: Creating visual diagrams...
📖 Step 4: Creating educational materials...

✅ Research completed successfully!
```

## 📁 Project Structure

```
ai_research_explainer/
├── agents/                    # AI Agent modules
│   ├── __init__.py
│   ├── research_agent.py      # Web search and research
│   ├── summarizer_agent.py    # Information summarization
│   ├── visualizer_agent.py    # Diagram generation
│   └── tutor_agent.py         # Educational materials
├── research_explainer.py      # Main orchestrator
├── cli.py                     # Command-line interface
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── results/                   # Generated study guides (created automatically)
```

## 🔧 How It Works

### Step 1: Research Phase
The **Research Agent** uses Tavily search to find:
- Academic papers and research
- Official documentation
- Reputable blog posts and articles
- Recent developments and trends

### Step 2: Summarization Phase
The **Summarizer Agent** processes the research to create:
- Clear overview of the topic
- Key concepts and definitions
- How it works (technical explanation)
- Real-world applications
- Related topics and technologies

### Step 3: Visualization Phase
The **Visualizer Agent** creates Mermaid diagrams:
- Process flowcharts
- Component diagrams
- Concept mind maps
- Architecture visualizations

### Step 4: Educational Phase
The **Tutor Agent** generates learning materials:
- Flashcards with Q&A
- Multiple-choice questions with explanations
- Key terms glossary
- Learning objectives
- Further learning resources

## 📊 Output Format

The system generates two types of files:

### 1. JSON Results (`results/topic_timestamp.json`)
Complete structured data including:
- Raw research results
- Structured summaries
- Diagram Mermaid code
- Educational materials

### 2. Markdown Study Guide (`results/topic_timestamp.md`)
Formatted study guide with:
- Overview and key concepts
- Technical explanations
- Visual diagrams
- Flashcards and quizzes
- Learning objectives

## 🎨 Example Output

### Study Guide Structure
```markdown
# 📚 Study Guide: Retrieval-Augmented Generation (RAG)

## 🔍 Overview
RAG combines external knowledge with LLM inference...

## 🧠 Key Concepts
- Vector embeddings
- Document retrieval
- Context injection
- Response generation

## ⚙️ How It Works
1. User query is processed
2. Relevant documents are retrieved
3. Context is injected into LLM
4. Response is generated

## 🖼️ Visual Diagrams
[Process flowcharts and component diagrams]

## 📖 Educational Materials
[Flashcards, MCQs, and learning resources]
```

## 🔍 Supported Topics

The system works with any technical topic, including:
- **AI/ML Concepts**: RAG, Transformers, Neural Networks
- **Programming**: Design Patterns, Algorithms, Frameworks
- **Technology**: Blockchain, Cloud Computing, APIs
- **Scientific Concepts**: Quantum Computing, Bioinformatics
- **And much more!**

## 🛠️ Customization

### Adding New Agents
1. Create a new agent class in `agents/`
2. Implement the required interface
3. Add it to the orchestrator in `research_explainer.py`

### Modifying Agent Behavior
Each agent can be customized by:
- Changing the system prompts
- Adjusting temperature settings
- Adding new tools and capabilities
- Modifying output formats

### Using Different Models
Change the model in the constructor:
```python
explainer = AIResearchExplainer(model_name="gpt-3.5-turbo")
```

## 🚧 Limitations & Considerations

- **API Costs**: Each research session uses multiple API calls
- **Search Quality**: Depends on available web sources
- **Processing Time**: Full research takes 2-5 minutes
- **Content Accuracy**: Verify generated content for critical applications

## 🔮 Future Enhancements

- **Web UI**: Streamlit interface for better user experience
- **PDF Export**: Direct PDF generation of study guides
- **Audio Explanations**: Text-to-speech for accessibility
- **Interactive Diagrams**: Clickable Mermaid diagrams
- **Multi-language Support**: Research in different languages
- **Custom Knowledge Bases**: Integration with private documents

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **LangChain**: For the agent framework
- **CrewAI**: For multi-agent coordination concepts
- **OpenAI**: For powerful LLM capabilities
- **Tavily**: For web search functionality

---

**Built with ❤️ to make learning technical topics easier and more engaging!** 