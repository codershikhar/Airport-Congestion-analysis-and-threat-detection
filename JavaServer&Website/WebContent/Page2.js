var flightNo = "", flightClass, SessionId = "", time, dateObj, timeTemp, webSocket, jsonObj, QueueListObj, sendData, packedData, count = 0, recv;
var QueueList = {
    'Queue1': "0 min", 'Queue2': "1 min", 'Queue3': "2 min", 'Queue4': "3 min", 'Queue5': "4 min",
    'Queue6': "5 min", 'Queue7': "4 min", 'Queue8': "3 min", 'Queue9': "5 min", 'Queue10': "9 min",
    'Queue11': "6 min", 'Queue12': "8 min", 'Queue13': "12 min", 'Queue14': "7 min", 'Queue15': "9 min",
    'Queue16': "7 min", 'Queue17': "2 min", 'Queue18': "8 min", 'Queue19': "4 min", 'Queue20': "7 min",
    'Queue21': "10 min"
}; //queue list for storing previous queue time for displaying if current is not updated from ML


$(document).ready(function () {

    $('#displayStopSignal').addClass("displayStopDivHidden");

    //accept flight no from previous js file
    recv = window.location.search;
    if (recv.substring(0, 1) == '?') {
        recv = recv.substring(1);
        recv = recv.split(",");
        flightNo = recv[0];
        flightClass = recv[1];
    }

    //obtain time ans set Session-Id
    dateObj = new Date();
    timeTemp = dateObj.toUTCString().split(' ');
    time = timeTemp[4];
    SessionId = flightNo + time;
    communicate();

});

//swipe and traverse the map on mobile devices (swipe up-down)
$(document).on("pagecreate", "#fullImage", function () {
    $("div").on("swipe", function () {
    });
});
//swipeleft
$(document).on("pagecreate", "#fullImage", function () {
    $("div").on("swipeleft", function () {
    });
});
//swiperight
$(document).on("pagecreate", "#fullImage", function () {
    $("div").on("swiperight", function () {
    });
});

function communicate() {
    var msg = document.getElementById("displayText");
    msg.value += "to connect";
    //make connection just once to java server
    webSocket = new WebSocket("ws://192.168.43.238:8080/JavaServer&Website/communicate");

    webSocket.onopen = function (message) { processOpen(message); };
    webSocket.onmessage = function (message) { processMessage(message); };
    webSocket.onclose = function (message) { processClose(message); };
    webSocket.onerror = function (message) { processError(message); };

    function processOpen(message) {
        msg.value += "Server Connected..." + "\n";

        $('#displayStopSignal').addClass("displayStopDivVisible");
        $('#stop').addClass("stopSignalClass");
        setTimeout(function () {
            $("#Dep1BusinessToEco").attr('title', "Now open for Economic class")     //dynamic updation of tooltip-text (i.e set queue time)
                         .tooltip('fixTitle')
                         .tooltip('show');
        }, 10000);
        setTimeout(function () {
            $("#Dep2BusinessToEco").attr('title', "Now open for Economic class")     //dynamic updation of tooltip-text (i.e set queue time)
                         .tooltip('fixTitle')
                         .tooltip('show');
        }, 15000);
        setInterval(sendMessage, 5000);
    }
    function processMessage(message) {
        var key;
        msg.value += "Received from server ; " + message.data + "\n";
        jsonObj = JSON.parse(message.data);
        var jsonKeys = Object.keys(jsonObj);
        var QueueListKeys = Object.keys(QueueList);
        msg.value += jsonKeys  + "\n";
        msg.value += QueueListKeys  + "\n";
        for (var i = 0; i < QueueListKeys.length; i++) {
            for (var j = 0; j < jsonKeys.length; j++) {
                if (QueueListKeys[i] == jsonKeys[j]) {
                    key = QueueListKeys[i];
                    msg.value += key + " : ";
                    QueueList[key] = jsonObj[key];
                    msg.value += QueueList[key] + "\n";
                }
            }
        }
        var tt = document.getElementById("TotalTime");
        tt.value = "Total Time: "+jsonObj.TotalTime;
        displayDep1();
        displayDep2();
      //displayDep3(); 
    }
    function processClose(message) {
        webSocket.send("Client Disconnected...");
        msg.value += "Server Disconnected..." + "\n";
    }
    function processError(message) {
        msg.value += "Error..." + "\n";
    }
    function sendMessage() {
        
    	sendData = { 'SID': SessionId, 'FlightNo': flightNo, 'FlightClass': flightClass };//, 'Latitude': latitude, 'Longitude': longitude };
        packedData = JSON.stringify(sendData);
        webSocket.send(packedData);
        msg.value += "Sent to server : " + packedData + "\n";
    }
    function displayDep1() {
        $("#Dep1EntryGate").attr('title', jsonObj.Queue1 || QueueList.Queue1)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');

        //departure1 checkin queue
        $("#Dep1CheckQ1").attr('title', jsonObj.Queue2 || QueueList.Queue2)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        $("#Dep1CheckQ2").attr('title', jsonObj.Queue3 || QueueList.Queue3)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        $("#Dep1CheckQ3").attr('title', jsonObj.Queue4 || QueueList.Queue4)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        //departure1 security queue
        $("#Dep1SecQ1").attr('title', jsonObj.Queue5 || QueueList.Queue5)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        $("#Dep1SecQ2").attr('title', jsonObj.Queue6 || QueueList.Queue6)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        //departure1 gates
        $("#Dep1BoardingGate").attr('title', jsonObj.Queue7 || QueueList.Queue7)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        
    }
    
    function displayDep2() {
        $("#Dep2EntryGate").attr('title', jsonObj.Queue8 || QueueList.Queue8)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');

        //departure2 checkin queue
        $("#Dep2CheckQ1").attr('title', jsonObj.Queue9 || QueueList.Queue9)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        $("#Dep2CheckQ2").attr('title', jsonObj.Queue10 || QueueList.Queue10)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        $("#Dep2CheckQ3").attr('title', jsonObj.Queue11 || QueueList.Queue11)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        //departure2 security queue
        $("#Dep2SecQ1").attr('title', jsonObj.Queue12 || QueueList.Queue12)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        $("#Dep2SecQ2").attr('title', jsonObj.Queue13 || QueueList.Queue13)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        //departure2 gates
        $("#Dep2BoardingGate").attr('title', jsonObj.Queue14 || QueueList.Queue14)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        
    }
    function displayDep3() {
        $("#Dep3EntryGate").attr('title', jsonObj.Queue15 || QueueList.Queue15)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');

        //departure1 checkin queue
        $("#Dep3CheckQ1").attr('title', jsonObj.Queue16 || QueueList.Queue16)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        $("#Dep3CheckQ2").attr('title', jsonObj.Queue17 || QueueList.Queue17)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        $("#Dep3CheckQ3").attr('title', jsonObj.Queue18 || QueueList.Queue18)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        //departure1 security queue
        $("#Dep3SecQ1").attr('title', jsonObj.Queue19 || QueueList.Queue19)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        $("#Dep3SecQ2").attr('title', jsonObj.Queue20 || QueueList.Queue20)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        //departure3 gates
        $("#Dep3BoardingGate").attr('title', jsonObj.Queue21 || QueueList.Queue21)     //dynamic updation of tooltip-text (i.e set queue time)
                     .tooltip('fixTitle')
                     .tooltip('show');
        
    }
}