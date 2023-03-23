
# BWF - Usama Mahtab

# 8-6 City Names
def city_country(city, country):
    info = '"' + city + ', ' + country + '"'
    return info


print(city_country("Islamabad", "Pakistan"))
print(city_country("Auckland", "New Zealand"))
print(city_country("Sydney", "Australia"))


# 8-7 Album
def make_album(a_name, a_title, tracks=''):
    album = {'artist name': a_name, 'album name': a_title}
    if tracks:
        album['no_of_tracks'] = tracks
    return album


print(make_album('Talha Anjum', 'Rebirth', 15))
print(make_album('Eminem', 'The Slim Shady', 20))


# 8-8 User Albums
def make_album(a_name, a_title, tracks=''):
    album = {'artist name': a_name, 'album name': a_title}
    if tracks:
        album['no_of_tracks'] = tracks
    return album


active = True
while active:
    artist = input("Enter artist's name:\n")
    album = input("Enter album name:\n")
    tracks = input("Enter number of tracks:\n")
    print(make_album(artist, album, tracks))

    choice = input('Press "q" to Quit OR any key to Continue:\n')

    if choice.lower() == 'q':
        active = False

