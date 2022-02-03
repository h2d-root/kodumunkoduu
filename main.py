from pytube import YouTube
url = input("video url? ")


try:
    YouTube(url).streams.filter(
        mime_type="video/mp4", res="720p").first().download()

    print("720p olarak indirildi")
except:
    YouTube(url).streams.filter(
        mime_type="video/mp4", res="480p").first().download()

    print("720p olamamasından dolayı videonuz 480p olarak indirildi")

yt = YouTube(url)
print(yt.title, " adlı video indirildi :)")
