
//TODO: mvoe websocket stuff into main (same for the other functions?)

// Note that the path doesn't matter for routing; any WebSocket
// connection gets bumped over to WebSocket consumers
socket = new WebSocket("ws://" + window.location.host + "/chat/");
socket.onmessage = function(e) {
    alert(e.data);
}
socket.onopen = function() {
    socket.send("hello world");
}
// Call onopen directly if socket is already open
if (socket.readyState == WebSocket.OPEN) socket.onopen();

function handleDragStart(e) {
    //$(this).css({"opacity":0.4}); //,"left":"","top":""});
}

function handleDragStop(e) {
    //$(this).css({"opacity":""});//,"left":"","top":""});
}


var main = function()
{
    var gamestate = {};
    $.get("/api/game/1.json",{dataType:"json"}).success(function(data) { setupLayout(data)});

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
         


$('.cardFaceDiv').each(function(index) {
    $(this).draggable({start: handleDragStart, stop: handleDragStop});
});

$('.cardBackDiv').each(function(index) {
    $(this).draggable({start: handleDragStart, stop: handleDragStop});
});



