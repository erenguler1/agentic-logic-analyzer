from langchain_core.tools import tool

@tool
def analyze_sr_latch(s: int, r: int, current_q: int) -> str:
    """Analyzes the next state of an Active-High SR Latch based on S, R, and current Q inputs."""
    if s == 0 and r == 0:
        return f"Memory State: Q remains {current_q}"
    elif s == 1 and r == 0:
        return "Set State: Q becomes 1"
    elif s == 0 and r == 1:
        return "Reset State: Q becomes 0"
    elif s == 1 and r == 1:
        return "Invalid State: Race condition, outputs are unpredictable."
    else:
        return "Invalid inputs. S and R must be 0 or 1."

# Agent'ın kullanabileceği araçlar listesi
TOOLS = [analyze_sr_latch]
