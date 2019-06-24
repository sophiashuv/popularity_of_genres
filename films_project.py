import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import csv


def read_file(file_name):
    """
    (str) -> generator
    The function reads file and returns generator of data
    """
    f = open(file_name, encoding='utf-8', errors='ignore')
    data = (line for line in f)
    return data


def amount_of_films(file_name, genres, year):
    """
    (str, str , str) -> int
    Returns the amount of moveis in each genre in each year
    >>> print(amount_of_films("genres.list", 'Drama', "2000"))
    3243
    """
    lst_genres_year = list()
    data = read_file(file_name)
    for line in data:
        if genres in line and year in line:
            lst_genres_year.append(line.strip())
    return len(lst_genres_year)


def whole_amount_of_films(file_name):
    """
    (str) -> int
    The function ruturns the amount of films from 1896 to 2016
    >>>print(whole_amount_of_films("genres.list"))
    2164406
    """
    lst = list()
    n = 0
    data = read_file(file_name)
    for line in data:
        lst.append(line.split())
    for i in lst[42: 74]:
        n = n + int(i[1])
    return n
print("The amount af moveis is: ", whole_amount_of_films("genres.list"))


def list_of_genres(file_name):
    """
    (str) -> lst
    Returns the lst of different genres of moveison
    >>> print(list_of_genres("genres.list"))
    ['Short', 'Drama', 'Comedy', 'Documentary', 'Adult', 'Action', 'Thriller',
    'Romance', 'Animation', 'Family', 'Horror', 'Music', 'Crime', 'Adven
    ture', 'Fantasy', 'Sci-Fi', 'Mystery', 'Biography', 'History', 'Sport',
    'Musical', 'War', 'Western', 'Reality-TV', 'News', 'Talk-Show', 'Game-S
    how', 'Film-Noir', 'Lifestyle', 'Experimental', 'Erotica', 'Commercial']
    """
    lst = list()
    lst2 = []
    data = read_file(file_name)
    for line in data:
        lst.append(line.split())
    for i in lst[42: 74]:
        lst2.append(i[0])
    return lst2
print("Genres are: ", list_of_genres("genres.list"))


def file_string():
    """
    () -> str
    The function returns the string of different genres. The ammount of words
    depends from popularity of the genre.
    """
    lst = []
    lst2 = []
    string = ""
    data = read_file("genres.list")
    for line in data:
        lst.append(line.split())
        l = lst[42:74]
    i = 0
    while i < 32:
        k = ((l[i])[0] + " ") * int((l[i])[1])
        i = i + 1
        string = string + k
    return string


def list_of_films_amounts(file_name):
    """
    (str) -> lst
    The function ruturns list of films
    """
    list1 = []
    for year in range(2006, 2015):
        for genres in list_of_genres(file_name):
            lst = [amount_of_films(file_name, genres, year), genres, year]
            list1.append(lst)
    return (list1)


def sum_of_movies(file_name, year):
    """
    (str, str) -> int
    the function returns the amount of moveis made on a concrete years
    >>>print(sum_of_movies("genres.list", "2000"))
    26565
    """
    n = 0
    for genres in list_of_genres(file_name):
        n = n + amount_of_films(file_name, genres, year)
    return n


def sum_10of_movies(file_name, year):
    """
    (str, str) -> int
    the function returns the amount of in 10 the most populsr moveigenres
    of  concrete years
    >>>print(sum_10of_movies("genres.list", "2000))
    20558
    """
    n = 0
    for i in range(10):
        n = n + amount_of_films(file_name, list_of_genres(file_name)[i], year)
    return n


def table_sum(file_name, year1, year2):
    """
    (str, str, str) -> lst
    The function returns list genres and ammounts of films af each of tham
    on a concretu yearself.
    >>> print(table_sum("genres.list", "1950", "2015"))
    [['Genres', '1950', '2015', 'Difference'], ['Short', 743, 33458, -32715],
    ['Drama', 814, 20392, -19578], ['Comedy', 585, 13532, -12947],
    ['Documentary', 408, 10413, -10005], ['Adult', 2, 1688, -1686],
    ['Action', 84,3153, -3069], ['Thriller', 69, 5053, -4984],
    ['Romance', 177, 3508, -3331], ['Animation', 176, 2143, -1967],
    ['Family', 207, 3003, -2796], ['Horror', 10, 4168, -4158],
    ['Music', 253, 3165, -2912], ['Crime', 202, 2462, -2260],
    ['Adventure', 117, 2245, -2128], ['Fantasy', 35, 2385, -2350],
    ['Sci-Fi', 17, 2465, -2448], ['Mystery', 63, 2347, -2284],
    ['Biography', 27, 1829, -1802], ['History', 49, 1653, -1604],
    ['Sport', 48, 956, -908], ['Musical', 119, 614, -495],
    ['War', 66, 1326, -1260], ['Western', 161, 309, -148],
    ['Reality-TV', 1, 927, -926], ['News', 9, 679, -670],
    ['Talk-Show', 13, 597, -584], ['Game-Show', 19, 129, -110],
    ['Film-Noir',60, 0, 60], ['Lifestyle', 0, 6, -6],
    ['Experimental', 0, 0, 0],['Erotica', 0, 5, -5], ['Commercial', 0, 36,-36]]
    """
    lst1 = [["Genres", "1950", "2015", "Difference"]]
    for genres in list_of_genres(file_name):
        lst2 = [genres, amount_of_films(file_name, genres, year1),\
        amount_of_films(file_name, genres, year2),\
        amount_of_films(file_name, genres, year1) -\
        amount_of_films(file_name, genres, year2)]
        lst1.append(lst2)
    return(lst1)


def persantage(file_name, genres, year):
    """
    (str, str, str) -> int
    the function returns the persantage of films in the concrete genre in a
    concrete year
    >>>print(persantage("genres.list", 'Drama', "2000"))
    12.21
    """
    n = sum_of_movies(file_name, year)
    p = amount_of_films(file_name, genres, year) * 100/n
    return round(p, 2)


def persentage_list10(file_name, year):
    """
    (str, str) -> list
    the function returns the list of persantages of 10 genras
    >>>print(persentage_list10("genres.list", "2000"))
    [23.7, 15.8, 12.1, 16.7, 10.7, 5.1, 3.8, 3.9, 4.6, 3.7]
    """
    lst = []
    n = sum_10of_movies(file_name, year)
    for i in range(10):
        lst.append(round(amount_of_films(file_name, \
        list_of_genres(file_name)[i], year) * 100/n, 1))
    return lst


def years_10(file_name, beginning, end, m):
    """
    (str, int, int, int) -> tuple
    Returns the tuple of amounts of moveison concrete amount of time and genres
    >>> print(years_10("genres.list", 2000, 2002, 0))
    (16994, 'Short', 2000, 2002)
    """
    n = 0
    for i in range(beginning, end+1):
        n = n + amount_of_films(file_name, list_of_genres(file_name)[m], str(i))
    return (n, list_of_genres(file_name)[m], beginning, end)


def list_of_top5():
    """
    () -> lst
    The function returns the list of list of filns
    >>>print(list_of_top5())
    [[(292300, 'Short', 2006, 2015), (168122, 'Drama', 2006, 2015),\
     (116981, 'Comedy', 2006, 2015), (103425, 'Documentary', 2006, 2015), \
     (37354, 'Thriller', 2006, 2015)],[(61889, 'Short', 1996, 2005),\
     (40735, 'Documentary', 1996, 2005), (39134, 'Drama', 1996, 2005), \
     (30486, 'Comedy', 1996, 2005), (25562, 'Adult', 1996, 2005)],\
     [(20723, 'Drama', 1986, 1995), (16978, 'Short', 1986, 1995), \
     (14447, 'Comedy', 1986, 1995), (14156, 'Documentary', 1986, 1995), \
     (10991, 'Adult', 1986, 1995)],[(17995, 'Drama', 1976, 1985), \
     (11459, 'Short', 1976, 1985), (10674, 'Comedy', 1976, 1985), \
     (9768, 'Documentary', 1976, 1985), (4810, 'Action', 1976, 1985)],
    [(17125, 'Drama', 1966, 1975), (12743, 'Short', 1966, 1975), \
    (9681, 'Comedy', 1966, 1975), (9287, 'Documentary', 1966, 1975), \
    (3948, 'Crime', 1966, 1975)],[(12947, 'Drama', 1956, 1965), \
    (10079, 'Short', 1956, 1965), (7996, 'Comedy', 1956, 1965), \
    (6792, 'Documentary', 1956, 1965), (3392, 'Music', 1956, 1965)]]
    """
    lst = []
    lst.append((top_5("genres.list", 2006, 2015)))
    lst.append((top_5("genres.list", 1996, 2005)))
    lst.append((top_5("genres.list", 1986, 1995)))
    lst.append((top_5("genres.list", 1976, 1985)))
    lst.append((top_5("genres.list", 1966, 1975)))
    lst.append((top_5("genres.list", 1956, 1965)))
    return lst


f = open('table4.csv', 'w')
arr = table_sum("genres.list", "1950", "2015")
for i in range(len(arr)):
    f.write(arr[i][0] + '\t' + str(arr[i][1]) + '\t' + str(arr[i][2]) + \
    '\t' + str(arr[i][3]) + '\n')


x1 = amount_of_films("genres.list", 'Short', "2011")
x2 = amount_of_films("genres.list", 'Short', "2012")
x3 = amount_of_films("genres.list", 'Short', "2013")
x4 = amount_of_films("genres.list", 'Short', "2014")
x5 = amount_of_films("genres.list", 'Short', "2015")
y1 = amount_of_films("genres.list", 'Drama', "2011")
y2 = amount_of_films("genres.list", 'Drama', "2012")
y3 = amount_of_films("genres.list", 'Drama', "2013")
y4 = amount_of_films("genres.list", 'Drama', "2014")
y5 = amount_of_films("genres.list", 'Drama', "2015")

short = (x1, x2, x3, x4, x5)
drama = (y1, y2, y3, y4, y5)

ind = np.arange(len(short))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, short, width,
                color='#ff8922', label='Short')
rects2 = ax.bar(ind + width/2, drama, width,
                color='#ffbe84', label='Drama')

ax.set_ylabel('Amount of films')
ax.set_xlabel('Years')
ax.set_title('Amount of films in Short and Drama ganre')
ax.set_xticks(ind)
ax.set_xticklabels(('2011', '2012', '2013', '2014', '2015'))
ax.legend()


def autolabel(rects, xpos='center'):

    xpos = xpos.lower()
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.6, 'right': 0.67, 'left': 0.53}

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()


x1 = amount_of_films("genres.list", 'Short', "1951")
x2 = amount_of_films("genres.list", 'Short', "1952")
x3 = amount_of_films("genres.list", 'Short', "1953")
x4 = amount_of_films("genres.list", 'Short', "1954")
x5 = amount_of_films("genres.list", 'Short', "1955")
y1 = amount_of_films("genres.list", 'Drama', "1951")
y2 = amount_of_films("genres.list", 'Drama', "1952")
y3 = amount_of_films("genres.list", 'Drama', "1953")
y4 = amount_of_films("genres.list", 'Drama', "1954")
y5 = amount_of_films("genres.list", 'Drama', "1955")

short = (x1, x2, x3, x4, x5)
drama = (y1, y2, y3, y4, y5)

ind = np.arange(len(short))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, short, width,
                color='#ff8922', label='Short')
rects2 = ax.bar(ind + width/2, drama, width,
                color='#ffbe84', label='Drama')

ax.set_ylabel('Amount of films')
ax.set_xlabel('Years')
ax.set_title('Amount of films in Short and Drama ganre')
ax.set_xticks(ind)
ax.set_xticklabels(('1951', '1952', '1953', '1954', '1955'))
ax.legend()

autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()


labels = list_of_genres("genres.list")[:10]
sizes = persentage_list10("genres.list", "1950")
colors = ['#ab5000', '#ffa95c', '#e66c00', '#ff7f0e', '#ffddbf', '#ff9435',\
'#ffbe84', '#f97500', '#da8133', '#ff6b41']
explode = (0.1, 0.1, 0, 0, 0, 0, 0, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()


labels = list_of_genres("genres.list")[:10]
sizes = persentage_list10("genres.list", "2015")
colors = ['#ab5000', '#ffa95c', '#e66c00', '#ff7f0e', '#ffddbf', '#ff9435',\
'#ffbe84', '#f97500', '#da8133', '#ff6b41']
explode = (0.1, 0.1, 0, 0, 0, 0, 0, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()

text = (file_string())

wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()


def top_5(file_name, beginning, end):
    """
    (str, int, int) -> list
    Returns the list of tuples of top 5 moveis on concrete amount of time
    >>> print(top_5("genres.list", 2001, 2010))
    [(145957, 'Short', 2001, 2010), (85388, 'Drama', 2001, 2010),
    (70665, 'Documentary', 2001, 2010), (62427, 'Comedy', 2001, 2010),
    (36639, 'Adult', 2001, 2010)]
    """
    lst = [years_10(file_name, beginning, end, i) for i in range(32)]
    m = sorted(lst, reverse=True, key=lambda x: x[0])
    return(m[:5])


arr2 = list_of_top5()
f = open('table4.csv', 'w')
for i in range(len(arr2) - 1):
    f.write((str(arr2[i][0][2]) + "-" +str(arr2[i][0][3])) + '\t' \
    + str(arr2[i][0][1]) + " " + str(arr2[i][0][0]) + '\t' +\
    str(arr2[i][1][1]) + " " + str(arr2[i][1][0]) + '\t' + \
    str(arr2[i][2][1]) + " " + str(arr2[i][2][0]) + '\t' \
    + str(arr2[i][3][1]) + " " + str(arr2[i][3][0]) + '\t' \
    + str(arr2[i][4][1]) + " " + str(arr2[i][4][0]) + '\n')
    
