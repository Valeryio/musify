

// Global variables
isPlaying = false;
currentSong = document.querySelector(".audio-player__song");


// Player attributes
let playerCurrentSongName = document.querySelector(".displayed-song-presentation__title");
let songSpotifybtn = document.querySelector(".displayed-song-representation__discover-btn");
let songErrorAlert = document.querySelector(".audio-player__error");

// track buttons
let playPauseBtn = document.querySelector(".audio-player__play_pause");
let seekSlider = document.querySelector(".audio-player__seek-slider");
let volumeSlider = document.querySelector(".audio-player__volume_slider");
let songList = document.querySelectorAll(".artist-song");

// console.log(songList);



/**
 * play the song and update the play/pause button status
 */
function playSong()
{
  if (isPlaying == false)
  {
    playPauseBtn.innerHTML = "<i class='fa fa-pause-circle fa-5x'></i>";
    currentSong.play()
    isPlaying = true;
  }
  else
  {
    playPauseBtn.innerHTML = "<i class='fa fa-play-circle fa-5x'></i>";
    currentSong.pause()
    isPlaying = false;
  }
}

/**
 * Update the different visual informations displayed
 * by the player
 *  
 */
function updatePlayerInformations() {
  // console.log("");
}


/**
 * Increase or decrease the volume of a song
 * 
 * @param {object} song the song to use
 * @param {object} volumeSlider the slider of the volume
 */
function manageSongVolume() {
  currentSong.volume = volumeSlider.value / 100;
}


/**
 * Update the position of the input range with the current
 * time
 */
function updateSeekSlider() {
  seekSlider.value = (currentSong.currentTime * 100) / currentSong.duration;
}

/**
 * Update the currentTime of the song with the input range
 */
function updateSongCurrentTime() {
  currentSong.currentTime = (seekSlider.value * currentSong.duration) / 100;
}




// Play the song if the play button is pushed
playPauseBtn.addEventListener("click", playSong);

// Detect loading errors in the song
currentSong.addEventListener("error", (e) => {
  // console.log("Error while loading the media");
  songErrorAlert.innerHTML = "No available preview for this song!";
})

// Detect functional loading for the song
currentSong.addEventListener("canplay", (e) => {
  songErrorAlert.innerHTML = "";
})

// Update the play.pause button when a song ends
currentSong.addEventListener("ended", (e) => {
  isPlaying = true;
  playSong();
})


// Manage the volume with the volume slider input range
volumeSlider.addEventListener("input", manageSongVolume);

// Update the place of the seek slider with the time
let songPosition = setInterval(updateSeekSlider, 1000);

// Update the currentTime of the music if the seek slider
// is triggered
seekSlider.addEventListener("input", updateSongCurrentTime);

// Play a new song if triggered
for (song of songList) {
  song.addEventListener("click", (e) => {

    ename = e.target.getAttribute("data-song-name");
    elink = e.target.getAttribute("data-preview-url");
    espotify = e.target.getAttribute("data-spotify-url");
    // console.log(ename, elink, espotify);

    songName = e.target.getAttribute("data-song-name");
    songPreviewLink = e.target.getAttribute("data-preview-url");
    songSpotifyUrl = e.target.getAttribute("data-spotify-url");;

    currentSong.src = songPreviewLink;
    playerCurrentSongName.innerHTML = songName;
    songSpotifybtn.setAttribute("href", songSpotifyUrl);


    
    currentSong.load();
    playSong();
    // console.log(songName, songPreviewLink, songSpotifyUrl);
  })
}