"""
Research Agent - Searches for relevant information about topics
"""
import os
import requests
from typing import List, Dict

class ResearchAgent:
    def __init__(self, model_name: str = "gpt-4"):
        """Initialize the Research Agent"""
        self.tavily_api_key = os.getenv("TAVILY_API_KEY")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    def research_topic(self, topic: str) -> Dict:
        """
        Research a given topic and return structured information
        
        Args:
            topic (str): The topic to research
            
        Returns:
            Dict: Structured research results
        """
        try:
            # Use Tavily for web search if available
            search_results = []
            if self.tavily_api_key:
                try:
                    url = "https://api.tavily.com/search"
                    headers = {"api-key": self.tavily_api_key, "content-type": "application/json"}
                    payload = {
                        "query": f"{topic} overview explanation guide tutorial",
                        "search_depth": "advanced",
                        "max_results": 5
                    }
                    
                    response = requests.post(url, headers=headers, json=payload)
                    response.raise_for_status()
                    data = response.json()
                    
                    if "results" in data:
                        for result in data["results"]:
                            search_results.append({
                                "title": result.get("title", ""),
                                "url": result.get("url", ""),
                                "content": result.get("content", "")
                            })
                except Exception as e:
                    print(f"⚠️ Tavily search failed: {e}")
            
            # Format research results
            research_text = ""
            if search_results:
                research_text = "Web Search Results:\n\n"
                for i, result in enumerate(search_results, 1):
                    research_text += f"{i}. {result['title']}\n"
                    research_text += f"   URL: {result['url']}\n"
                    research_text += f"   Content: {result['content'][:200]}...\n\n"
            else:
                research_text = "No web search results available."
            
            return {
                "topic": topic,
                "research_results": research_text,
                "sources": search_results,
                "status": "success"
            }
            
        except Exception as e:
            return {
                "topic": topic,
                "research_results": f"Error during research: {str(e)}",
                "sources": [],
                "status": "error"
            } 