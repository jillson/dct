var main = function()
{
    var gamestate = {};
    console.log("Userid is" + uid);

    function createChatWindow()
    {
	var $div = $("#content");
	$div.html('<input type="textarea" id="chat" name="chat"><input type="button" id="sendMessage" value="send"><br><div id="chattext">&nbsp;</div><br>');
	$("#sendMessage").click(function() {
	    var text = $("#chat").val();
	    console.log("Debug" + text);
	    $("#chat").val(''); //clear text typed
	    chatSocket.send(text);
	    return false;
	});
    }
    createChatWindow();

    function createSocket(path,onmessage,onopen)
    {
	var socket = new WebSocket("ws://" + window.location.host + path);
	socket.onmessage = onmessage;
	socket.onopen = onopen;
	// Call onopen directly if socket is already open
	if (socket.readyState == WebSocket.OPEN) socket.onopen();
	return socket;
    }

    var chatSocket = createSocket("/chat/",
				  function(e) {
				      $("#chattext").append("<p>"+e.data+"</p>")
				      if (e.data === "your mom")
				      {
					  $.get("/api/gameinstance/1",{dataType:"json"}).success(function(data) { setupLayout(data)});
				      }
				  }, function() {
				      chatSocket.send(username + " joined the chat");
				  });
    function handleStatus(e) {
	$("#chattext").append("<i>"+e.data+"</i>");
    }

    
    var statusSocket = createSocket("/user/"+uid,handleStatus,function(){});

    
    function handleDragStart(e) {
	//$(this).css({"opacity":0.4}); //,"left":"","top":""});
    }

    function handleDragStop(e) {
	//$(this).css({"opacity":""});//,"left":"","top":""});
    }

   
    function makeCard(card,$target)
    {
	var $div;
	if ($target.hasClass('them') || $target.hasClass('flip'))
	{
	    $div = $("<div class='cardBackDiv'/>");
	}
	else
	{
	    $div = $("<div class='cardFaceDiv'/>");
	}
	var text = card.text || "";
	$div.append($("<p>"+text+"</p>"));
	console.log("Adding"+text+"to"+$target);
	$target.append($div);
	$div.draggable({start: handleDragStart, stop: handleDragStop});

    }
    
    function setupDeck(data)
    {
	data = JSON.parse(data);
	gamestate["cards"] = data.cards;
	for (var i = 0; i < data.cards.length; i++)
	{
	    if (data.cards[i].list && data.cards[i].list.length > 0)
	    {
		var $target = $('#' + data.cards[i].target);
		console.log($target);
		var $card = makeCard(data.cards[i].list[0],$target);
		$target.append($card);
	    }
	}

	$('.cardFaceDiv').each(function(index) {
	    $(this).draggable({start: handleDragStart, stop: handleDragStop});
	});
	
	$('.cardBackDiv').each(function(index) {
	    $(this).draggable({start: handleDragStart, stop: handleDragStop});
	});
    }
    
    function setupLayout(data)
    {
	gamestate["board"] = data;
	data = JSON.parse(data);
	$base = $('#base');
	$base.text("");
	$base.append($("<h2>" + data.name + "</h2>"));
	for (var i = 0; i < data.board.length; i++)
	{
	    var $nextDiv = $("<div class='groupDiv'/>");
	    var group = data.board[i];
	    if (group.name) {
		$nextDiv.append($("<p>"+group.name+"</p>"));
	    }

	    for (var j = 0; j < group.spots.length; j++)
	    {
		var spot = group.spots[j];
		var visibility = group.visibility || "all";
		var cid = spot.id || "";
		if (cid) {
		    cid = "id=" + cid + " ";
		}
		var $spotDiv = $("<div " + cid + "class='dropDiv " + visibility + "'/>");
		var spotWidth = group.spotWidth || 80;

		if (spot.drop) {
		    $spotDiv.droppable({
			hoverClass: 'active',
			drop: function(event, ui) {
			    var $parent = $(ui.draggable).parent();
			    var parentId = $parent.attr("id");
			    var cards = gamestate.cards;
			    for (var i = 0; i < cards.length; i++)
			    {
				if (cards[i].target == parentId && cards[i].list && cards[i].list.length > 0)
				{
				    console.log("Pulling top card off deck, adding next one back");
				    cards[i].list.shift();
				    if (cards[i].list.length > 0)
				    {
					var $card = makeCard(cards[i].list[0],$parent);
					$parent.append($card);
				    }
				}
			    }
			    
			    $(this).append($(ui.draggable));
			    $(ui.draggable).css({"left":"","top":""});
			    
			    if (!$(this).hasClass('them'))
			    {
				if (ui.draggable.hasClass('cardBackDiv'))
				{
				    ui.draggable.toggleClass('cardBackDiv');
				    ui.draggable.toggleClass('cardFaceDiv');
				}
			    }
			}});
		}
		if (spot.name) {
		    $spotDiv.text(spot.name);
		}
		//$spotDiv.width(spotWidth);
		$spotDiv.css({"minWidth":spotWidth+"px"});
		$nextDiv.append($spotDiv);
	    }
	    $base.append($nextDiv);
	    if (group.newRow) {
		$base.append("<br style='clear:both;'>");
	    }

	}
	$.get("/api/gameinstance/1.json",{dataType:"json"}).success(function(data) { setupDeck(data)});
	

    }
    return({"state":gamestate});
}();
         






