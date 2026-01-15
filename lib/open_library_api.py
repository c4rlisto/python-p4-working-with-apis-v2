import requests
import json


class Search:

    def get_search_results(self):
        search_term = "the lord of the rings"

        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = (
            f"https://openlibrary.org/search.json?"
            f"title={search_term_formatted}&"
            f"fields={fields_formatted}&"
            f"limit={limit}"
        )

        response = requests.get(URL)
        return response.content

    def get_search_results_json(self):
        search_term = "the lord of the rings"

        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = (
            f"https://openlibrary.org/search.json?"
            f"title={search_term_formatted}&"
            f"fields={fields_formatted}&"
            f"limit={limit}"
        )

        response = requests.get(URL)
        return response.json()

    def get_user_search_results(self, search_term):
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = (
            f"https://openlibrary.org/search.json?"
            f"title={search_term_formatted}&"
            f"fields={fields_formatted}&"
            f"limit={limit}"
        )

        response = requests.get(URL).json()

        title = response["docs"][0]["title"]
        author = response["docs"][0]["author_name"][0]

        return f"Title: {title}\nAuthor: {author}"


# Uncomment to test static search
# results = Search().get_search_results()
# print(results)

# Uncomment to test JSON output
# results_json = Search().get_search_results_json()
# print(json.dumps(results_json, indent=2))


# User input search
search_term = input("Enter a book title: ")
result = Search().get_user_search_results(search_term)
print("\nSearch Result:\n")
print(result)

