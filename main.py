## Imports
from flask import Flask, render_template, jsonify, request, make_response, redirect, url_for, session
from flask_session import Session
from backend import *
from functools import wraps

#Flaks app initialisation with session set up
app = Flask('app', template_folder='static')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


#Home Page Route
@app.route('/')
def home():
    """Generates Home Screen From Template

    Returns:
        HTML File: Template For Homescreen
    """
    return render_template('home/home.html')

#This is the route to get all playlists form the JSON file
@app.route('/api/playlists')
def playlists():
    """Generates Playlists Table

    Returns:
        String: returns a string of all the current playlists
    """
    #Create a HTML layout of the table to print back into the DOM
    return createPlaylistTable()

	
#This is the route to get the total number of playlists
@app.route('/api/num_playlists', methods=['GET'])
def numOfPlay():
	"""Calls backend function to get total number of playlists

		return:
			result of function: Total Number Of playlists
	"""
	#Gets total number of playlists
	num = numOfPlaylists()
	return num


@app.route('/view/api/playlist_name', methods=['GET'])
def playlistName():
	"""Gets Selected Playlist Name

	Args:
		pid (int): ID of playlist
	
	Returns:
			String: Name Of Playlist
	"""
	pid = request.args.get('playlistID')
	return getPlaylistName(pid)
	
#This route gets the playlist infomation such as Name, Number of Songs and Date of Creation
@app.route('/view/api/playlist_info', methods=['GET'])
def playlistInfo():
	"""Gets Selected Playlisted Infomation

		Args:
		selectedPlaylist (int): ID of selected laylist

		return:
			result of funciton: Gets all infomation on select playlist
  """
	selectedPlaylist = request.args.get('playlistID')
	return getPlaylistInfo(selectedPlaylist) #Links to a function in backend.py
  

#This route returns all a songs in a table format
@app.route('/view/api/playlist_songs', methods=['GET'])
def playlistSongs():
	"""Lists All of the Selected Playlists Songs

		Args:
		selectedPlaylist (int): ID of selected laylist

		return:
			result of funciton: Gets all songs from the select playlist
  """
	selectedPlaylist = request.args.get('playlistID')
	return getPlaylistSongs(selectedPlaylist) #Links to a function in backend.py


#This is the route for creating a new playlist
@app.route('/api/createPlaylist', methods=["POST"])
def newPlaylist():
	"""Creates a new playlist

		Args:
		 new_playlist_name (String): Value is received by API call from the forunt end

		return:
			redirect: Returns to home screen
	"""
	new_playlist_name = request.form['playlistName']
	createPlaylist(new_playlist_name)
	
	return redirect(request.referrer)

	
#
@app.route('/api/addSong', methods=['POST'])
def addSong():
	"""adds Song to Playlists

	Gets ID, Name, Artist, Link from HTML Form
	
	Returns:
			Reidrect: Redirects the user to the home screen
	"""
	playlistID = request.form['playlistID']
	songName = request.form['name']
	songArtist = request.form['artist']
	songLink = request.form['link']
	newSong = {"Name": songName, "Artist": songArtist, "Link": songLink}
	
	addSongToJson(playlistID, newSong) #Links to a function in backend.py
	
	return redirect(request.referrer)

	
#
@app.route('/api/delSong', methods=['POST'])
def deleteSong():
	"""Deletes Song Form Playlist

	Args:
		songID (int): ID of Song to Delete
		playlistID (int): ID of playlist to delete from

	Returns:
			redirect: redirects to home screen
	"""
	songID = request.form['sid']
	playlistID = request.form['pid']
	deleteSongFromJson(songID, playlistID) #Links to a function in backend.py
	return redirect(request.referrer)

	
#
@app.route('/api/delPlay', methods=['POST'])
def deletePlaylist():
	"""Deletes a selected playlist

		args:
			pid (int): ID of Playlist to delete
	
		Returns:
			redirect: redirects to home screen
	"""
	pid = request.form['delpid']
	deletePlaylistById(pid)
	return redirect(request.referrer)

	
app.run(debug=True, host='0.0.0.0', port=8080)