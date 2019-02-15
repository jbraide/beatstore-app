// search form and audio-player$
$("#search").click(function(){
  $("#form1").slideDown();
});

$(".play-button").click(function(){
  $(".player").toggle().slideDown()
});

$(".clickable-row").click(function(){
  thisdata = $(this).data("href");
  //console.log(thisdata);
  //window.location = thisdata;
})

// audio player functionality

// var songs = $('.loadbeat').attr('data-href');



// var songs = $(".loadbeat").click(function(){
//    var beatdata = $(this).attr("data-href");
//    window.load = beatdata
//  });

var songs =
  $(".loadbeat").click(function(){
   var beatdata = $(this).data("href");
   //window.onload = beatdata
   console.log(beatdata) = song

 });

var songTitle = document.getElementById('songTitle');
var seekBar = document.getElementById('seekbar');
var currentTime = document.getElementById('currenttime')

var song = new Audio();
var currentSong = 0;

window.onload = playSong();

function playSong(){
  song.src = songs;
  songTitle.textContent = songs;

  song.play();
}

function playOrPauseSong(){
  if(song.paused){
    song.play();
    $("#play span").attr("class","fa fa-pause")
  }
  else{
    song.pause()
    $("#play span").attr("class","fa fa-play")
    }

}



function repeat(){
      song.loop = true;
}

function decreaseVolume(){
  song.volume -= 0.1;
}
function increaseVolume(){
  song.volume += 0.1;
}

// song.addEventListener('timeupdate', function(){
//   var position = song.currentTime / song.duration;
//
//   seekBar.style.width = position * 100 + '%';
//
//   convertTime(Math.round(song.currentTime);
//
//   if(song.ended){
//     next();
//   }
// })

function convertTime(seconds){
        var min = Math.floor(seconds / 60);
        var sec = seconds % 60;

        min = (min<10) ? "0" + min : min;
        sec = (sec < 10) ? "0" + sec : sec;
        currentTime.textContent = min + ":" + sec;

        totalTime(Math.round(song.duration))
      }

function totalTime(seconds){
      var min = Math.floor(seconds / 60);
      var sec = seconds % 60;

      min = (min<10) ? "0" + min : min;
      sec = (sec < 10) ? "0" + sec : sec;
      currentTime.textContent += "/" + min + ":" + sec;
      }



function next(){
  currentSong++;
  if(currentSong > 2){
    currentSong = 0;
  }

  playSong()
}

function previous(){
  currentSong--;
  if(currentSong < 0){
    currentSong = 2;
  }

  playSong();
}

function mute(){
  if(song.muted = true){
      $("#mute span").attr("class","fa fa-volume-off")
  }
  else{
    song.muted = false;
    $("#mute span").attr("class", "fa fa-volume-up")
  }

}
