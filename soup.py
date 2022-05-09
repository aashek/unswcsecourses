from gazpacho import Soup

url = "https://en.wikipedia.org/wiki/List_of_multiple_Olympic_gold_medalists"
soup = Soup.get(url)
table = soup.find("table", {"class": "wikitable sortable"}, mode="first")
# trs = table.find("tr")[1:]
trs = table.find("tr")[1:]
print(type(trs))
print(len(trs))


# li = []
# for tr in trs:
#     li.append(
#     {
#         "name": tr.find("td")[0].text,
#         "country": tr.find("td")[1].text,
#         "medals": int(tr.find("td")[-1].text)
#     }
#     )
# print(li[:5], indent=2)