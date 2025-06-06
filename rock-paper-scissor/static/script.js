function play(playerChoice) {
    fetch('/play', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ player: playerChoice })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('player-choice').innerText = "You chose: " + data.player;
        document.getElementById('computer-choice').innerText = "Computer chose: " + data.computer;
        document.getElementById('result').innerText = data.result;
    });
}