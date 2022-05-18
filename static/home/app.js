/// Defining Elements
var homePage = document.getElementById('homePage')
var viewPlaylistPage = document.getElementById('viewPlaylistPage')
var playlist = document.getElementById('playlist_dropdown')

/// API Functions
function callAPI_innerHTML(url, id){
	let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      let Result = this.responseText;
      document.getElementById(id).innerHTML = Result;
    }
  }
  xhttp.open("GET", url, true);
  xhttp.send();
}

function callAPI(url, id){
	let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      let Result = this.responseText;
			console.log(Result)
      document.getElementById(id).innerText = Result;
    }
  }
  xhttp.open("GET", url, true);
  xhttp.send();
}


/// Change To View Playlist Page
function viewPlaylist(pid){
  console.log("PLaylist ID: " + pid);
	document.getElementById('homePage').style.display='None';
	document.getElementById('viewPlaylistPage').style.display='block';

	document.getElementById('addSong_PlaylistID').value = pid;

	// Setting the Playlist Name
	url = "/view/api/playlist_name?playlistID="+pid;
	callAPI(url ,'view_playlist_name')

	// Getting Playlist Infomation
	url = "/view/api/playlist_info?playlistID="+pid;
	callAPI_innerHTML(url ,'view_playlist_info');

	// Listin All The Songs
	url = "/view/api/playlist_songs?playlistID="+pid;
	callAPI_innerHTML(url ,'view_playlist_songs');
}

/// Delete Song Function
function delSongID(sid, pid) {
	document.getElementById('delSID').value = sid;
	document.getElementById('delPID').value = pid;
}

/// Delete Playlist Function
function delPlaylistID(pid, pname){
	document.getElementById('delPlaylistName').innerHTML = pname;
	document.getElementById('delPlaylistID').value = pid;
}

/// ON Window Load Populate Tables
window.addEventListener('load', (event) =>  {
  callAPI_innerHTML('/api/playlists' ,'playlist_list');
	callAPI('/api/num_playlists', 'numOfPlay');
});