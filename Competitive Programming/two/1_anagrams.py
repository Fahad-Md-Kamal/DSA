# def anagrams(st):
#     d = {}
#     for word in st:
#         s = "".join(sorted(word))
#         print("D:\t", d)
#         if s in d:
#             d[s].append(word)
#         else:
#             d[s] = [word]
#     return [d[s] for s in d if len(d[s]) > 1]

# print(anagrams('bowel below elbow'))

