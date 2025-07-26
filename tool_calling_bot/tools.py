# tools.py

import math
from datetime import datetime
from dateutil import tz
import requests

def calculator_tool(expression: str) -> str:
    """
    Safely evaluate mathematical expressions.

    Args:
        expression (str): Math expression like "2 + 3 * 4" or "sqrt(16)"

    Returns:
        str: Calculation result or error message
    """
    try:
        # Use math.__dict__ for safe functions like sqrt, sin, etc.
        result = eval(expression, {"__builtins__": None}, math.__dict__)
        return f"Result: {result}"
    except Exception as e:
        return f"Invalid expression: {e}"

def get_current_time(timezone: str = "UTC") -> str:
    """
    Get current time in specified timezone.

    Args:
        timezone (str): Timezone string like "UTC", "US/Eastern", "Asia/Tokyo"

    Returns:
        str: Formatted time string or error message
    """
    try:
        target_zone = tz.gettz(timezone)
        if target_zone is None:
            raise ValueError("Unknown timezone.")
        now = datetime.now(target_zone)
        return now.strftime(f"%Y-%m-%d %H:%M:%S ({timezone})")
    except Exception as e:
        return f"Timezone error: {e}"

def web_search(query: str, num_results: int = 3) -> str:
    """
    Search the web using DuckDuckGo and return top results.

    Args:
        query (str): Search terms
        num_results (int): Number of results to return (1-5)

    Returns:
        str: Formatted string with top results or error message
    """
    try:
        if num_results < 1 or num_results > 5:
            return "Please request between 1 and 5 results."

        response = requests.get(
            "https://api.duckduckgo.com/",
            params={
                "q": query,
                "format": "json",
                "no_html": 1,
                "skip_disambig": 1
            }
        )
        data = response.json()
        results = []

        for topic in data.get("RelatedTopics", []):
            if "Text" in topic and "FirstURL" in topic:
                results.append(f"- {topic['Text']} ({topic['FirstURL']})")
                if len(results) == num_results:
                    break

        return "\n".join(results) if results else "No results found."

    except Exception as e:
        return f"Web search error: {e}"
