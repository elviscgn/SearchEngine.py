# Mini Search Engine

For this project you will be building a very small in-memory search engine using python and classes.

I have already written test cases and your job is to write code that satisfies those test cases.

## Learning objectives
This project is meant to help you practice
1. Classes and instance variables
2. Dictionaries and how you can use them to map words to a document ID
3. Sets for storing unique document ids (this is a clue on how to solve this)
4. Loops and Sorting
5. Unit tests


## Example Usage

```
engine = SearchEngine()

# Registering websites
# engine.add(document_id: int, text: str) -> None
engine.add(1, "Explore the hidden trails in the Drakensberg mountains")
engine.add(2, "Join us for a weekend braai in Johannesburg with friends")
engine.add(3, "Discover Table Mountain and the beaches of Cape Town")
engine.add(4, "Listen to Kwaito and Afrobeat music on SA Radio")
engine.add(5, "Braais and live music make Durban weekends special")

# Single word search examples
# engine.search(search_word: str) -> List[Document ids]
engine.search("braai")        # [2, 5]      <- rmultiple matches
engine.search("music")        # [4, 5]      <- multiple matches
engine.search("durban")       # [5]         <- single match
engine.search("cape")         # [3]         <- singe match
engine.search("weekend")      # [2, 5]      <- multiple matches
engine.search("johannesburg") # [2]         <- single match
engine.search("kwaito")       # [4]         <- single match
engine.search("soccer")       # []          <- no match
```


## Notes
- Search queries only contain one word for now
- Matching is case-insenstive
- Ignore punctuations for now
- Only exact matches count (altho your next exercise for this is how you're handle search queries that are very similar or have typos eg (durbon -> durban; brai -> braai; johhanesburg -> johannesburg)
- If no documents match return empty list
