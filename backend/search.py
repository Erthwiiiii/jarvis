from duckduckgo_search import DDGS

def web_search(query):

    results = []

    with DDGS() as ddgs:

        data = ddgs.text(query, max_results=5)

        for r in data:

            results.append(
                f"• {r['title']}"
            )

    return "\n".join(results)
