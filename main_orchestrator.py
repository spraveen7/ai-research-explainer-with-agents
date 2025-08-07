"""
Main Orchestrator - Coordinates 4 Agents using CrewAI
"""
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from agents.research_agent import ResearchAgent
from agents.summarizer_agent import SummarizerAgent
from agents.visualizer_agent import VisualizerAgent
from agents.tutor_agent import TutorAgent

# Load environment variables
load_dotenv()

class AIResearchOrchestrator:
    def __init__(self):
        """Initialize the 4-agent orchestrator"""
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.tavily_api_key = os.getenv("TAVILY_API_KEY")
        
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        print("🤖 4-Agent AI Research Orchestrator Initialized!")
    
    def create_agents(self):
        """Create the 4 specialized agents"""
        
        # Agent 1: Research Agent
        research_agent = Agent(
            role='Research Specialist',
            goal='Find comprehensive, accurate information about technical topics',
            backstory="""You are an expert research specialist with years of experience 
            in finding high-quality information about technical topics. You excel at 
            identifying authoritative sources, academic papers, and recent developments.""",
            verbose=True,
            allow_delegation=False,
            tools=[],  # Will use Tavily search
            llm_model="gpt-4"
        )
        
        # Agent 2: Summarizer Agent
        summarizer_agent = Agent(
            role='Content Summarizer',
            goal='Create clear, structured summaries of complex technical information',
            backstory="""You are a skilled content analyst who excels at breaking down 
            complex technical concepts into clear, structured summaries. You have a 
            talent for organizing information logically and making it accessible.""",
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm_model="gpt-4"
        )
        
        # Agent 3: Visualizer Agent
        visualizer_agent = Agent(
            role='Visual Content Creator',
            goal='Create clear diagrams and visual representations of technical concepts',
            backstory="""You are a visual communication expert who specializes in 
            creating diagrams, flowcharts, and visual representations of technical 
            concepts. You excel at making complex ideas easy to understand visually.""",
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm_model="gpt-4"
        )
        
        # Agent 4: Tutor Agent
        tutor_agent = Agent(
            role='Educational Content Creator',
            goal='Create engaging educational materials like flashcards and quizzes',
            backstory="""You are an experienced educator who knows how to create 
            engaging learning materials. You excel at designing flashcards, quizzes, 
            and other educational content that helps people learn effectively.""",
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm_model="gpt-4"
        )
        
        return research_agent, summarizer_agent, visualizer_agent, tutor_agent
    
    def create_tasks(self, topic: str, research_agent, summarizer_agent, visualizer_agent, tutor_agent):
        """Create the sequential tasks for the agents"""
        
        # Task 1: Research
        research_task = Task(
            description=f"""
            Research the topic: {topic}
            
            Find comprehensive information including:
            1. Key definitions and concepts
            2. How it works (technical details)
            3. Real-world applications and examples
            4. Recent developments and trends
            5. Related technologies or concepts
            
            Use web search to find authoritative sources, academic papers, 
            and recent information about this topic.
            
            Provide detailed, well-sourced information that can be used by 
            other agents to create summaries, diagrams, and educational materials.
            """,
            agent=research_agent,
            expected_output="Comprehensive research findings with sources and detailed information about the topic"
        )
        
        # Task 2: Summarize
        summarize_task = Task(
            description=f"""
            Based on the research findings about {topic}, create a structured summary.
            
            Organize the information into:
            1. **Overview**: Clear introduction to the topic
            2. **Key Concepts**: Main ideas and definitions
            3. **How It Works**: Technical explanation
            4. **Applications**: Real-world uses and examples
            5. **Related Topics**: Connected concepts or technologies
            
            Make the summary beginner-friendly but accurate and comprehensive.
            Focus on clarity and logical organization.
            """,
            agent=summarizer_agent,
            expected_output="Structured summary with clear sections covering all aspects of the topic",
            context=[research_task]
        )
        
        # Task 3: Visualize
        visualize_task = Task(
            description=f"""
            Based on the summary of {topic}, create visual diagrams.
            
            Create these diagrams in Mermaid syntax:
            1. **Process Flowchart**: Show how the main process works
            2. **Component Diagram**: Show key components and relationships
            3. **Concept Mind Map**: Show related concepts and their connections
            
            Make the diagrams:
            - Clear and easy to understand
            - Educational and informative
            - Well-structured and professional
            
            Format each diagram with proper Mermaid syntax.
            """,
            agent=visualizer_agent,
            expected_output="Multiple Mermaid diagrams showing different aspects of the topic",
            context=[summarize_task]
        )
        
        # Task 4: Create Educational Materials
        tutor_task = Task(
            description=f"""
            Based on the summary of {topic}, create educational materials.
            
            Create:
            1. **Flashcards** (5 cards): Q&A format covering key concepts
            2. **Multiple Choice Questions** (3 questions): With explanations for each option
            3. **Key Terms Glossary**: Important vocabulary with clear definitions
            4. **Learning Objectives**: What someone should understand after studying this topic
            5. **Further Learning Resources**: Suggested next steps for deeper understanding
            
            Make the materials:
            - Engaging and educational
            - Appropriate for beginners
            - Comprehensive but not overwhelming
            """,
            agent=tutor_agent,
            expected_output="Complete set of educational materials including flashcards, quizzes, and learning resources",
            context=[summarize_task]
        )
        
        return research_task, summarize_task, visualize_task, tutor_task
    
    def explain_topic(self, topic: str):
        """
        Execute the 4-agent workflow to explain a topic
        
        Args:
            topic (str): The topic to research and explain
            
        Returns:
            dict: Complete explanation with all components
        """
        print(f"🚀 Starting 4-agent research on: {topic}")
        
        # Create agents
        research_agent, summarizer_agent, visualizer_agent, tutor_agent = self.create_agents()
        
        # Create tasks
        research_task, summarize_task, visualize_task, tutor_task = self.create_tasks(
            topic, research_agent, summarizer_agent, visualizer_agent, tutor_agent
        )
        
        # Create crew
        crew = Crew(
            agents=[research_agent, summarizer_agent, visualizer_agent, tutor_agent],
            tasks=[research_task, summarize_task, visualize_task, tutor_task],
            verbose=True
        )
        
        # Execute the workflow - simple and fast
        result = crew.kickoff()
        
        return {
            "topic": topic,
            "research": str(result),
            "summary": str(result),
            "diagrams": str(result),
            "educational_materials": str(result)
        }

def main():
    """Main function to test the 4-agent orchestrator"""
    print("🤖 AI Research Topic Explainer - 4-Agent System")
    print("=" * 60)
    
    try:
        # Initialize the orchestrator
        orchestrator = AIResearchOrchestrator()
        
        # Get topic from user
        topic = input("🔍 Enter a topic to research: ").strip()
        
        if topic:
            # Execute the 4-agent workflow
            result = orchestrator.explain_topic(topic)
            
            print("\n" + "=" * 60)
            print("✅ 4-Agent Research Complete!")
            print("=" * 60)
            
            print(f"\n📚 Topic: {result['topic']}")
            print(f"\n🔍 Research:")
            print(result['research'][:500] + "..." if len(result['research']) > 500 else result['research'])
            
            print(f"\n📝 Summary:")
            print(result['summary'][:500] + "..." if len(result['summary']) > 500 else result['summary'])
            
            print(f"\n🎨 Diagrams:")
            print(result['diagrams'][:300] + "..." if len(result['diagrams']) > 300 else result['diagrams'])
            
            print(f"\n📖 Educational Materials:")
            print(result['educational_materials'][:500] + "..." if len(result['educational_materials']) > 500 else result['educational_materials'])
            
        else:
            print("❌ Please enter a valid topic")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main() 