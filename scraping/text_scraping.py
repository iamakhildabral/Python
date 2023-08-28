import requests
from bs4 import BeautifulSoup

url = "https://news.google.com/articles/CBMiqwFodHRwczovL3d3dy5tb25leWNvbnRyb2wuY29tL25ld3MvbG9rLXNhYmhhLWVsZWN0aW9ucy9ianAtbWF5LWdvLWZvci1sb2stc2FiaGEtcG9sbHMtaW4tZGVjZW1iZXItMjAyMy1oYXMtYm9va2VkLWFsbC1jaG9wcGVycy1mb3ItY2FtcGFpZ25pbmctbWFtYXRhLWJhbmVyamVlLTExMjcwOTgxLmh0bWzSAa8BaHR0cHM6Ly93d3cubW9uZXljb250cm9sLmNvbS9uZXdzL2xvay1zYWJoYS1lbGVjdGlvbnMvYmpwLW1heS1nby1mb3ItbG9rLXNhYmhhLXBvbGxzLWluLWRlY2VtYmVyLTIwMjMtaGFzLWJvb2tlZC1hbGwtY2hvcHBlcnMtZm9yLWNhbXBhaWduaW5nLW1hbWF0YS1iYW5lcmplZS0xMTI3MDk4MS5odG1sL2FtcA?hl=en-IN&gl=IN&ceid=IN%3Aen"

response = requests.get(url)
text_list = []
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    all_paragraphs = soup.find_all("p")

    for paragraph in all_paragraphs:
        text_block = paragraph.get_text().split(" ")
        # print(text_block)
        for word in text_block:
            text_list.append(word)
else:
    print("Data Fetched Failed :")

most_repeated_word = max(text_list, key=text_list.count)
frequency = text_list.count(most_repeated_word)

print(
    f"The most repeated word in this link is {most_repeated_word} and the no of time it got repeated is {frequency}")
