import json
from datetime import date

######## Playlists Backend Functions  ########
def numOfPlaylists():
	"""Works out total Number of Playlists

		Args:
			None

		Return:
			String: Number of Playlists
	"""
	with open('databse.json') as file: # Opens JSON file as 'file'
		f = json.load(file)
		playlists = f['Playlists'] # Selects the 'Playlists' array from the JSON
		num = len(playlists) # Gets the length of the array
				
	return str(count)

def getPlaylistName(id):
  '''This function will return the name of a playlist using the ID'''
  with open('databse.json') as file:
        f = json.load(file)
        f = f['Playlists']
        for playlist in f:
          if playlist['ID'] == int(id):
            return playlist['Name']

def getPlaylistInfo(pid):
	"""Retrieves all infomation of a selected playlist

		Args:
			pid (int): ID of Playlist

		return:
			String: String of HTML Table rows to be injected with JS
	"""
	playlist_info = "<tr>"
	with open('databse.json') as file: # Opens JSON file as 'file'
		f = json.load(file)
		playlists = f['Playlists']
		for playlist in playlists: # Lops through each playlist until it gets to the playlist with the right ID
			if playlist['ID'] == int(pid):
				playlist_info += "<td>{}</td>".format(playlist['Name'])
				playlist_info += "<td>{}</td>".format(len(playlist['Songs']))
				playlist_info += "<td>{}</td>".format(playlist['Date'])
			
	playlist_info += "</tr>"
	return playlist_info

def getPlaylistSongs(pid):
	"""Gets all the songs from a selected playlist
	
		Args:
			pid (int): ID of playlist

		Return:
			String: HTML Table rows of all songs
	"""
  '''This function retrieves all of the songs stored about the selected playlist.'''
  playlist_songs = ""
  with open('databse.json') as file:
        f = json.load(file)
        playlist = f['Playlists']
        for playlist in playlist: # Loops though each playlist till it ets to the correct playlist
          if playlist['ID'] == int(pid):
            songs = playlist['Songs']
            songIndex = 0 # Sets 'songIndex' as 0 to assign each song an ID the same as the index ion the array
            for song in songs: #Loops though each song building the 'Tr' element
              playlist_songs += "<tr>"
              playlist_songs += "<td style='width: 32.5%'>{}</td>".format(song['Name'])
              playlist_songs += "<td style='width: 32.5%'>{}</td>".format(song['Artist'])
              playlist_songs += "<td style='width: 25%'><a href='{}' target='_blank'>Listen Now!</a></td>".format(song['Link'])
              playlist_songs += f"<td class='text-center' style='width: 25%'><a data-bs-toggle='modal' data-bs-target='#delSongModal' onclick='delSongID({songIndex}, {id});'><i class='bi bi-x'></i></a></td>"
              playlist_songs += "</tr>"
              songIndex +=1
  return playlist_songs
            

def createPlaylistTable():
	"""populates the playlist Table
	
		Args:
			None

		Return:
			Stirng: HTML Table row with all playlist infomation
	"""
	'''This function will read the external database and prints all of the playlists'''
	with open('databse.json') as file:
		playlist_table = ""
		f = json.load(file)
		f = f['Playlists']  #This makes the function search the 'Playlists' part of the database
		
		for playlist in f:  #Loops though every user in the database and compares them with entered credentials.
			playlist_table+= "<tr>"
			playlist_table += f"<td>{playlist['Name']}</td>"
			playlist_table += f"<td>{len(playlist['Songs'])}</td>"
			playlist_table += f"<td>{playlist['Date']}</td>"
			playlist_table += f"""<td>
						<div class='dropdown'>
							<i class='bi bi-three-dots' id='dropdownMenuButton1' data-bs-toggle='dropdown'> </i>
							<ul id='playlist_dropdown' class='dropdown-menu' aria-labelledby='dropdownMenuButton1'>
								<li><a class='dropdown-item' onclick='viewPlaylist({playlist['ID']})' >View</a></li>"""
			playlist_table += r"""<li><a class='dropdown-item' onclick='delPlaylistID({}, "{}")' id='delete' data-bs-toggle='modal' data-bs-target='#delPlayModal'>Delete</a></li>""".format(playlist['ID'], playlist['Name'])
			playlist_table += """</ul>
						</div></td>
						</tr>"""
				
		if playlist_table == "": # If no playlists excists table row will display 'No Playlists Found'
			playlist_table = "<tr><td class='text-center' colspan='4'>No Playlists Found</td></tr>"

		return playlist_table

def addSongToJson(id, newSong):
	"""Adds song to playlist

	Args:
			id (int):Id Of Playlist
			newSong (dict): dicgtionary off the new song

	Return:
		None
	"""
	with open('databse.json','r+') as file:
	 data = json.load(file)
	 playlists = data['Playlists']
	 for playlist in playlists:
		 if playlist['ID'] == int(id):
			 songs = playlist["Songs"] # Sets var 'songs' to all current soings in the selected playlist
			 songs.append(newSong) # Adds new song infomation to end of array
			 file.seek(0) # Sets the file readline to the first line
			 json.dump(data, file, indent = 4) # Overwirites the Json File with the Updated Verson

def deleteSongFromJson(songID, pid):
	"""deletes Songs from Playlist

	Args:
			songID (int): ID Of Song
			id (itn): ID Of Playlist

	Return:
	 None
	"""
	pid = int(pid)
	songID = int(songID)
	
	with open('databse.json','r') as file:
			print('Opening')
			data = json.load(file)
			playlists = data['Playlists']
			
			for playlist in playlists:
				if playlist['ID'] == pid:
					print(playlist['ID'])
					print(playlist["Songs"])
					del playlist["Songs"][songID]
					print(playlist["Songs"])

	with open('databse.json','w') as file:
			json.dump(data, file, indent=4)

def deletePlaylistById(pid):
	"""
		Deletes a playlist from the json unsing an inputed ID

		Args:
			pid (String - Int): ID Of playlist
	"""
	pid = int(pid)

	with open('databse.json','r') as file:
			print('Opening')
			data = json.load(file)
			playlists = data['Playlists']

			i = 0
			for playlist in playlists:
				if playlist['ID'] == pid:
					del playlists[i]
				i += 1

	with open('databse.json','w') as file:
			json.dump(data, file, indent=4)

def createPlaylist(name):
	"""
		Creates A Playlist:

		Args:
			name (String): Name of new playlist
	"""
	
	today = date.today()
	today_date = today.strftime("%d / %m / %Y")
	
	with open('databse.json','r+') as file:
		data = json.load(file)
		playlists = data['Playlists']
		number_of_playlists = len(playlists)
		ID_new_playlist = number_of_playlists + 1

		new_playlist = {
			"ID": ID_new_playlist,
			"Name": name,
			"Songs": [],
			"Date": today_date
		}

		playlists.append(new_playlist)
		file.seek(0)
		json.dump(data, file, indent = 4)