import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=KEIvXwUm8iE")
img.save("example_youtube.png")