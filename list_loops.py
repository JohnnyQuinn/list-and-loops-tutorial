songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[0])
print(songs[2])

print(songs[1:3])

songs[2] = "Papa's Got a Brand New Bag"

print(songs)

songs.extend(["Slow Burn", "Stuck in the Middle With You", "Sweet Time"])

del songs[0]

print(songs)

animals =["Gorilla", "Goose", "Giraffe"]

animals.append("Ground Hog")

print(animals[2])

del animals[0]

for animal in animals:
    print(animal)