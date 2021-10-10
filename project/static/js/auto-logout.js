var timoutNow = 180000; // 180 Seconds of inactivity before the user is logged out.
var timeoutTimerID;

function startTimer() {
    window.clearTimeout(timeoutTimerID);
    timeoutTimerID = window.setTimeout(IdleTimeout, timoutNow);
}

function resetTimer() {
    window.clearTimeout(timeoutTimerID);
    startTimer();
}

function IdleTimeout() {
    window.location = '/login/endsession.do'  
}

function setupTimers () {
    document.addEventListener("mousemove", resetTimer, false);
    document.addEventListener("mousedown", resetTimer, false);
    document.addEventListener("keypress", resetTimer, false);
    document.addEventListener("touchmove", resetTimer, false);
    document.addEventListener("onscroll", resetTimer, false);
    startTimer();
}

function redirectToHome() {
    window.location = '/'  
}
