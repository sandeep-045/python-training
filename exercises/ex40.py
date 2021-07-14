class Song:
	def __init__(self,lyrics):
		self.lyrics=lyrics

	def sing(self):
		print(self.lyrics)


new_song=Song('Happy birthday song')
new_song.sing()