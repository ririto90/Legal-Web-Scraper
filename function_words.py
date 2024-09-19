
conjunctions = [
    "and", "but", "for", "nor", "or", "so", "yet", "after", "although", "as",
    "because", "before", "even if", "even though", "if", "in order that",
    "lest", "once", "provided that", "since", "so that", "though", "till",
    "unless", "until", "when", "whenever", "where", "wherever", "while"
]

articles = ["a", "an", "the"]

prepositions = [
    "aboard", "about", "above", "across", "after", "against", "along", "amid", "among",
    "around", "as", "at", "before", "behind", "below", "beneath", "beside", "between",
    "beyond", "by", "down", "during", "for", "from", "in", "inside", "into", "like",
    "near", "of", "off", "on", "onto", "out", "outside", "over", "past", "since",
    "through", "to", "toward", "under", "underneath", "until", "up", "upon", "with",
    "within", "without"
]

pronouns = [
    "I", "me", "we", "us", "you", "he", "him", "she", "her", "it", "they", "them",
    "myself", "yourself", "himself", "herself", "itself", "ourselves", "yourselves", "themselves",
    "this", "that", "these", "those", "who", "whom", "whose", "which", "what", "whatever",
    "whoever", "whomever", "whichever"
]

auxiliary_verbs = [
    "am", "is", "are", "was", "were", "being", "been", "be", "have", "has", "had",
    "having", "do", "does", "did", "will", "would", "shall", "should", "may", "might",
    "must", "can", "could"
]

determiners = [
    "the", "a", "an", "this", "that", "these", "those", "my", "your", "his", "her",
    "its", "our", "their", "some", "any", "no", "every", "each", "either", "neither",
    "much", "many", "more", "most", "few", "fewer", "least", "several", "enough", "all",
    "both", "half", "one", "two", "three", "four", "five", "many", "several", "numerous", "every"
]

function_words = conjunctions + articles + prepositions + pronouns + auxiliary_verbs + determiners
unique_function_words = set(function_words)

print(len(function_words), len(unique_function_words))


