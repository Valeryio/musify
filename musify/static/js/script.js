

// Global variables
isPlaying = false;
song = document.querySelector(".audio-player__song");

console.log("Here");
// track buttons
let playPauseBtn = document.querySelector(".audio-player__play_pause");


playPauseBtn.addEventListener("click", play_song());

function play_song()
{
    if (isPlaying == false)
    {
        playPauseBtn.innerHTML = "<i class='fa fa-play-circle fa-5x'></i>";
        //song.play()
        isPlaying = true;
    }
    else
    {
        playPauseBtn.innerHTML = "<i class='fa fa-pause-circle fa-5x'></i>";
        song.play()
        isPlaying = false;
    }
    // Qinx Majie American Love
}