from text_to_speech.convert.offline import OfflineConversion

text = "Brown fox jumps over a lazy dog."
convert = OfflineConversion(text=text)
convert.speak()
