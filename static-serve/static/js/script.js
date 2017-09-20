function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

$(document).ready(function(){
  console.log("working?");
  // get the query string from url
  var query = getParameterByName('q')
  var tweetList =[];
  var nextTweetUrl;

  // attach a new tweet to the web
  function attachTweet(tweetValue, prepend, retweet){
    var tweetContent = tweetValue.content;
    var dateDisplay = tweetValue.date_display;
    var timesince = tweetValue.timesince;
    var tweetUser = tweetValue.user;
    var tweetFormattedHTML = "<div class=\"panel\" id=\"mediabody\">"
    +tweetContent + "</div><br>" + "via <span class='bg-info text-center'>" +
    "<a href='"+ tweetUser.url +"'>" + tweetUser.username +"</a>"+
    " | "+ dateDisplay +
     "</span> <a href='/tweet/"+ tweetValue.id +"' class='btn btn-primary btn-xs'>View</a>"+
      " " + timesince + "| <a href='' class='tweet-like'>Like</a></div><hr />"

    if(prepend == true){
      $('#tweet-container').prepend(tweetFormattedHTML)
    }else{
      $('#tweet-container').append(tweetFormattedHTML)
    }
  }

  function updateHashLinks(){
    $("#mediabody").each(function(data){
      var hashtagRegex = /(^|\s)#([\w\d-]+)/g
      var newText = $(this).html().replace(hashtagRegex, "$1<a href='/tags/$2/'>#$2</a>")
      $(this).html(newText)
    })
  }

  // parse all the tweet and display on page at the beginning
  function parseTweets(){
    if (tweetList == 0){
        $('#tweet-container').text('No tweet found')
    }else{
      //tweet exists
      $.each(tweetList, function(key, value){
        var tweetKey = value.key;
          attachTweet(value)
      })
    }
  }

  //update the web immediately by using ajax and search function applied
  function fetchTweets(url){
    var fetchUrl;
    if(!url){
      fetchUrl = '/api/tweet/'
    }else{
      fetchUrl = url
    }

    // make ajax env
    $.ajax({
      url:fetchUrl,
      data: {
        "q": query
      },
      method:'GET',
      success: function(data){
        // store the data into tweetlist
        tweetList = data.results
        console.log(data)
        if(data.next){
          // the next page of data for loadmore
          nextTweetUrl = data.next
        }else{
          $("#loadmore").css("display", 'none')
        }
        // call the parseTweets
        parseTweets()
        updateHashLinks()
      },
      error: function(data){
        console.log("error")
        console.log(data)
      }
    })
  }

  // intialize call of fetchTweets()
  fetchTweets()

  // load more tweets
  $('#loadmore').click(function(event){
    event.preventDefault()
    if(nextTweetUrl){
      fetchTweets(nextTweetUrl)
    }
  })

  $(document.body).on("click",".tweet-like", function(e){
    e.preventDefault()
    var this_ = $(this)
    this_.text("Linked")
  })


  // display char left
  var charsStart = 140
  var charsCurrent = 0
  $("#tweet-form").append("<span id='tweetCharsLeft'>"+ charsStart +"</span>")

  $("#tweet-form textarea").keyup(function(event){
    var tweetValue = $(this).val()
    console.log(tweetValue.length)
    charsCurrent= charsStart - tweetValue.length
    var spanChars = $('#tweetCharsLeft')
    $('#tweetCharsLeft').text(charsCurrent)

    if(charsCurrent > 0 ){
      spanChars.removeClass('grey-color')
      spanChars.removeClass('red-color')

    }else if(charsCurrent == 0 ){
        spanChars.removeClass('red-color')
        spanChars.addClass('grey-color')
    }else if(charsCurrent < 0){
      spanChars.removeClass('grey-color')
      spanChars.addClass('red-color')
    }
  })

  $("#tweet-form").submit(function(event){
    event.preventDefault()
    var this_ = $(this)
    console.log(this_.serialize())
    var formData = this_.serialize()
    if (charsCurrent >=0){
      $.ajax({
        url:"/api/tweet/create/",
        data: formData,
        method:'POST',
        success: function(data){
            this_.find("input[type=text], textarea").val('')
           attachTweet(data, true)
           updateHashLinks()
        },
        error: function(data){
          console.log("error")
          console.log(data)
        }
      })
    }else{
      $('#tweet-form').text("Tweet too long, cannot send")
    }
  })
});
