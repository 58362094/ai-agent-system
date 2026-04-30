from agents.planner import PlannerAgent
from agents.retriever import RetrieverAgent
from agents.generator import GeneratorAgent
from agents.reviewer import ReviewerAgent
from agents.tester import TesterAgent

def main():
    task = "Refactor a Python function for better readability"

    planner = PlannerAgent()
    retriever = RetrieverAgent()
    generator = GeneratorAgent()
    reviewer = ReviewerAgent()
    tester = TesterAgent()

    plan = planner.run(task)
    context = retriever.run(plan)
    code = generator.run(context)
    reviewed = reviewer.run(code)
    result = tester.run(reviewed)

    print("Final Output:\n", result)

if __name__ == "__main__":
    main()
