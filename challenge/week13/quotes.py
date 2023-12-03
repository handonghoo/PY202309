import requests
import bs4

def get_text(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    return text

def get_word_counts(text):
    word_counts = {}
    for word in text.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def get_top_5_words(word_counts):
    top_5_words = []
    for word, count in word_counts.items():
        top_5_words.append((count, word))
    top_5_words.sort(key=lambda x: x[0], reverse=True)
    return top_5_words[:5]

if __name__ == "__main__":
    url = "https://quotes.toscrape.com/tag/life/"
    text = get_text(url)
    word_counts = get_word_counts(text)
    top_5_words = get_top_5_words(word_counts)
    for count, word in top_5_words:
        print(f"{count:>5} {word}")
