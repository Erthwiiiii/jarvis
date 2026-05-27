try:
    from duckduckgo_search import DDGS
except Exception:
    DDGS = None


def web_search(query):

    results = []

    if DDGS is not None:

        try:
            with DDGS() as ddgs:

                data = ddgs.text(query, max_results=5)

                for r in data:

                    results.append(f"• {r.get('title', 'No title')}")

            return "\n".join(results)

        except Exception:
            pass

    # Fallback when duckduckgo_search isn't available or fails
    return "Search service unavailable. Install 'duckduckgo_search' or check internet connection."
